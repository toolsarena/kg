"""
Ingest routes — upload files, extract entities, preview before committing to graph.
"""
import re
import time
import tempfile
from pathlib import Path
from fastapi import APIRouter, UploadFile, File, Form
from fastapi.responses import JSONResponse

router = APIRouter(prefix="/api/ingest", tags=["ingest"])

UPLOAD_DIR = Path("uploads")
UPLOAD_DIR.mkdir(exist_ok=True)


def extract_from_json_schema(data: dict, source: str = "") -> dict:
    """Extract entities and relationships from JSON Schema (TMF SID style)."""
    entities = []
    relationships = []
    definitions = data.get("definitions", {})
    title = data.get("title", source)

    for class_name, class_def in definitions.items():
        cid = re.sub(r'[^a-z0-9_]', '_', class_name.lower())[:60]
        desc = class_def.get("description", "")
        props = []
        
        for prop_name, prop_def in class_def.get("properties", {}).items():
            if isinstance(prop_def, dict):
                # Check if it's a $ref (relationship to another class)
                ref = prop_def.get("$ref", "")
                if not ref and prop_def.get("items"):
                    ref = prop_def["items"].get("$ref", "") if isinstance(prop_def["items"], dict) else ""
                
                if ref:
                    # Extract target class from $ref path
                    # e.g. "../EngagedParty/RelatedParty.schema.json#RelatedParty" -> "RelatedParty"
                    target = ref.split("#")[-1] if "#" in ref else ref.split("/")[-1].replace(".schema.json", "")
                    tid = re.sub(r'[^a-z0-9_]', '_', target.lower())[:60]
                    is_array = prop_def.get("type") == "array"
                    relationships.append({
                        "source": cid,
                        "target": tid,
                        "relation": prop_name,
                        "label": prop_name,
                        "is_array": is_array,
                        "description": prop_def.get("description", ""),
                    })
                else:
                    # Simple property
                    ptype = prop_def.get("type", "string")
                    props.append({
                        "name": prop_name,
                        "type": ptype,
                        "description": prop_def.get("description", ""),
                    })

        # Check inheritance via allOf
        parent = None
        for item in class_def.get("allOf", []):
            if isinstance(item, dict) and "$ref" in item:
                parent_ref = item["$ref"]
                parent = parent_ref.split("#")[-1] if "#" in parent_ref else parent_ref.split("/")[-1].replace(".schema.json", "")

        entities.append({
            "id": cid,
            "label": class_name,
            "type": "concept",
            "source": "json_schema",
            "description": desc[:200] if desc else "",
            "properties": props,
            "parent": parent,
            "relationships": [{"target": r["target"], "relation": r["relation"]} for r in relationships if r["source"] == cid],
        })

    # Also add referenced classes that aren't defined here
    defined_ids = {e["id"] for e in entities}
    for rel in relationships:
        if rel["target"] not in defined_ids:
            entities.append({
                "id": rel["target"],
                "label": rel["target"].replace("_", " ").title(),
                "type": "concept",
                "source": "json_schema_ref",
                "description": f"Referenced from {title}",
                "properties": [],
                "relationships": [],
            })
            defined_ids.add(rel["target"])

    return {
        "title": title,
        "source": source,
        "file_type": "json_schema",
        "entities": entities,
        "relationships": relationships,
        "class_count": len(definitions),
        "relationship_count": len(relationships),
    }


def extract_from_text(text: str, source: str = "") -> dict:
    """Extract entities and relationships from raw text using pattern matching."""
    lines = text.split("\n")
    title = ""
    for line in lines:
        stripped = line.strip().lstrip("#").strip()
        if stripped and len(stripped) > 3:
            title = stripped[:120]
            break

    # Find headings as potential entities
    entities = []
    seen = set()
    for line in lines:
        s = line.strip()
        if s.startswith("#"):
            name = s.lstrip("#").strip()
            if name and len(name) > 2 and name.lower() not in seen:
                seen.add(name.lower())
                nid = re.sub(r'[^a-z0-9_]', '_', name.lower())[:60]
                entities.append({"id": nid, "label": name, "type": "concept", "source": "heading"})

    # Find AWS services mentioned
    aws_pattern = r'(Amazon|AWS)\s+[A-Z][A-Za-z0-9 ]+(?:Service|Manager|Hub|Guard|Inspector|Trail|Watch|Bridge|Config|Lambda|Gateway|Firewall|Shield|WAF|Batch|Glue|Athena|Redshift|Aurora|Neptune|Kinesis|SQS|SNS|S3|EC2|ECS|EKS|RDS|VPC|IAM|KMS|CDK)'
    for match in re.finditer(aws_pattern, text):
        name = match.group(0).strip()
        if name.lower() not in seen:
            seen.add(name.lower())
            nid = re.sub(r'[^a-z0-9_]', '_', name.lower())[:60]
            entities.append({"id": nid, "label": name, "type": "service", "source": "pattern"})

    # Find capitalized multi-word terms as concepts
    cap_pattern = r'\b([A-Z][a-z]+(?:\s+[A-Z][a-z]+)+)\b'
    for match in re.finditer(cap_pattern, text):
        name = match.group(0).strip()
        if len(name) > 5 and name.lower() not in seen and len(name.split()) <= 5:
            seen.add(name.lower())
            nid = re.sub(r'[^a-z0-9_]', '_', name.lower())[:60]
            entities.append({"id": nid, "label": name, "type": "concept", "source": "pattern"})

    return {
        "title": title,
        "source": source,
        "text_length": len(text),
        "entities": entities[:100],
        "raw_text": text[:2000],
    }


def extract_from_csv(text: str, source: str = "") -> dict:
    """Extract entities from CSV — each row becomes a potential entity."""
    import csv
    import io
    reader = csv.DictReader(io.StringIO(text))
    entities = []
    headers = reader.fieldnames or []
    for i, row in enumerate(reader):
        if i >= 200:
            break
        # Use first column as label
        label = str(list(row.values())[0]) if row else f"row_{i}"
        nid = re.sub(r'[^a-z0-9_]', '_', label.lower())[:60]
        entities.append({
            "id": nid,
            "label": label,
            "type": "concept",
            "source": "csv_row",
            "attributes": {k: v for k, v in row.items() if v},
        })
    return {
        "title": source,
        "source": source,
        "headers": headers,
        "entities": entities,
        "row_count": i + 1 if entities else 0,
    }


@router.post("/upload")
async def upload_file(file: UploadFile = File(...)):
    """Upload a file, extract entities, return preview."""
    content = await file.read()
    filename = file.filename or "unknown"
    suffix = Path(filename).suffix.lower()

    # Save to uploads
    save_path = UPLOAD_DIR / filename
    save_path.write_bytes(content)

    try:
        if suffix == ".pdf":
            import pdfplumber
            text = ""
            with pdfplumber.open(save_path) as pdf:
                for page in pdf.pages[:50]:
                    text += (page.extract_text() or "") + "\n"
            result = extract_from_text(text, filename)
            result["file_type"] = "pdf"
            result["pages"] = len(pdfplumber.open(save_path).pages)

        elif suffix == ".csv":
            text = content.decode("utf-8", errors="ignore")
            result = extract_from_csv(text, filename)
            result["file_type"] = "csv"

        elif suffix in (".json", ".jsonld"):
            import json as jsonmod
            data = jsonmod.loads(content)
            # Check if it's a JSON Schema (TMF SID style)
            if "definitions" in data or "$schema" in data:
                result = extract_from_json_schema(data, filename)
            else:
                text = jsonmod.dumps(data, indent=2)
                result = extract_from_text(text, filename)
            result["file_type"] = "json_schema" if "definitions" in (data if isinstance(data, dict) else {}) else "json"

        elif suffix in (".ttl", ".owl", ".rdf"):
            # Ontology file — validate and return stats
            from rdflib import Graph as RG
            rg = RG()
            fmt = "turtle" if suffix == ".ttl" else "xml"
            rg.parse(data=content.decode("utf-8"), format=fmt)
            result = {
                "title": filename,
                "source": filename,
                "file_type": "ontology",
                "format": fmt,
                "triples": len(rg),
                "entities": [],
                "valid": True,
                "raw_text": content.decode("utf-8")[:3000],
            }

        else:
            # Treat as text
            text = content.decode("utf-8", errors="ignore")
            result = extract_from_text(text, filename)
            result["file_type"] = "text"

        return result

    except Exception as e:
        return JSONResponse({"error": str(e), "filename": filename}, 400)


@router.post("/text")
async def ingest_text(body: dict):
    """Extract entities from pasted text."""
    text = body.get("text", "")
    if not text:
        return JSONResponse({"error": "No text provided"}, 400)
    return extract_from_text(text, "pasted_text")


@router.post("/commit")
async def commit_entities(body: dict):
    """Commit selected entities to the graph as TTL.

    When project_id is provided, saves the generated TTL into the project directory.
    If filename is not provided, auto-generates one using a timestamp.
    """
    entities = body.get("entities", [])
    if not entities:
        return JSONResponse({"error": "No entities"}, 400)

    project_id = body.get("project_id")
    filename = body.get("filename")

    lines = [
        "@prefix kg: <http://kg.local/ontology#> .",
        "@prefix kgr: <http://kg.local/resource/> .",
        "@prefix skos: <http://www.w3.org/2004/02/skos/core#> .",
        "@prefix rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> .",
        "@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .",
        "",
    ]

    type_map = {
        "concept": "kg:Concept", "service": "kg:Service", "process": "kg:Process",
        "decision": "kg:Decision", "team": "kg:Team", "role": "kg:Role",
        "best_practice": "kg:BestPractice", "document": "kg:Document",
    }

    for e in entities:
        eid = re.sub(r'[^a-z0-9_]', '_', e.get("id", "").lower())[:80]
        if not eid:
            continue
        etype = type_map.get(e.get("type", "concept"), "kg:Concept")
        label = e.get("label", eid).replace('"', '\\"')
        desc = e.get("description", "").replace('"', '\\"').replace("\n", " ")[:200]
        lines.append(f'kgr:{eid} a {etype} ; skos:prefLabel "{label}" .')
        if desc:
            lines.append(f'kgr:{eid} rdfs:comment "{desc}" .')
        # Inheritance
        if e.get("parent"):
            pid = re.sub(r'[^a-z0-9_]', '_', e["parent"].lower())[:80]
            lines.append(f'kgr:{eid} rdfs:subClassOf kgr:{pid} .')

    # Add relationships
    for e in entities:
        eid = re.sub(r'[^a-z0-9_]', '_', e.get("id", "").lower())[:80]
        for rel in e.get("relationships", []):
            tid = re.sub(r'[^a-z0-9_]', '_', rel.get("target", "").lower())[:80]
            rtype = re.sub(r'[^a-z0-9_]', '_', rel.get("relation", "relates_to").lower())[:60]
            if eid and tid:
                lines.append(f'kgr:{eid} kg:{rtype} kgr:{tid} .')

    ttl = "\n".join(lines)

    # Save to project if project_id is provided
    if project_id:
        project_dir = Path("projects") / project_id
        project_dir.mkdir(parents=True, exist_ok=True)
        if not filename:
            filename = f"ingest_{int(time.time())}.ttl"
        (project_dir / filename).write_text(ttl, encoding="utf-8")
        return {
            "ttl": ttl,
            "entity_count": len(entities),
            "saved_to": filename,
            "project_id": project_id,
        }

    return {"ttl": ttl, "entity_count": len(entities)}
