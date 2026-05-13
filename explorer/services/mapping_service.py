"""Mapping Service — LLM-assisted and heuristic column-to-ontology mapping."""
import json
import re
from typing import Any

from rdflib import Graph as RDFGraph, RDF, RDFS, OWL, Namespace, URIRef
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
    """Parse a TTL string and extract all classes and properties.
    
    Recognizes owl:Class, rdfs:Class, and any custom types used as classes
    (anything that has instances via rdf:type).
    """
    g = RDFGraph()
    g.parse(data=ttl_content, format="turtle")

    classes = []
    object_properties = []
    datatype_properties = []
    seen_class_uris = set()

    # Extract OWL classes
    for s in g.subjects(RDF.type, OWL.Class):
        uri = str(s)
        if uri in seen_class_uris:
            continue
        seen_class_uris.add(uri)
        local_name = uri.split("#")[-1] if "#" in uri else uri.split("/")[-1]
        label = local_name.replace("_", " ").title()
        for _, _, o in g.triples((s, RDFS.label, None)):
            label = str(o)
        classes.append(OntologyClass(uri=uri, label=label, local_name=local_name))

    # Extract RDFS classes
    for s in g.subjects(RDF.type, RDFS.Class):
        uri = str(s)
        if uri in seen_class_uris:
            continue
        seen_class_uris.add(uri)
        local_name = uri.split("#")[-1] if "#" in uri else uri.split("/")[-1]
        label = local_name.replace("_", " ").title()
        for _, _, o in g.triples((s, RDFS.label, None)):
            label = str(o)
        classes.append(OntologyClass(uri=uri, label=label, local_name=local_name))

    # If no OWL/RDFS classes found, look for any URI used as rdf:type object
    # (e.g., kg:Concept, kg:Service — custom types)
    if not classes:
        type_uris = set()
        for _, _, o in g.triples((None, RDF.type, None)):
            uri = str(o)
            # Skip well-known vocabulary types
            if any(uri.startswith(ns) for ns in [
                'http://www.w3.org/2002/07/owl#',
                'http://www.w3.org/2000/01/rdf-schema#',
                'http://www.w3.org/1999/02/22-rdf-syntax-ns#',
            ]):
                continue
            type_uris.add(uri)
        for uri in type_uris:
            if uri in seen_class_uris:
                continue
            seen_class_uris.add(uri)
            local_name = uri.split("#")[-1] if "#" in uri else uri.split("/")[-1]
            label = local_name.replace("_", " ").title()
            # Try to find a label
            uri_ref = URIRef(uri) if not isinstance(uri, URIRef) else uri
            for _, _, o in g.triples((uri_ref, RDFS.label, None)):
                label = str(o)
            from rdflib.namespace import SKOS as _SKOS
            for _, _, o in g.triples((uri_ref, _SKOS.prefLabel, None)):
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

    # If no formal properties found, extract predicates used in the graph as properties
    if not object_properties and not datatype_properties:
        skip_preds = {
            str(RDF.type), str(RDFS.label), str(RDFS.comment),
            'http://www.w3.org/2004/02/skos/core#prefLabel',
            'http://www.w3.org/2000/01/rdf-schema#subClassOf',
        }
        pred_uris = set()
        for _, p, o in g:
            uri = str(p)
            if uri in skip_preds:
                continue
            pred_uris.add((uri, hasattr(o, 'n3') and str(o).startswith('http')))

        for uri, is_object in pred_uris:
            local_name = uri.split("#")[-1] if "#" in uri else uri.split("/")[-1]
            label = local_name.replace("_", " ").title()
            prop = OntologyProperty(uri=uri, label=label, local_name=local_name)
            if is_object:
                object_properties.append(prop)
            else:
                datatype_properties.append(prop)

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

IMPORTANT: Map ALL columns to properties. If no exact ontology property exists for a column, create a new datatype property URI using the ontology namespace and a camelCase version of the column name. Do NOT leave columns as "unmapped" — every column should be mapped as either "datatype" or "object".

Return a JSON object with:
- "target_class": the ontology class URI that best represents each data row
- "id_column": the column that uniquely identifies each row (prefer columns with "id", "key", "code", or unique values)
- "label_column": the column best used as a human-readable label (prefer "name", "title", "label" columns)
- "column_mappings": array of objects, one per column, each with:
  - "column_name": the column name
  - "mapped_property": the ontology property URI (create one if needed using the ontology namespace)
  - "mapping_type": "datatype" for literal values, "object" for references to other entities
  - "confidence": float 0.0-1.0 (1.0 for exact matches, 0.5+ for reasonable mappings)
  - "target_class": for object properties, the target class URI (or null for datatype)

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
    """Generate a mapping suggestion using string similarity (fallback).
    
    When no good matches are found, maps all columns as datatype properties
    to the target class — better than leaving everything unmapped.
    """
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
        if any(kw in col_lower for kw in ("id", "identifier", "key", "code", "number", "frn")):
            if not id_column:
                id_column = col
        if any(kw in col_lower for kw in ("name", "label", "title", "dba")):
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
            # No good match found — leave as unmapped, user will assign manually
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
    """Validate that mapped properties belong to the domain of the target class.
    
    Only validates properties that exist in the ontology. Properties not found
    are treated as new extensions (user is extending the ontology with data).
    """
    errors = []
    warnings = []

    # Build lookup maps
    class_uris = {c.uri for c in ontology.classes}
    prop_map: dict[str, OntologyProperty] = {}
    for p in ontology.datatype_properties + ontology.object_properties:
        prop_map[p.uri] = p

    # Check target class exists (warning, not error)
    if mapping.target_class and mapping.target_class not in class_uris:
        warnings.append(f"Target class '{mapping.target_class}' not found in ontology — will be created")

    # Check each column mapping
    for cm in mapping.column_mappings:
        if cm.mapping_type in ("skip", "unmapped") or not cm.mapped_property:
            continue

        # If property exists in ontology, check domain constraint
        if cm.mapped_property in prop_map:
            prop = prop_map[cm.mapped_property]
            if prop.domain and mapping.target_class:
                if prop.domain != mapping.target_class:
                    warnings.append(
                        f"Property '{prop.local_name}' has domain '{prop.domain}', "
                        f"target class is '{mapping.target_class}'"
                    )
        # If property doesn't exist, that's fine — it will be created as a new property

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
