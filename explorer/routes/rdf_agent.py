"""
RDF Agent routes — LLM-powered agent that:
1. Builds RDF from natural language or data
2. Shows modeling techniques/patterns
3. Converts visual graphs (gra.fo style) to RDF
4. Teaches ontology design patterns
"""
import json
import re
from pathlib import Path
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from rdflib import Graph as RDFGraph

router = APIRouter(prefix="/api/rdf-agent", tags=["rdf-agent"])

# Modeling patterns library
PATTERNS = {
    "hierarchy": {
        "name": "Class Hierarchy (rdfs:subClassOf)",
        "description": "Model is-a relationships. E.g. ElectricCar subClassOf Car subClassOf Vehicle.",
        "ttl": """@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .
@prefix kg: <http://kg.local/ontology#> .

kg:Vehicle a owl:Class ; rdfs:label "Vehicle" .
kg:Car a owl:Class ; rdfs:subClassOf kg:Vehicle ; rdfs:label "Car" .
kg:ElectricCar a owl:Class ; rdfs:subClassOf kg:Car ; rdfs:label "Electric Car" .""",
        "when": "When you have is-a / type-of relationships"
    },
    "composition": {
        "name": "Composition (hasPart / partOf)",
        "description": "Model whole-part relationships. E.g. Engine is part of Car.",
        "ttl": """@prefix owl: <http://www.w3.org/2002/07/owl#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .
@prefix kg: <http://kg.local/ontology#> .
@prefix kgr: <http://kg.local/resource/> .

kg:hasPart a owl:ObjectProperty ; rdfs:label "has part" ;
    rdfs:domain kg:System ; rdfs:range kg:Component .
kg:partOf a owl:ObjectProperty ; owl:inverseOf kg:hasPart .

kgr:my_car a kg:Car ; kg:hasPart kgr:engine_v8 .""",
        "when": "When something contains or is composed of other things"
    },
    "event_pattern": {
        "name": "Event Pattern (temporal)",
        "description": "Model things that happen at a point in time with actors and outcomes.",
        "ttl": """@prefix owl: <http://www.w3.org/2002/07/owl#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .
@prefix kg: <http://kg.local/ontology#> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

kg:Event a owl:Class .
kg:hasActor a owl:ObjectProperty ; rdfs:domain kg:Event ; rdfs:range kg:Agent .
kg:hasTime a owl:DatatypeProperty ; rdfs:domain kg:Event ; rdfs:range xsd:dateTime .
kg:hasOutcome a owl:ObjectProperty ; rdfs:domain kg:Event ; rdfs:range kg:Outcome .""",
        "when": "When modeling processes, incidents, transactions, or anything time-based"
    },
    "role_pattern": {
        "name": "Role Pattern (n-ary relation)",
        "description": "When an entity plays different roles in different contexts.",
        "ttl": """@prefix owl: <http://www.w3.org/2002/07/owl#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .
@prefix kg: <http://kg.local/ontology#> .

kg:Membership a owl:Class ; rdfs:label "Membership" .
kg:hasMember a owl:ObjectProperty ; rdfs:domain kg:Membership ; rdfs:range kg:Person .
kg:hasRole a owl:ObjectProperty ; rdfs:domain kg:Membership ; rdfs:range kg:Role .
kg:inOrganization a owl:ObjectProperty ; rdfs:domain kg:Membership ; rdfs:range kg:Organization .""",
        "when": "When the same entity has different roles in different contexts (reification)"
    },
    "dependency": {
        "name": "Dependency Graph",
        "description": "Model depends-on relationships between services/components.",
        "ttl": """@prefix owl: <http://www.w3.org/2002/07/owl#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .
@prefix kg: <http://kg.local/ontology#> .
@prefix kgr: <http://kg.local/resource/> .

kg:dependsOn a owl:ObjectProperty ; rdfs:label "depends on" ;
    rdfs:domain kg:Service ; rdfs:range kg:Service .
kg:implements a owl:ObjectProperty ; rdfs:label "implements" ;
    rdfs:domain kg:Service ; rdfs:range kg:Concept .

kgr:auth_service a kg:Service ; rdfs:label "Auth Service" .
kgr:user_service a kg:Service ; rdfs:label "User Service" ;
    kg:dependsOn kgr:auth_service .""",
        "when": "Microservices, software components, infrastructure dependencies"
    },
    "taxonomy": {
        "name": "SKOS Taxonomy",
        "description": "Model controlled vocabularies with broader/narrower/related.",
        "ttl": """@prefix skos: <http://www.w3.org/2004/02/skos/core#> .
@prefix kgr: <http://kg.local/resource/> .

kgr:technology a skos:Concept ; skos:prefLabel "Technology" .
kgr:cloud_computing a skos:Concept ; skos:prefLabel "Cloud Computing" ;
    skos:broader kgr:technology .
kgr:serverless a skos:Concept ; skos:prefLabel "Serverless" ;
    skos:broader kgr:cloud_computing ;
    skos:related kgr:microservices .""",
        "when": "Categorization, tagging systems, knowledge organization"
    },
    "provenance": {
        "name": "Provenance (who/when/where)",
        "description": "Track where data came from, who created it, when.",
        "ttl": """@prefix dcterms: <http://purl.org/dc/terms/> .
@prefix prov: <http://www.w3.org/ns/prov#> .
@prefix kg: <http://kg.local/ontology#> .
@prefix kgr: <http://kg.local/resource/> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

kgr:report_2024 a kg:Document ;
    dcterms:creator kgr:alice ;
    dcterms:created "2024-01-15"^^xsd:date ;
    dcterms:source "internal_wiki" ;
    prov:wasGeneratedBy kgr:quarterly_review .""",
        "when": "When you need audit trails, data lineage, or attribution"
    },
}


@router.get("/patterns")
def list_patterns():
    """List all available modeling patterns."""
    return {"patterns": [{"id": k, **{kk: vv for kk, vv in v.items() if kk != "ttl"}} for k, v in PATTERNS.items()]}


@router.get("/patterns/{pattern_id}")
def get_pattern(pattern_id: str):
    """Get a specific pattern with full TTL example."""
    if pattern_id not in PATTERNS:
        return JSONResponse({"error": "Pattern not found"}, 404)
    return PATTERNS[pattern_id]


@router.post("/build")
async def build_rdf(body: dict):
    """
    RDF Agent: takes natural language description and builds RDF.
    Input: {"description": "I have services: Auth, User, Payment. User depends on Auth. Payment depends on Auth and User."}
    Output: {"ttl": "...", "explanation": "...", "pattern_used": "dependency"}
    """
    description = body.get("description", "")
    context = body.get("context", "")  # existing TTL to extend
    if not description:
        return JSONResponse({"error": "No description"}, 400)

    patterns_summary = "\n".join(f"- {k}: {v['name']} — {v['when']}" for k, v in PATTERNS.items())

    prompt = f"""You are an RDF/OWL ontology builder. Convert the user's description into valid Turtle (TTL) syntax.

Available modeling patterns:
{patterns_summary}

{"Existing ontology context:" + chr(10) + context[:2000] if context else ""}

User description: {description}

Rules:
1. Use prefixes: @prefix kg: <http://kg.local/ontology#> . @prefix kgr: <http://kg.local/resource/> . @prefix owl: <http://www.w3.org/2002/07/owl#> . @prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> . @prefix skos: <http://www.w3.org/2004/02/skos/core#> . @prefix xsd: <http://www.w3.org/2001/XMLSchema#> .
2. Define classes with owl:Class, properties with owl:ObjectProperty or owl:DatatypeProperty
3. Create instances with kgr: prefix
4. Always add rdfs:label or skos:prefLabel
5. Use the most appropriate pattern from above

Return JSON: {{"ttl": "valid turtle syntax", "explanation": "what you modeled and why", "pattern_used": "pattern_id_or_custom", "classes": ["list of class names"], "instances": ["list of instance names"]}}
Return ONLY valid JSON."""

    try:
        from explorer.server import llm_manager
        raw = llm_manager.generate(prompt, system="You are an expert RDF/OWL ontology engineer. Always produce valid Turtle syntax. Return only JSON.")
        raw = raw.strip()
        if raw.startswith("```"):
            raw = raw.split("\n", 1)[1] if "\n" in raw else raw[3:]
            if raw.endswith("```"):
                raw = raw[:-3]
        result = json.loads(raw.strip())
        # Validate the TTL
        if result.get("ttl"):
            try:
                g = RDFGraph()
                g.parse(data=result["ttl"], format="turtle")
                result["valid"] = True
                result["triples"] = len(g)
            except Exception as e:
                result["valid"] = False
                result["validation_error"] = str(e)
        return result
    except Exception as e:
        return {"error": str(e), "ttl": "", "explanation": "LLM unavailable. Use patterns library or visual modeler instead."}


@router.post("/convert-visual")
async def convert_visual(body: dict):
    """
    Convert a visual graph (gra.fo style nodes+edges) to RDF.
    Input: {"nodes": [{"id": "x", "label": "X", "type": "class|instance"}], "edges": [{"source": "x", "target": "y", "label": "relates_to"}]}
    """
    nodes = body.get("nodes", [])
    edges = body.get("edges", [])
    if not nodes:
        return JSONResponse({"error": "No nodes"}, 400)

    lines = [
        "@prefix owl: <http://www.w3.org/2002/07/owl#> .",
        "@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .",
        "@prefix kg: <http://kg.local/ontology#> .",
        "@prefix kgr: <http://kg.local/resource/> .",
        "@prefix skos: <http://www.w3.org/2004/02/skos/core#> .",
        "@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .",
        "",
    ]

    node_map = {}
    for n in nodes:
        nid = re.sub(r'[^a-z0-9_]', '_', n.get("id", "").lower())[:60]
        node_map[n["id"]] = nid
        label = n.get("label", nid).replace('"', '\\"')
        ntype = n.get("type", "class")

        if ntype == "class":
            lines.append(f'kg:{nid} a owl:Class ; rdfs:label "{label}" .')
        else:
            # Instance — find its class from edges or default
            cls = "Concept"
            for e in edges:
                if e["source"] == n["id"] and e.get("label", "").lower() in ("a", "type", "rdf:type", "is_a"):
                    cls = re.sub(r'[^a-z0-9_]', '_', e["target"].lower())[:60]
                    break
            lines.append(f'kgr:{nid} a kg:{cls} ; skos:prefLabel "{label}" .')
        lines.append("")

    # Edges as properties
    for e in edges:
        sid = node_map.get(e["source"], "")
        tid = node_map.get(e["target"], "")
        if not sid or not tid:
            continue
        rel = e.get("label", "relates_to")
        if rel.lower() in ("a", "type", "rdf:type", "is_a"):
            continue  # already handled
        rel_id = re.sub(r'[^a-z0-9_]', '_', rel.lower())[:60]
        # Determine if source is class or instance
        src_node = next((n for n in nodes if n["id"] == e["source"]), {})
        if src_node.get("type") == "class":
            lines.append(f'kg:{rel_id} a owl:ObjectProperty ; rdfs:label "{rel}" ; rdfs:domain kg:{sid} ; rdfs:range kg:{tid} .')
        else:
            lines.append(f'kgr:{sid} kg:{rel_id} kgr:{tid} .')
        lines.append("")

    ttl = "\n".join(lines)
    # Validate
    try:
        g = RDFGraph()
        g.parse(data=ttl, format="turtle")
        return {"ttl": ttl, "valid": True, "triples": len(g)}
    except Exception as e:
        return {"ttl": ttl, "valid": False, "error": str(e)}


@router.post("/teach")
async def teach_modeling(body: dict):
    """
    Ask the agent to explain a modeling technique or suggest how to model something.
    Input: {"question": "How do I model many-to-many relationships in RDF?"}
    """
    question = body.get("question", "")
    if not question:
        return JSONResponse({"error": "No question"}, 400)

    patterns_detail = "\n\n".join(f"### {v['name']}\n{v['description']}\nUse when: {v['when']}\nExample:\n```turtle\n{v['ttl']}\n```" for v in PATTERNS.values())

    prompt = f"""You are an RDF/OWL modeling teacher. Answer the user's question about ontology modeling.

Reference patterns:
{patterns_detail}

Question: {question}

Provide:
1. Clear explanation
2. A concrete TTL example
3. Which pattern(s) apply
4. Common mistakes to avoid

Be concise but thorough."""

    try:
        from explorer.server import llm_manager
        answer = llm_manager.generate(prompt, system="You teach RDF/OWL ontology modeling. Give practical examples in Turtle syntax.")
        return {"answer": answer, "related_patterns": [k for k, v in PATTERNS.items() if any(w in question.lower() for w in v["when"].lower().split())]}
    except Exception as e:
        # Fallback: find relevant pattern
        relevant = []
        ql = question.lower()
        for k, v in PATTERNS.items():
            if any(w in ql for w in k.split("_")) or any(w in ql for w in v["when"].lower().split()[:5]):
                relevant.append(v)
        if relevant:
            answer = f"**{relevant[0]['name']}**\n\n{relevant[0]['description']}\n\nUse when: {relevant[0]['when']}\n\n```turtle\n{relevant[0]['ttl']}\n```"
        else:
            answer = "LLM unavailable. Browse the patterns library with GET /api/rdf-agent/patterns for examples."
        return {"answer": answer, "related_patterns": [k for k in PATTERNS if any(w in ql for w in k.split("_"))]}
