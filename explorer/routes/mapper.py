"""
Mapper routes — map raw data (CSV/JSON) to ontology classes → generate RDF instances.
Like gra.fo but converts visual models to RDF automatically.
"""
import re
import json
import csv
import io
from pathlib import Path
from fastapi import APIRouter, UploadFile, File
from fastapi.responses import JSONResponse
from rdflib import Graph as RDFGraph, Namespace, Literal, URIRef, RDF, RDFS
from rdflib.namespace import XSD, SKOS

router = APIRouter(prefix="/api/mapper", tags=["mapper"])

KG = Namespace("http://kg.local/ontology#")
KGR = Namespace("http://kg.local/resource/")

# In-memory mapping sessions
mapping_sessions = {}


def make_id(text: str) -> str:
    return re.sub(r'[^a-z0-9_]', '_', text.lower().strip())[:80]


@router.post("/upload-data")
async def upload_data(file: UploadFile = File(...)):
    """Upload data file, return columns/fields + ALL rows for mapping."""
    content = await file.read()
    text = content.decode("utf-8", errors="ignore")
    filename = file.filename or "data"
    suffix = Path(filename).suffix.lower()

    if suffix == ".csv":
        reader = csv.DictReader(io.StringIO(text))
        headers = reader.fieldnames or []
        all_rows = [dict(row) for row in reader]
        sample = all_rows[:5]
        return {"type": "csv", "columns": headers, "sample": sample, "data": all_rows, "total_rows": len(all_rows), "filename": filename}

    elif suffix == ".json":
        data = json.loads(text)
        if isinstance(data, list) and data:
            sample = data[:5]
            columns = list(data[0].keys()) if data else []
            return {"type": "json_array", "columns": columns, "sample": sample, "data": data, "total_rows": len(data), "filename": filename}
        elif isinstance(data, dict):
            columns = list(data.keys())
            return {"type": "json_object", "columns": columns, "sample": [data], "data": [data], "total_rows": 1, "filename": filename}

    return JSONResponse({"error": f"Unsupported format: {suffix}. Use CSV or JSON."}, 400)


@router.post("/paste-data")
async def paste_data(body: dict):
    """Parse pasted CSV/JSON data."""
    text = body.get("text", "")
    if not text:
        return JSONResponse({"error": "No data"}, 400)
    # Try JSON first
    try:
        data = json.loads(text)
        if isinstance(data, list) and data:
            return {"type": "json_array", "columns": list(data[0].keys()), "sample": data[:5], "total_rows": len(data)}
        elif isinstance(data, dict):
            return {"type": "json_object", "columns": list(data.keys()), "sample": [data], "total_rows": 1}
    except:
        pass
    # Try CSV
    try:
        reader = csv.DictReader(io.StringIO(text))
        headers = reader.fieldnames or []
        rows = [dict(r) for i, r in enumerate(reader) if i < 5]
        if headers:
            return {"type": "csv", "columns": headers, "sample": rows, "total_rows": text.count("\n") - 1}
    except:
        pass
    return JSONResponse({"error": "Could not parse as CSV or JSON"}, 400)


@router.get("/ontology-classes")
def get_ontology_classes():
    """Return available ontology classes/properties for mapping targets."""
    # Read from current project or main graph
    classes = []
    props = []
    # Check ontologies dir
    ont_dir = Path("ontologies")
    ttl_files = list(ont_dir.glob("*.ttl")) if ont_dir.exists() else []
    ttl_files += list(Path("projects").glob("*/model.ttl"))
    main_ttl = Path("graphify-out/graph.ttl")
    if main_ttl.exists():
        ttl_files.append(main_ttl)

    seen_classes = set()
    seen_props = set()
    for ttl_path in ttl_files:
        try:
            g = RDFGraph()
            g.parse(str(ttl_path), format="turtle")
            from rdflib import OWL
            for s, _, _ in g.triples((None, RDF.type, OWL.Class)):
                cid = str(s).split("/")[-1].split("#")[-1]
                if cid not in seen_classes:
                    seen_classes.add(cid)
                    label = cid.replace("_", " ").title()
                    for _, _, o in g.triples((s, RDFS.label, None)):
                        label = str(o)
                    classes.append({"id": cid, "label": label, "uri": str(s), "source": ttl_path.name})
            for s, _, _ in g.triples((None, RDF.type, OWL.ObjectProperty)):
                pid = str(s).split("/")[-1].split("#")[-1]
                if pid not in seen_props:
                    seen_props.add(pid)
                    label = pid.replace("_", " ").title()
                    for _, _, o in g.triples((s, RDFS.label, None)):
                        label = str(o)
                    domain = ""
                    for _, _, o in g.triples((s, RDFS.domain, None)):
                        domain = str(o).split("/")[-1].split("#")[-1]
                    range_ = ""
                    for _, _, o in g.triples((s, RDFS.range, None)):
                        range_ = str(o).split("/")[-1].split("#")[-1]
                    props.append({"id": pid, "label": label, "domain": domain, "range": range_, "source": ttl_path.name})
        except:
            continue

    # Add built-in KG types
    builtins = ["Service", "Concept", "Process", "Decision", "Team", "Role", "BestPractice", "Document", "Component", "API", "Event"]
    for b in builtins:
        if b not in seen_classes:
            classes.append({"id": b, "label": b, "uri": f"http://kg.local/ontology#{b}", "source": "builtin"})

    return {"classes": classes, "properties": props}


@router.post("/generate-rdf")
async def generate_rdf(body: dict):
    """
    Generate RDF from data + mapping.
    mapping = {
        "class": "Service",
        "id_column": "name",
        "label_column": "name",
        "property_map": {"column_name": "ontology_property", ...},
        "relationship_map": {"column_name": {"predicate": "depends_on", "target_class": "Service"}, ...},
        "data": [...rows...]
    }
    """
    mapping = body
    target_class = mapping.get("class", "Concept")
    id_col = mapping.get("id_column", "")
    label_col = mapping.get("label_column", id_col)
    prop_map = mapping.get("property_map", {})
    rel_map = mapping.get("relationship_map", {})
    data = mapping.get("data", [])

    if not data:
        return JSONResponse({"error": "No data rows"}, 400)

    g = RDFGraph()
    g.bind("kg", KG)
    g.bind("kgr", KGR)
    g.bind("skos", SKOS)
    g.bind("rdfs", RDFS)
    g.bind("xsd", XSD)

    count = 0
    for row in data:
        # Generate ID
        raw_id = str(row.get(id_col, f"item_{count}"))
        eid = make_id(raw_id)
        if not eid:
            continue
        uri = KGR[eid]

        # Type
        g.add((uri, RDF.type, KG[target_class]))

        # Label
        label = str(row.get(label_col, raw_id))
        g.add((uri, SKOS.prefLabel, Literal(label)))

        # Mapped properties (datatype)
        for col, prop in prop_map.items():
            val = row.get(col, "")
            if val:
                g.add((uri, KG[make_id(prop)], Literal(str(val))))

        # Mapped relationships (object properties)
        for col, rel_info in rel_map.items():
            val = row.get(col, "")
            if val:
                predicate = rel_info.get("predicate", "relates_to")
                # Handle comma-separated values
                targets = [v.strip() for v in str(val).split(",")]
                for t in targets:
                    if t:
                        tid = make_id(t)
                        target_uri = KGR[tid]
                        g.add((uri, KG[make_id(predicate)], target_uri))
                        # Ensure target exists
                        target_class_name = rel_info.get("target_class", "Concept")
                        g.add((target_uri, RDF.type, KG[target_class_name]))
                        g.add((target_uri, SKOS.prefLabel, Literal(t)))

        count += 1

    ttl = g.serialize(format="turtle")
    return {"ttl": ttl, "triples": len(g), "instances": count}


@router.post("/auto-map")
async def auto_map(body: dict):
    """LLM-assisted auto-mapping: given columns + ontology classes, suggest mapping."""
    columns = body.get("columns", [])
    sample = body.get("sample", [])
    classes = body.get("classes", [])

    if not columns:
        return JSONResponse({"error": "No columns"}, 400)

    prompt = f"""Given these data columns: {json.dumps(columns)}
Sample data: {json.dumps(sample[:2])}
Available ontology classes: {json.dumps([c['id'] for c in classes[:20]])}

Suggest a mapping. Return JSON:
{{"class": "best_matching_class", "id_column": "column_for_id", "label_column": "column_for_label", "property_map": {{"column": "ontology_property"}}, "relationship_map": {{"column": {{"predicate": "relation_name", "target_class": "ClassName"}}}}}}
Only map columns that clearly fit. Return ONLY valid JSON."""

    try:
        from explorer.server import llm_manager
        raw = llm_manager.generate(prompt, system="You map data columns to ontology classes. Return only valid JSON.")
        raw = raw.strip()
        if raw.startswith("```"):
            raw = raw.split("\n", 1)[1] if "\n" in raw else raw[3:]
            if raw.endswith("```"):
                raw = raw[:-3]
        result = json.loads(raw.strip())
        return {"suggestion": result}
    except Exception as e:
        # Fallback: simple heuristic
        suggestion = {
            "class": "Concept",
            "id_column": columns[0] if columns else "",
            "label_column": columns[0] if columns else "",
            "property_map": {c: c for c in columns[1:4]},
            "relationship_map": {},
        }
        return {"suggestion": suggestion, "note": f"LLM unavailable ({e}), using heuristic"}
