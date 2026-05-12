"""Mapping Service — LLM-assisted and heuristic column-to-ontology mapping."""
import json
import re
from typing import Any

from rdflib import Graph as RDFGraph, RDF, RDFS, OWL, Namespace
from rdflib.namespace import XSD

from explorer.services.models import (
    ColumnMapping,
    ConfirmedMapping,
    MappingSuggestion,
    OntologyClass,
    OntologyProperty,
    OntologySchema,
    ValidationResult,
)


def extract_ontology_schema(ttl_content: str) -> OntologySchema:
    """Parse a TTL string and extract all OWL classes and properties."""
    g = RDFGraph()
    g.parse(data=ttl_content, format="turtle")

    classes = []
    object_properties = []
    datatype_properties = []

    # Extract OWL classes
    for s in g.subjects(RDF.type, OWL.Class):
        uri = str(s)
        local_name = uri.split("#")[-1] if "#" in uri else uri.split("/")[-1]
        label = local_name.replace("_", " ").title()
        for _, _, o in g.triples((s, RDFS.label, None)):
            label = str(o)
        classes.append(OntologyClass(uri=uri, label=label, local_name=local_name))

    # Extract object properties
    for s in g.subjects(RDF.type, OWL.ObjectProperty):
        uri = str(s)
        local_name = uri.split("#")[-1] if "#" in uri else uri.split("/")[-1]
        label = local_name.replace("_", " ").title()
        domain = None
        range_ = None
        for _, _, o in g.triples((s, RDFS.label, None)):
            label = str(o)
        for _, _, o in g.triples((s, RDFS.domain, None)):
            domain = str(o)
        for _, _, o in g.triples((s, RDFS.range, None)):
            range_ = str(o)
        object_properties.append(OntologyProperty(
            uri=uri, label=label, local_name=local_name,
            domain=domain, range=range_,
        ))

    # Extract datatype properties
    for s in g.subjects(RDF.type, OWL.DatatypeProperty):
        uri = str(s)
        local_name = uri.split("#")[-1] if "#" in uri else uri.split("/")[-1]
        label = local_name.replace("_", " ").title()
        domain = None
        range_ = None
        for _, _, o in g.triples((s, RDFS.label, None)):
            label = str(o)
        for _, _, o in g.triples((s, RDFS.domain, None)):
            domain = str(o)
        for _, _, o in g.triples((s, RDFS.range, None)):
            range_ = str(o)
        datatype_properties.append(OntologyProperty(
            uri=uri, label=label, local_name=local_name,
            domain=domain, range=range_,
        ))

    return OntologySchema(
        classes=classes,
        object_properties=object_properties,
        datatype_properties=datatype_properties,
    )


def suggest_mapping(
    columns: list[dict],
    sample: list[dict],
    ontology: OntologySchema,
    llm_manager: Any,
) -> MappingSuggestion:
    """Generate an LLM-assisted mapping suggestion.

    Falls back to heuristic_mapping if LLM is unavailable or returns invalid JSON.
    """
    # Build prompt context
    class_info = [{"uri": c.uri, "label": c.label, "local_name": c.local_name} for c in ontology.classes]
    prop_info = []
    for p in ontology.datatype_properties + ontology.object_properties:
        prop_info.append({
            "uri": p.uri, "label": p.label, "local_name": p.local_name,
            "domain": p.domain, "range": p.range,
            "type": "datatype" if p in ontology.datatype_properties else "object",
        })

    col_names = [c["name"] if isinstance(c, dict) else c.name for c in columns]

    prompt = f"""You are mapping dataset columns to an ontology. Given:

Dataset columns: {json.dumps(col_names)}
Sample data (first 3 rows): {json.dumps(sample[:3], default=str)}

Ontology classes: {json.dumps(class_info)}
Ontology properties: {json.dumps(prop_info)}

Return a JSON object with:
- "target_class": the ontology class URI that best represents each data row
- "id_column": the column that uniquely identifies each row
- "label_column": the column best used as a human-readable label
- "column_mappings": array of objects, one per column, each with:
  - "column_name": the column name
  - "mapped_property": the ontology property URI (or null if unmapped)
  - "mapping_type": "datatype", "object", "skip", or "unmapped"
  - "confidence": float 0.0-1.0
  - "target_class": for object properties, the target class URI (or null)

Return ONLY valid JSON, no explanation."""

    try:
        result = llm_manager.generate_json(
            prompt,
            system="You map dataset columns to ontology classes and properties. Return only valid JSON."
        )

        # Parse LLM response
        target_class = result.get("target_class", "")
        id_column = result.get("id_column", col_names[0] if col_names else "")
        label_column = result.get("label_column", id_column)

        mappings = []
        raw_mappings = result.get("column_mappings", [])
        mapped_cols = set()

        for rm in raw_mappings:
            col_name = rm.get("column_name", "")
            if col_name:
                mapped_cols.add(col_name)
            confidence = rm.get("confidence", 0.5)
            confidence = max(0.0, min(1.0, float(confidence)))
            mappings.append(ColumnMapping(
                column_name=col_name,
                mapped_property=rm.get("mapped_property"),
                mapping_type=rm.get("mapping_type", "unmapped"),
                confidence=confidence,
                target_class=rm.get("target_class"),
            ))

        # Ensure all columns are represented
        for col in col_names:
            if col not in mapped_cols:
                mappings.append(ColumnMapping(
                    column_name=col,
                    mapped_property=None,
                    mapping_type="unmapped",
                    confidence=0.0,
                ))

        return MappingSuggestion(
            target_class=target_class,
            id_column=id_column,
            label_column=label_column,
            column_mappings=mappings,
        )

    except Exception:
        # Fallback to heuristic mapping
        return heuristic_mapping(columns, ontology)


def heuristic_mapping(
    columns: list[Any],
    ontology: OntologySchema,
) -> MappingSuggestion:
    """Generate a mapping suggestion using string similarity (fallback)."""
    col_names = [c["name"] if isinstance(c, dict) else (c.name if hasattr(c, "name") else str(c)) for c in columns]

    # Determine target class (first class or empty)
    target_class = ontology.classes[0].uri if ontology.classes else ""

    # All properties for matching
    all_props = ontology.datatype_properties + ontology.object_properties

    # Find id and label columns heuristically
    id_column = ""
    label_column = ""
    for col in col_names:
        col_lower = col.lower()
        if any(kw in col_lower for kw in ("id", "identifier", "key", "code")):
            if not id_column:
                id_column = col
        if any(kw in col_lower for kw in ("name", "label", "title")):
            if not label_column:
                label_column = col

    if not id_column and col_names:
        id_column = col_names[0]
    if not label_column:
        label_column = id_column

    # Map each column
    mappings = []
    for col in col_names:
        best_prop = None
        best_score = 0.0
        best_type = "unmapped"

        for prop in all_props:
            score = compute_similarity(col, prop.local_name)
            label_score = compute_similarity(col, prop.label)
            score = max(score, label_score)

            if score > best_score:
                best_score = score
                best_prop = prop

        if best_prop and best_score >= 0.3:
            is_object = best_prop in ontology.object_properties
            best_type = "object" if is_object else "datatype"
            target_cls = best_prop.range if is_object else None
            mappings.append(ColumnMapping(
                column_name=col,
                mapped_property=best_prop.uri,
                mapping_type=best_type,
                confidence=best_score,
                target_class=target_cls,
            ))
        else:
            mappings.append(ColumnMapping(
                column_name=col,
                mapped_property=None,
                mapping_type="unmapped",
                confidence=0.0,
            ))

    return MappingSuggestion(
        target_class=target_class,
        id_column=id_column,
        label_column=label_column,
        column_mappings=mappings,
    )


def validate_mapping(mapping: ConfirmedMapping, ontology: OntologySchema) -> dict:
    """Validate that mapped properties belong to the domain of the target class."""
    errors = []
    warnings = []

    # Build lookup maps
    class_uris = {c.uri for c in ontology.classes}
    prop_map: dict[str, OntologyProperty] = {}
    for p in ontology.datatype_properties + ontology.object_properties:
        prop_map[p.uri] = p

    # Check target class exists
    if mapping.target_class and mapping.target_class not in class_uris:
        errors.append(f"Target class '{mapping.target_class}' not found in ontology")

    # Check each column mapping
    for cm in mapping.column_mappings:
        if cm.mapping_type in ("skip", "unmapped") or not cm.mapped_property:
            continue

        if cm.mapped_property not in prop_map:
            errors.append(f"Property '{cm.mapped_property}' not found in ontology")
            continue

        prop = prop_map[cm.mapped_property]
        # Check domain constraint
        if prop.domain and mapping.target_class:
            if prop.domain != mapping.target_class:
                errors.append(
                    f"Property '{prop.local_name}' has domain '{prop.domain}', "
                    f"incompatible with class '{mapping.target_class}'"
                )

    valid = len(errors) == 0
    return {"valid": valid, "errors": errors, "warnings": warnings}


def compute_similarity(a: str, b: str) -> float:
    """Compute normalized token overlap similarity between two strings."""
    if not a or not b:
        return 0.0

    # Normalize: lowercase, split on non-alphanumeric
    tokens_a = set(re.split(r'[^a-z0-9]+', a.lower()))
    tokens_b = set(re.split(r'[^a-z0-9]+', b.lower()))

    # Remove empty tokens
    tokens_a.discard("")
    tokens_b.discard("")

    if not tokens_a or not tokens_b:
        return 0.0

    # Exact case-insensitive match
    if a.lower().strip() == b.lower().strip():
        return 1.0

    # Token overlap (Jaccard-like)
    intersection = tokens_a & tokens_b
    union = tokens_a | tokens_b

    if not union:
        return 0.0

    return len(intersection) / len(union)
