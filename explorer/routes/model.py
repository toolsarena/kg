"""
Model routes — ontology building via LLM conversation, TTL upload/validate, visual modeler.
"""
import re
import json
from pathlib import Path
from fastapi import APIRouter, UploadFile, File
from fastapi.responses import JSONResponse
from rdflib import Graph as RDFGraph

router = APIRouter(prefix="/api/model", tags=["model"])

ONTOLOGY_DIR = Path("ontologies")
ONTOLOGY_DIR.mkdir(exist_ok=True)

# Conversation state per session (simple in-memory)
conversations = {}


@router.post("/validate")
async def validate_ttl(body: dict):
    """Validate TTL/Turtle content."""
    ttl = body.get("ttl", "")
    if not ttl:
        return JSONResponse({"error": "No TTL content"}, 400)
    try:
        g = RDFGraph()
        g.parse(data=ttl, format="turtle")
        # Extract stats
        classes = list(g.query("SELECT ?c WHERE { ?c a <http://www.w3.org/2002/07/owl#Class> }"))
        props = list(g.query("SELECT ?p WHERE { ?p a ?t . FILTER(?t IN (<http://www.w3.org/2002/07/owl#ObjectProperty>, <http://www.w3.org/2002/07/owl#DatatypeProperty>)) }"))
        return {
            "valid": True,
            "triples": len(g),
            "classes": len(classes),
            "properties": len(props),
        }
    except Exception as e:
        return {"valid": False, "error": str(e)}


@router.post("/upload-ttl")
async def upload_ttl(file: UploadFile = File(...)):
    """Upload and validate a TTL file, save to ontologies/."""
    content = await file.read()
    text = content.decode("utf-8", errors="ignore")
    try:
        g = RDFGraph()
        g.parse(data=text, format="turtle")
        # Save
        save_path = ONTOLOGY_DIR / (file.filename or "uploaded.ttl")
        save_path.write_text(text, encoding="utf-8")
        return {
            "valid": True,
            "triples": len(g),
            "saved_to": str(save_path),
            "filename": file.filename,
        }
    except Exception as e:
        return JSONResponse({"valid": False, "error": str(e)}, 400)


@router.post("/merge-ttl")
async def merge_ttl(body: dict):
    """Merge TTL content into the main graph and reload."""
    ttl = body.get("ttl", "")
    if not ttl:
        return JSONResponse({"error": "No TTL"}, 400)
    try:
        # Validate first
        test = RDFGraph()
        test.parse(data=ttl, format="turtle")
        # Append to main graph file
        graph_path = Path("graphify-out/graph.ttl")
        with open(graph_path, "a", encoding="utf-8") as f:
            f.write("\n\n# --- Merged from modeler ---\n")
            f.write(ttl)
        # Reload into new model view (separate from main graph)
        try:
            import explorer.server as srv
            from rdflib import Graph as RG2, RDF, Namespace
            from rdflib.namespace import SKOS, RDFS
            ng = RG2()
            ng.parse(data=ttl, format="turtle")
            srv.new_model_ttl = ttl
            # Build nodes/edges for new model
            srv.new_model_nodes = []
            srv.new_model_edges = []
            all_uris = set()
            for s, p, o in ng:
                if hasattr(s, 'n3'):
                    all_uris.add(s)
                if hasattr(o, 'n3') and str(o).startswith('http'):
                    all_uris.add(o)
            skip_preds = {str(RDF.type), str(SKOS.prefLabel), str(RDFS.label), str(RDFS.comment)}
            node_ids = set()
            for uri in all_uris:
                uid = str(uri).split('/')[-1].split('#')[-1]
                label = uid
                for _, _, o in ng.triples((uri, RDFS.label, None)):
                    label = str(o)
                for _, _, o in ng.triples((uri, SKOS.prefLabel, None)):
                    label = str(o)
                ntype = 'concept'
                for _, _, o in ng.triples((uri, RDF.type, None)):
                    t = str(o).split('#')[-1].split('/')[-1]
                    if t not in ('Class','ObjectProperty','DatatypeProperty','Ontology'):
                        ntype = t.lower()
                srv.new_model_nodes.append({'id': uid, 'label': label, 'type': ntype, 'uri': str(uri)})
                node_ids.add(uid)
            for s, p, o in ng:
                if str(p) in skip_preds:
                    continue
                sid = str(s).split('/')[-1].split('#')[-1]
                oid = str(o).split('/')[-1].split('#')[-1] if hasattr(o, 'n3') else None
                if oid and sid in node_ids and oid in node_ids:
                    rel = str(p).split('/')[-1].split('#')[-1]
                    srv.new_model_edges.append({'source': sid, 'target': oid, 'relation': rel})
        except Exception:
            pass
        return {"merged": True, "new_triples": len(test)}
    except Exception as e:
        return JSONResponse({"error": str(e)}, 400)


@router.post("/conversation")
async def model_conversation(body: dict):
    """LLM-assisted ontology modeling conversation."""
    session_id = body.get("session_id", "default")
    project_id = body.get("project_id")        # NEW — target project
    active_file = body.get("active_file")      # NEW — e.g. "telecom_model.ttl"
    message = body.get("message", "")
    if not message:
        return JSONResponse({"error": "No message"}, 400)

    # Get or create conversation
    if session_id not in conversations:
        conversations[session_id] = {
            "history": [],
            "ontology": {"classes": [], "properties": [], "relationships": []},
            "ttl": "",
        }
    conv = conversations[session_id]
    conv["history"].append({"role": "user", "content": message})

    # Build prompt with conversation history + current ontology state
    ontology_state = json.dumps(conv["ontology"], indent=2) if conv["ontology"]["classes"] else "Empty — no classes defined yet."
    history_text = "\n".join(f"{m['role'].upper()}: {m['content']}" for m in conv["history"][-10:])

    prompt = f"""You are an ontology engineer helping the user build an RDF/OWL ontology.

Current ontology state:
{ontology_state}

Conversation:
{history_text}

Based on the user's latest message, do ONE of:
1. If they describe a domain, propose classes and relationships
2. If they ask to add/modify/remove, update the ontology
3. If they ask to export, generate Turtle syntax

Respond with JSON:
{{"response": "your message to the user", "ontology": {{"classes": [{{"id": "snake_case", "label": "Human Name", "description": "...", "properties": ["prop1", "prop2"]}}], "properties": [{{"id": "snake_case", "label": "Human Name", "domain": "class_id", "range": "class_id_or_xsd:string"}}], "relationships": [{{"source": "class_id", "target": "class_id", "relation": "relation_name", "label": "Human Name"}}]}}, "ttl": "optional turtle syntax if user asked to export"}}

Return ONLY valid JSON."""

    try:
        from explorer.server import llm_manager
        raw = llm_manager.generate(prompt, system="You are an expert ontology engineer. Always respond with valid JSON.")
        # Parse
        raw = raw.strip()
        if raw.startswith("```"):
            raw = raw.split("\n", 1)[1] if "\n" in raw else raw[3:]
            if raw.endswith("```"):
                raw = raw[:-3]
        result = json.loads(raw.strip())
        # Update state
        if result.get("ontology"):
            conv["ontology"] = result["ontology"]
        if result.get("ttl"):
            conv["ttl"] = result["ttl"]
        conv["history"].append({"role": "assistant", "content": result.get("response", "")})

        # Save TTL to project file when project context is provided
        saved_to = None
        if project_id and active_file and conv["ttl"]:
            project_dir = Path("projects") / project_id
            project_dir.mkdir(parents=True, exist_ok=True)
            (project_dir / active_file).write_text(conv["ttl"], encoding="utf-8")
            saved_to = active_file

        return {
            "response": result.get("response", ""),
            "ontology": conv["ontology"],
            "ttl": result.get("ttl", ""),
            "session_id": session_id,
            "project_id": project_id,
            "active_file": active_file,
            "saved_to": saved_to,
        }
    except Exception as e:
        # Fallback — no LLM available
        fallback = f"LLM unavailable ({e}). You can still use the visual modeler or upload TTL directly."
        conv["history"].append({"role": "assistant", "content": fallback})
        return {
            "response": fallback,
            "ontology": conv["ontology"],
            "ttl": "",
            "session_id": session_id,
        }


@router.get("/conversation/{session_id}")
def get_conversation(session_id: str):
    """Get conversation state."""
    conv = conversations.get(session_id, {"history": [], "ontology": {"classes": [], "properties": [], "relationships": []}, "ttl": ""})
    return conv


@router.post("/canvas-to-ttl")
async def canvas_to_ttl(body: dict):
    """Convert visual modeler canvas state to TTL."""
    classes = body.get("classes", [])
    relationships = body.get("relationships", [])

    lines = [
        "@prefix owl: <http://www.w3.org/2002/07/owl#> .",
        "@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .",
        "@prefix kg: <http://kg.local/ontology#> .",
        "@prefix kgr: <http://kg.local/resource/> .",
        "@prefix skos: <http://www.w3.org/2004/02/skos/core#> .",
        "@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .",
        "",
    ]

    for cls in classes:
        cid = re.sub(r'[^a-z0-9_]', '_', cls.get("id", "").lower())[:60]
        label = cls.get("label", cid).replace('"', '\\"')
        desc = cls.get("description", "").replace('"', '\\"')
        lines.append(f'kg:{cid} a owl:Class ;')
        lines.append(f'    rdfs:label "{label}" ;')
        if desc:
            lines.append(f'    rdfs:comment "{desc}" ;')
        # Properties
        for prop in cls.get("properties", []):
            pid = re.sub(r'[^a-z0-9_]', '_', prop.lower())[:60]
            lines.append(f'    kg:{pid} xsd:string ;')
        lines[-1] = lines[-1].rstrip(" ;") + " ."
        lines.append("")

    for rel in relationships:
        sid = re.sub(r'[^a-z0-9_]', '_', rel.get("source", "").lower())[:60]
        tid = re.sub(r'[^a-z0-9_]', '_', rel.get("target", "").lower())[:60]
        rid = re.sub(r'[^a-z0-9_]', '_', rel.get("relation", "relates_to").lower())[:60]
        label = rel.get("label", rid).replace('"', '\\"')
        lines.append(f'kg:{rid} a owl:ObjectProperty ;')
        lines.append(f'    rdfs:label "{label}" ;')
        lines.append(f'    rdfs:domain kg:{sid} ;')
        lines.append(f'    rdfs:range kg:{tid} .')
        lines.append("")

    ttl = "\n".join(lines)
    # Validate
    try:
        g = RDFGraph()
        g.parse(data=ttl, format="turtle")
        return {"ttl": ttl, "valid": True, "triples": len(g)}
    except Exception as e:
        return {"ttl": ttl, "valid": False, "error": str(e)}


@router.post("/suggest")
async def suggest(body: dict):
    """AI suggest — given current canvas state, suggest next classes/relationships."""
    classes = body.get("classes", [])
    relationships = body.get("relationships", [])
    context = body.get("context", "")  # what user selected or typed

    class_names = [c.get("label", c.get("id", "")) for c in classes]
    rel_names = [f"{r.get('source','')} → {r.get('target','')}" for r in relationships]

    prompt = f"""Current ontology has these classes: {', '.join(class_names) if class_names else 'none yet'}
Relationships: {', '.join(rel_names) if rel_names else 'none yet'}
User context: {context or 'none'}

Suggest 3-5 new classes and relationships that would complement this ontology.
Return JSON: {{"suggestions": [{{"type": "class", "id": "snake_case", "label": "Name", "description": "why"}}, {{"type": "relationship", "source": "class_id", "target": "class_id", "relation": "rel_name", "label": "Name"}}]}}
Return ONLY valid JSON."""

    try:
        from explorer.server import llm_manager
        raw = llm_manager.generate(prompt, system="You suggest ontology additions. Return only valid JSON.")
        raw = raw.strip()
        if raw.startswith("```"):
            raw = raw.split("\n", 1)[1] if "\n" in raw else raw[3:]
            if raw.endswith("```"):
                raw = raw[:-3]
        result = json.loads(raw.strip())
        return result
    except Exception as e:
        return {"suggestions": [], "error": str(e)}
