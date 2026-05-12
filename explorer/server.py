"""
KG Explorer — Backend
FastAPI server: loads .ttl, serves graph JSON, SPARQL, LLM Q&A, N-hop drill-down.

Usage:
    python -m explorer.server                         # default graph.ttl
    python -m explorer.server --ttl path/to/file.ttl  # custom TTL
    python -m explorer.server --port 8899
"""
import json, sys, os
from pathlib import Path
from collections import defaultdict
from fastapi import FastAPI, Query
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse, JSONResponse
from rdflib import Graph as RDFGraph, Namespace, RDF, RDFS
from rdflib.namespace import SKOS, DCTERMS
from llm.provider import LLMProviderManager
from store.sparql_store import SPARQLStore
from agent.qa_engine import QAEngine

KG = Namespace("http://kg.local/ontology#")
KGR = Namespace("http://kg.local/resource/")

# --- Unified LLM layer (replaces inline call_llm / llm_config) ---
llm_manager = LLMProviderManager("config.yaml")

# --- Agent layer (shared LLM provider) ---
sparql_store = SPARQLStore()
qa_engine: QAEngine | None = None  # initialized after graph loads

app = FastAPI(title="KG Studio")

# --- Mount new route modules ---
from explorer.routes.ingest import router as ingest_router
from explorer.routes.model import router as model_router
from explorer.routes.export import router as export_router
from explorer.routes.projects import router as projects_router
from explorer.routes.mapper import router as mapper_router
from explorer.routes.rdf_agent import router as rdf_agent_router
from explorer.routes.structured_ingest import router as structured_ingest_router
from explorer.routes.population import router as population_router
app.include_router(ingest_router)
app.include_router(model_router)
app.include_router(export_router)
app.include_router(projects_router)
app.include_router(mapper_router)
app.include_router(rdf_agent_router)
app.include_router(structured_ingest_router)
app.include_router(population_router)

# --- State ---
g: RDFGraph = None
nodes_cache: dict = {}
edges_cache: list = []
adj: dict = {}  # adjacency list for fast traversal


def uri_to_id(uri):
    s = str(uri)
    for prefix in ["http://kg.local/resource/", "http://kg.local/ontology#"]:
        if s.startswith(prefix):
            return s[len(prefix):]
    return s.split("/")[-1].split("#")[-1]


def get_label(uri):
    for _, _, o in g.triples((uri, SKOS.prefLabel, None)):
        return str(o)
    for _, _, o in g.triples((uri, RDFS.label, None)):
        return str(o)
    return uri_to_id(uri)


def get_type(uri):
    for _, _, o in g.triples((uri, RDF.type, None)):
        t = uri_to_id(o)
        if t not in ("Class", "ObjectProperty", "DatatypeProperty"):
            return t
    return "unknown"


def get_comment(uri):
    for _, _, o in g.triples((uri, RDFS.comment, None)):
        return str(o)
    return ""


def build_cache():
    global nodes_cache, edges_cache, adj
    nodes_cache = {}
    edges_cache = []
    adj = defaultdict(set)

    # Collect all subjects and objects that are URIs
    all_uris = set()
    for s, p, o in g:
        if hasattr(s, 'n3') and str(s).startswith("http://kg.local/"):
            all_uris.add(s)
        if hasattr(o, 'n3') and str(o).startswith("http://kg.local/"):
            all_uris.add(o)

    # Build nodes
    for uri in all_uris:
        nid = uri_to_id(uri)
        ntype = get_type(uri)
        if ntype in ("Class", "ObjectProperty", "DatatypeProperty"):
            continue
        nodes_cache[nid] = {
            "id": nid,
            "label": get_label(uri),
            "type": ntype,
            "description": get_comment(uri),
            "uri": str(uri),
        }

    # Build edges
    skip_preds = {str(RDF.type), str(SKOS.prefLabel), str(RDFS.label),
                  str(RDFS.comment), str(DCTERMS.source)}
    seen_edges = set()
    for s, p, o in g:
        if str(p) in skip_preds:
            continue
        sid = uri_to_id(s)
        oid = uri_to_id(o) if hasattr(o, 'n3') else None
        if not oid or sid not in nodes_cache or oid not in nodes_cache:
            continue
        edge_key = (sid, oid, uri_to_id(p))
        if edge_key in seen_edges:
            continue
        seen_edges.add(edge_key)
        edges_cache.append({
            "source": sid,
            "target": oid,
            "relation": uri_to_id(p),
        })
        adj[sid].add(oid)
        adj[oid].add(sid)

    print(f"  Cache: {len(nodes_cache)} nodes, {len(edges_cache)} edges")


# --- API ---

@app.get("/api/graph")
def get_graph():
    """Full graph for initial render."""
    return {"nodes": list(nodes_cache.values()), "edges": edges_cache}


@app.get("/api/expand")
def expand(node_id: str, hops: int = Query(default=2, ge=1, le=20)):
    """N-hop expansion from a node."""
    if node_id not in nodes_cache:
        return JSONResponse({"error": f"Node '{node_id}' not found"}, 404)

    visited = {node_id}
    frontier = [node_id]
    for _ in range(hops):
        next_f = []
        for nid in frontier:
            for neighbor in adj.get(nid, []):
                if neighbor not in visited:
                    visited.add(neighbor)
                    next_f.append(neighbor)
        frontier = next_f

    sub_nodes = [nodes_cache[n] for n in visited if n in nodes_cache]
    sub_edges = [e for e in edges_cache if e["source"] in visited and e["target"] in visited]
    return {"nodes": sub_nodes, "edges": sub_edges, "center": node_id, "hops": hops}


@app.get("/api/search")
def search(q: str, limit: int = 30):
    """Fuzzy search nodes."""
    ql = q.lower()
    results = []
    for n in nodes_cache.values():
        score = 0
        if ql == n["label"].lower():
            score = 100
        elif ql in n["label"].lower():
            score = 80
        elif ql in n["id"].lower():
            score = 60
        elif ql in n.get("description", "").lower():
            score = 40
        if score > 0:
            results.append({**n, "score": score})
    results.sort(key=lambda x: x["score"], reverse=True)
    return results[:limit]


@app.get("/api/neighbors")
def neighbors(node_id: str):
    """Direct neighbors of a node with edge info."""
    if node_id not in nodes_cache:
        return JSONResponse({"error": "Not found"}, 404)
    incoming = []
    outgoing = []
    for e in edges_cache:
        if e["source"] == node_id:
            outgoing.append({**nodes_cache.get(e["target"], {}), "relation": e["relation"], "direction": "out"})
        elif e["target"] == node_id:
            incoming.append({**nodes_cache.get(e["source"], {}), "relation": e["relation"], "direction": "in"})
    return {"node": nodes_cache[node_id], "incoming": incoming, "outgoing": outgoing}


@app.get("/api/path")
def shortest_path(source: str, target: str):
    """BFS shortest path."""
    if source not in nodes_cache or target not in nodes_cache:
        return JSONResponse({"error": "Node not found"}, 404)
    from collections import deque
    visited = {source}
    queue = deque([(source, [source])])
    while queue:
        current, path = queue.popleft()
        if current == target:
            path_nodes = [nodes_cache[n] for n in path if n in nodes_cache]
            path_edges = []
            for i in range(len(path) - 1):
                for e in edges_cache:
                    if (e["source"] == path[i] and e["target"] == path[i+1]) or \
                       (e["source"] == path[i+1] and e["target"] == path[i]):
                        path_edges.append(e)
                        break
            return {"path": path, "nodes": path_nodes, "edges": path_edges}
        for neighbor in adj.get(current, []):
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append((neighbor, path + [neighbor]))
    return {"path": [], "nodes": [], "edges": []}


@app.get("/api/sparql")
def run_sparql(query: str):
    """Execute raw SPARQL."""
    try:
        results = g.query(query)
        rows = []
        for row in results:
            rows.append({str(var): str(row[var]) for var in results.vars})
        return {"results": rows, "count": len(rows)}
    except Exception as e:
        return JSONResponse({"error": str(e)}, 400)


@app.get("/api/stats")
def stats():
    """Graph statistics."""
    types = defaultdict(int)
    relations = defaultdict(int)
    for n in nodes_cache.values():
        types[n["type"]] += 1
    for e in edges_cache:
        relations[e["relation"]] += 1
    return {
        "triples": len(g),
        "nodes": len(nodes_cache),
        "edges": len(edges_cache),
        "types": dict(sorted(types.items(), key=lambda x: -x[1])),
        "relations": dict(sorted(relations.items(), key=lambda x: -x[1])),
    }


# --- LLM endpoints (delegate to llm_manager) ---


def call_llm(prompt: str, system: str = "") -> str:
    """Backward-compatible wrapper — delegates to llm_manager.generate().

    Routes still import this until task 1.3 migrates them to llm_manager directly.
    """
    return llm_manager.generate(prompt, system)


@app.get("/api/llm/config")
def get_llm_config():
    """Get current LLM config."""
    cfg = llm_manager.config
    safe = {k: v for k, v in cfg.items() if k != "api_key"}
    safe["has_api_key"] = bool(cfg.get("api_key"))
    return safe


@app.post("/api/llm/config")
async def set_llm_config(body: dict):
    """Update LLM config from UI — delegates to llm_manager.reconfigure()."""
    llm_manager.reconfigure(body)
    # Return safe view of new config
    cfg = llm_manager.config
    safe = {k: v for k, v in cfg.items() if k != "api_key"}
    return {"status": "ok", "config": safe}


@app.post("/api/llm/test")
async def test_llm(body: dict = {}):
    """Test LLM connection."""
    try:
        result = llm_manager.generate("Say 'connected' in one word.", system="Respond with exactly one word.")
        return {"status": "ok", "response": result.strip()}
    except Exception as e:
        return JSONResponse({"status": "error", "error": str(e)}, 500)


# --- Context helpers ---


def _get_sparql_schema_hint() -> str:
    """Get schema hint for LLM-based SPARQL generation."""
    types = defaultdict(int)
    for n in nodes_cache.values():
        types[n["type"]] += 1
    if types:
        type_list = ", ".join(f"{t} ({c})" for t, c in sorted(types.items(), key=lambda x: -x[1])[:10])
        return f"Available node types in the graph: {type_list}"
    return ""


def get_context_for_question(question: str) -> tuple:
    """Pull relevant graph context for a question."""
    words = question.split()
    search_results = []
    for w in words[-3:]:
        if len(w) > 2:
            search_results.extend(search(w, limit=3))
    # dedupe
    seen = set()
    unique = []
    for r in search_results:
        if r["id"] not in seen:
            seen.add(r["id"])
            unique.append(r)
    search_results = unique[:6]

    context_parts = []
    for r in search_results:
        nb = neighbors(r["id"])
        lines = [f"{r['label']} ({r['type']})"]
        for conn in (nb.get("outgoing", []) + nb.get("incoming", []))[:8]:
            direction = "\u2192" if conn.get("direction") == "out" else "\u2190"
            lines.append(f"  {direction} {conn.get('label', '')} [{conn.get('relation', '')}]")
        context_parts.append("\n".join(lines))
    return "\n\n".join(context_parts), [r["id"] for r in search_results]


@app.post("/api/ask")
async def ask(body: dict):
    """LLM Q&A with graph context."""
    question = body.get("question", "")
    if not question:
        return JSONResponse({"error": "No question"}, 400)

    context, context_nodes = get_context_for_question(question)

    prompt = f"""Answer based on this knowledge graph context:

{context}

Question: {question}

Be specific, reference entities and relationships from the graph."""

    try:
        answer = llm_manager.generate(prompt, system="You answer questions using knowledge graph data. Be concise and specific.")
        return {"answer": answer, "context_nodes": context_nodes, "context": context}
    except Exception as e:
        return {"answer": f"LLM unavailable: {e}\n\nHere's what the graph knows:\n\n{context}", "context_nodes": context_nodes, "context": context, "llm_error": str(e)}


@app.post("/api/ask/sparql")
async def ask_sparql(body: dict):
    """Smart SPARQL — tries template matching first, falls back to LLM."""
    question = body.get("question", "")
    if not question:
        return JSONResponse({"error": "No question"}, 400)

    ql = question.lower()

    # Track whether SPARQL was generated by LLM (for fallback handling)
    llm_generated = False

    # --- Template matching (no LLM needed) ---
    sparql = None
    if any(w in ql for w in ["implement", "implements", "implementing"]):
        # "What implements X" or "What services implement X"
        for word in ql.replace("?", "").split():
            if len(word) > 3 and word not in ("what", "which", "services", "service", "implement", "implements", "implementing", "that", "does"):
                sparql = f"""PREFIX kg: <http://kg.local/ontology#>
PREFIX skos: <http://www.w3.org/2004/02/skos/core#>
SELECT ?serviceLabel ?conceptLabel WHERE {{
  ?svc kg:implements ?concept .
  ?concept skos:prefLabel ?conceptLabel .
  FILTER(CONTAINS(LCASE(STR(?conceptLabel)), "{word}"))
  ?svc skos:prefLabel ?serviceLabel .
}}"""
                break

    elif any(w in ql for w in ["best practice", "best practices", "practices for", "bp for"]):
        pillar = None
        for p in ["security", "reliability", "operational", "performance", "cost", "sustainability"]:
            if p in ql:
                pillar = p
                break
        if pillar:
            pillar_map = {"security": "security", "reliability": "reliability", "operational": "operational_excellence", "performance": "performance_efficiency", "cost": "cost_optimization", "sustainability": "sustainability"}
            pid = pillar_map.get(pillar, pillar)
            sparql = f"""PREFIX kg: <http://kg.local/ontology#>
PREFIX kgr: <http://kg.local/resource/>
PREFIX skos: <http://www.w3.org/2004/02/skos/core#>
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
SELECT ?bpLabel WHERE {{
  ?bp rdf:type kg:BestPractice .
  ?bp skos:broader kgr:{pid} .
  ?bp skos:prefLabel ?bpLabel .
}} ORDER BY ?bpLabel"""

    elif any(w in ql for w in ["what does", "what can", "capabilities of", "features of"]):
        for word in ql.replace("?", "").split():
            if len(word) > 4 and word not in ("what", "does", "features", "capabilities"):
                sparql = f"""PREFIX kg: <http://kg.local/ontology#>
PREFIX skos: <http://www.w3.org/2004/02/skos/core#>
SELECT ?conceptLabel WHERE {{
  ?svc kg:implements ?concept .
  ?svc skos:prefLabel ?svcLabel .
  FILTER(CONTAINS(LCASE(STR(?svcLabel)), "{word}"))
  ?concept skos:prefLabel ?conceptLabel .
}}"""
                break

    elif any(w in ql for w in ["how many", "count", "total"]):
        if "service" in ql:
            sparql = """PREFIX kg: <http://kg.local/ontology#>
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
SELECT (COUNT(?s) as ?count) WHERE { ?s rdf:type kg:Service . }"""
        elif "best practice" in ql or "bp" in ql:
            sparql = """PREFIX kg: <http://kg.local/ontology#>
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
SELECT (COUNT(?s) as ?count) WHERE { ?s rdf:type kg:BestPractice . }"""
        elif "concept" in ql:
            sparql = """PREFIX kg: <http://kg.local/ontology#>
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
SELECT (COUNT(?s) as ?count) WHERE { ?s rdf:type kg:Concept . }"""

    elif any(w in ql for w in ["relate", "related", "connects", "connected", "linked"]):
        for word in ql.replace("?", "").split():
            if len(word) > 4 and word not in ("what", "relate", "related", "connects", "connected", "linked", "nodes"):
                sparql = f"""PREFIX kg: <http://kg.local/ontology#>
PREFIX skos: <http://www.w3.org/2004/02/skos/core#>
SELECT ?relatedLabel ?relation WHERE {{
  ?node skos:prefLabel ?nLabel .
  FILTER(CONTAINS(LCASE(STR(?nLabel)), "{word}"))
  {{ ?node ?rel ?related . ?related skos:prefLabel ?relatedLabel . BIND(STR(?rel) as ?relation) }}
  UNION
  {{ ?related ?rel ?node . ?related skos:prefLabel ?relatedLabel . BIND(STR(?rel) as ?relation) }}
}} LIMIT 30"""
                break

    elif any(w in ql for w in ["mitigate", "prevent", "protect", "anti-pattern"]):
        sparql = """PREFIX kg: <http://kg.local/ontology#>
PREFIX skos: <http://www.w3.org/2004/02/skos/core#>
SELECT ?bpLabel ?antiLabel WHERE {
  ?bp kg:mitigates ?anti .
  ?bp skos:prefLabel ?bpLabel .
  ?anti skos:prefLabel ?antiLabel .
}"""

    elif any(w in ql for w in ["pillar", "pillars"]):
        sparql = """PREFIX kg: <http://kg.local/ontology#>
PREFIX skos: <http://www.w3.org/2004/02/skos/core#>
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
SELECT ?pillarLabel (COUNT(?bp) as ?bpCount) WHERE {
  ?pillar rdf:type kg:Pillar .
  ?pillar skos:prefLabel ?pillarLabel .
  ?bp skos:broader ?pillar .
} GROUP BY ?pillarLabel ORDER BY DESC(?bpCount)"""

    elif "disaster recovery" in ql or "dr strateg" in ql:
        sparql = """PREFIX kg: <http://kg.local/ontology#>
PREFIX skos: <http://www.w3.org/2004/02/skos/core#>
SELECT ?label ?relatedLabel WHERE {
  ?n skos:prefLabel ?label .
  FILTER(CONTAINS(LCASE(STR(?label)), "recovery") || CONTAINS(LCASE(STR(?label)), "disaster") || CONTAINS(LCASE(STR(?label)), "standby") || CONTAINS(LCASE(STR(?label)), "pilot") || CONTAINS(LCASE(STR(?label)), "active/active"))
  OPTIONAL { ?n kg:relates_to ?r . ?r skos:prefLabel ?relatedLabel . }
}"""

    # --- Execute ---
    if not sparql:
        # Try LLM-based SPARQL generation when templates don't match
        llm_generated = False
        try:
            schema_hint = _get_sparql_schema_hint()
            sparql_prompt = (
                f"Generate a SPARQL query to answer this question about a knowledge graph.\n"
                f"The graph uses these prefixes:\n"
                f"  PREFIX kg: <http://kg.local/ontology#>\n"
                f"  PREFIX kgr: <http://kg.local/resource/>\n"
                f"  PREFIX skos: <http://www.w3.org/2004/02/skos/core#>\n"
                f"  PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>\n"
                f"  PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>\n\n"
                f"{schema_hint}\n\n"
                f"Question: {question}\n\n"
                f"Return ONLY the SPARQL query, no explanation."
            )
            raw_sparql = llm_manager.generate(
                sparql_prompt,
                system="You are a SPARQL query generator. Return only valid SPARQL queries."
            )
            # Clean up LLM response (strip markdown fences)
            raw_sparql = raw_sparql.strip()
            if raw_sparql.startswith("```"):
                raw_sparql = raw_sparql.split("\n", 1)[1] if "\n" in raw_sparql else raw_sparql[3:]
                if raw_sparql.endswith("```"):
                    raw_sparql = raw_sparql[:-3]
            sparql = raw_sparql.strip()
            llm_generated = True
        except Exception:
            # LLM unavailable — fall back to generic keyword-based SPARQL
            words = [w for w in ql.replace("?", "").split() if len(w) > 3 and w not in ("what", "which", "where", "how", "does", "about", "tell", "show", "list", "find", "that", "this", "with", "from", "have", "the", "more")]
            if words:
                term = sorted(words, key=len, reverse=True)[0]
                sparql = f"""PREFIX skos: <http://www.w3.org/2004/02/skos/core#>
PREFIX kg: <http://kg.local/ontology#>
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
SELECT ?label ?type ?description ?relatedLabel ?relation WHERE {{
  ?s skos:prefLabel ?label .
  ?s a ?type .
  FILTER(CONTAINS(LCASE(STR(?label)), "{term.lower()}"))
  OPTIONAL {{ ?s rdfs:comment ?description . }}
  OPTIONAL {{
    ?s ?rel ?related .
    ?related skos:prefLabel ?relatedLabel .
    BIND(REPLACE(STR(?rel), ".*[#/]", "") as ?relation)
  }}
}} LIMIT 50"""
            else:
                # No keywords and no LLM — return context-based fallback
                context, context_nodes = get_context_for_question(question)
                if context:
                    return {"answer": f"LLM unavailable for SPARQL generation. Here's what the graph knows:\n\n{context}", "sparql": "", "results": [], "count": 0, "context": context, "context_nodes": context_nodes, "llm_error": "LLM unavailable"}
                return {"answer": "Could not understand the question. Try: 'What services implement observability?' or 'Best practices for security'", "sparql": "", "results": [], "count": 0}

    try:
        results = g.query(sparql)
        rows = [{str(var): str(row[var]) for var in results.vars} for row in results]
        # Format answer
        if not rows:
            answer = "No results found for that query."
        elif len(rows) == 1 and "count" in rows[0]:
            answer = f"Count: {rows[0]['count']}"
        else:
            # Group by main entity for readable output
            grouped = {}
            for row in rows[:50]:
                vals = list(row.values())
                key = vals[0] if vals else ""
                if key not in grouped:
                    grouped[key] = {"type": vals[1] if len(vals) > 1 else "", "desc": "", "connections": []}
                if len(vals) > 2 and vals[2] and vals[2] != "None":
                    grouped[key]["desc"] = vals[2]
                if len(vals) > 3 and vals[3] and vals[3] != "None":
                    rel = vals[4] if len(vals) > 4 else ""
                    conn = f"{vals[3]} [{rel}]" if rel and rel != "None" else vals[3]
                    if conn not in grouped[key]["connections"]:
                        grouped[key]["connections"].append(conn)

            lines = []
            for name, info in grouped.items():
                t = info['type'].split('#')[-1].split('/')[-1] if info['type'] else ''
                line = f"\u25cf {name} ({t})"
                if info['desc']:
                    line += f"\n  {info['desc']}"
                for c in info['connections'][:10]:
                    line += f"\n  \u2192 {c}"
                lines.append(line)
            answer = "\n\n".join(lines)
        return {"answer": answer, "sparql": sparql, "results": rows[:30], "count": len(rows)}
    except Exception as e:
        # If LLM-generated SPARQL failed, fall back to context-based answer
        if llm_generated:
            context, context_nodes = get_context_for_question(question)
            if context:
                return {"answer": f"SPARQL query failed. Here's what the graph knows:\n\n{context}", "sparql": sparql, "results": [], "count": 0, "context": context, "context_nodes": context_nodes, "sparql_error": str(e)}
        return JSONResponse({"error": str(e), "sparql": sparql}, 400)


# --- State for new/current model (separate from main graph) ---
new_model_ttl = ""
new_model_nodes = []
new_model_edges = []


def get_project_context(question: str) -> tuple:
    """Pull context from the project graph (new_model_nodes/edges)."""
    if not new_model_nodes:
        return "", []
    ql = question.lower()
    # Find relevant nodes by keyword match
    words = [w for w in ql.replace("?", "").split() if len(w) > 2]
    matched = []
    for n in new_model_nodes:
        for w in words:
            if w in n.get("label", "").lower() or w in n.get("id", "").lower():
                matched.append(n)
                break
    if not matched:
        matched = new_model_nodes[:10]  # fallback: show some nodes
    matched = matched[:8]
    # Build adjacency from edges
    node_map = {n["id"]: n for n in new_model_nodes}
    context_parts = []
    for n in matched:
        lines = [f"{n.get('label', n['id'])} ({n.get('type', 'unknown')})"]
        for e in new_model_edges:
            if e["source"] == n["id"]:
                t = node_map.get(e["target"], {})
                lines.append(f"  \u2192 {t.get('label', e['target'])} [{e['relation']}]")
            elif e["target"] == n["id"]:
                s = node_map.get(e["source"], {})
                lines.append(f"  \u2190 {s.get('label', e['source'])} [{e['relation']}]")
        context_parts.append("\n".join(lines[:12]))
    return "\n\n".join(context_parts), [n["id"] for n in matched]


@app.post("/api/ask/project")
async def ask_project(body: dict):
    """LLM Q&A using the project graph context (new_model_nodes)."""
    question = body.get("question", "")
    if not question:
        return JSONResponse({"error": "No question"}, 400)

    context, context_nodes = get_project_context(question)
    if not context:
        return {"answer": "No project graph loaded. Build a graph first.", "context_nodes": []}

    prompt = f"""Answer based ONLY on this knowledge graph context. Do not make up information.

{context}

Question: {question}

Be specific, reference entities and relationships from the graph."""

    try:
        answer = llm_manager.generate(prompt, system="You answer questions using ONLY the provided knowledge graph data. Be concise and specific. If the answer is not in the context, say so.")
        return {"answer": answer, "context_nodes": context_nodes, "context": context}
    except Exception as e:
        return {"answer": f"LLM unavailable. Here's what the project graph knows:\n\n{context}", "context_nodes": context_nodes, "context": context, "llm_error": str(e)}


@app.get("/api/new-graph")
def get_new_graph():
    """Get only the newly modeled graph (not the full main graph)."""
    return {"nodes": new_model_nodes, "edges": new_model_edges}


@app.get("/view-new")
def view_new():
    """Serve explorer loaded with only the new model."""
    return FileResponse(str(static_dir / "view_new.html"))


@app.post("/api/reload")
async def reload_graph():
    """Reload graph from TTL without restarting server."""
    global g, qa_engine
    ttl_path = Path("graphify-out/graph.ttl")
    if not ttl_path.exists():
        return JSONResponse({"error": "No graph.ttl found"}, 404)
    from rdflib import Graph as RDFGraph
    g = RDFGraph()
    g.bind("kg", KG)
    g.bind("kgr", KGR)
    g.bind("skos", SKOS)
    g.bind("dcterms", DCTERMS)
    g.parse(str(ttl_path), format="turtle")
    build_cache()
    # Re-initialize agent layer with reloaded graph
    sparql_store.graph = g
    qa_engine = QAEngine(sparql_store, llm_manager.provider)
    return {"status": "ok", "triples": len(g), "nodes": len(nodes_cache), "edges": len(edges_cache)}


# --- Static files + SPA ---
static_dir = Path(__file__).parent / "static"
app.mount("/static", StaticFiles(directory=str(static_dir)), name="static")

@app.get("/")
def index():
    return FileResponse(str(static_dir / "index.html"))

@app.get("/studio")
def studio():
    return FileResponse(str(static_dir / "studio.html"))


# --- Startup ---
def load_ttl(ttl_path: str):
    global g, qa_engine
    g = RDFGraph()
    g.bind("kg", KG)
    g.bind("kgr", KGR)
    g.bind("skos", SKOS)
    g.bind("dcterms", DCTERMS)
    if not Path(ttl_path).exists():
        print(f"  No graph file at {ttl_path} — starting with empty graph")
        build_cache()
        return
    print(f"Loading: {ttl_path}")
    g.parse(ttl_path, format="turtle")
    print(f"  Loaded: {len(g)} triples")
    build_cache()
    # Re-initialize agent layer with loaded graph
    sparql_store.graph = g
    qa_engine = QAEngine(sparql_store, llm_manager.provider)


if __name__ == "__main__":
    import argparse, uvicorn
    parser = argparse.ArgumentParser()
    parser.add_argument("--ttl", default="graphify-out/graph.ttl")
    parser.add_argument("--port", type=int, default=8899)
    parser.add_argument("--host", default="127.0.0.1")
    args = parser.parse_args()
    load_ttl(args.ttl)
    print(f"\n  KG Explorer \u2192 http://{args.host}:{args.port}\n")
    uvicorn.run(app, host=args.host, port=args.port, log_level="warning")
