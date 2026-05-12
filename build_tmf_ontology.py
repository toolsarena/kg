"""
Convert TMF SID JSON Schemas into RDF/TTL.
This IS the modeling — each schema becomes a class with properties and relationships.
"""
import json, re, os
from pathlib import Path

SID_DIR = Path("uploads/tmf_sid")
OUT = Path("uploads/tmf_sid_ontology.ttl")

lines = [
    "@prefix owl: <http://www.w3.org/2002/07/owl#> .",
    "@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .",
    "@prefix rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> .",
    "@prefix skos: <http://www.w3.org/2004/02/skos/core#> .",
    "@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .",
    "@prefix tmf: <http://kg.local/tmf/> .",
    "@prefix sid: <http://kg.local/sid/> .",
    "",
    "# =============================================",
    "# TMF SID Ontology — auto-generated from JSON Schemas",
    "# =============================================",
    "",
]

classes_seen = set()
relationships = []

def make_id(name):
    return re.sub(r'[^a-z0-9_]', '_', name.lower())[:80]

files = sorted(SID_DIR.glob("*.json"))
print(f"Processing {len(files)} schema files...")

for f in files:
    try:
        data = json.loads(f.read_text(encoding="utf-8"))
    except:
        continue

    defs = data.get("definitions", {})
    domain = f.name.split("__")[0] if "__" in f.name else "Common"

    for class_name, class_def in defs.items():
        cid = make_id(class_name)
        if cid in classes_seen:
            continue
        classes_seen.add(cid)

        desc = class_def.get("description", "").replace('"', "'").replace("\n", " ")[:200]
        lines.append(f'sid:{cid} a owl:Class ;')
        lines.append(f'    rdfs:label "{class_name}" ;')
        if desc:
            lines.append(f'    rdfs:comment "{desc}" ;')
        lines.append(f'    tmf:domain "{domain}" .')
        lines.append("")

        # Inheritance
        for item in class_def.get("allOf", []):
            if isinstance(item, dict) and "$ref" in item:
                parent = item["$ref"].split("#")[-1] if "#" in item["$ref"] else item["$ref"].split("/")[-1].replace(".schema.json", "")
                pid = make_id(parent)
                relationships.append((cid, "rdfs:subClassOf", pid))

        # Properties with $ref = relationships
        for prop_name, prop_def in class_def.get("properties", {}).items():
            if not isinstance(prop_def, dict):
                continue
            ref = prop_def.get("$ref", "")
            if not ref and isinstance(prop_def.get("items"), dict):
                ref = prop_def["items"].get("$ref", "")
            if ref:
                target = ref.split("#")[-1] if "#" in ref else ref.split("/")[-1].replace(".schema.json", "")
                tid = make_id(target)
                rel_id = make_id(prop_name)
                relationships.append((cid, f"sid:{rel_id}", tid))

# Add relationships
lines.append("")
lines.append("# =============================================")
lines.append("# Relationships")
lines.append("# =============================================")
lines.append("")

rel_seen = set()
for src, pred, tgt in relationships:
    if tgt not in classes_seen:
        # Add referenced class
        classes_seen.add(tgt)
        lines.append(f'sid:{tgt} a owl:Class ; rdfs:label "{tgt.replace("_", " ").title()}" .')
    key = (src, pred, tgt)
    if key not in rel_seen:
        rel_seen.add(key)
        lines.append(f'sid:{src} {pred} sid:{tgt} .')

ttl = "\n".join(lines)
OUT.write_text(ttl, encoding="utf-8")
print(f"\nDone!")
print(f"  Classes: {len(classes_seen)}")
print(f"  Relationships: {len(rel_seen)}")
print(f"  Output: {OUT}")
print(f"  Size: {len(ttl)} bytes")
print(f"\nLoad it in Studio: Ingest tab or Model tab > Upload TTL")
