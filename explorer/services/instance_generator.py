"""Instance Generator — transforms data rows into RDF triples based on confirmed mappings."""
import re
from typing import Any

from rdflib import Graph as RDFGraph, Namespace, Literal, URIRef, RDF, RDFS, BNode
from rdflib.namespace import XSD, SKOS

from explorer.services.models import (
    ColumnMapping,
    ConfirmedMapping,
    GenerationResult,
    MergeResult,
)


def _make_safe_uri_part(value: str) -> str:
    """Convert a value into a safe URI fragment."""
    # Replace non-alphanumeric with underscore, collapse multiples
    safe = re.sub(r'[^a-zA-Z0-9_-]', '_', str(value).strip())
    safe = re.sub(r'_+', '_', safe).strip('_')
    return safe[:200] if safe else "unnamed"


def _xsd_type_for(inferred_type: str) -> URIRef | None:
    """Map inferred type string to XSD datatype URI."""
    type_map = {
        "integer": XSD.integer,
        "float": XSD.float,
        "boolean": XSD.boolean,
        "date": XSD.date,
        "uri": XSD.anyURI,
        "string": XSD.string,
    }
    return type_map.get(inferred_type, XSD.string)


def generate(
    data: list[dict],
    mapping: ConfirmedMapping,
    base_uri: str,
    existing_graph: RDFGraph | None = None,
) -> GenerationResult:
    """Generate RDF individuals from data rows based on a confirmed mapping.

    Args:
        data: List of row dicts from the dataset.
        mapping: The confirmed column-to-ontology mapping.
        base_uri: Base URI for generating instance URIs (e.g. "http://kg.local/resource/").
        existing_graph: Optional existing graph for incremental loading.

    Returns:
        GenerationResult with TTL content and statistics.
    """
    if not data:
        raise ValueError("No data rows to process")

    g = RDFGraph()
    ns = Namespace(base_uri if base_uri.endswith("/") or base_uri.endswith("#") else base_uri + "/")
    g.bind("inst", ns)

    target_class_uri = URIRef(mapping.target_class) if mapping.target_class else None

    # Build mapping lookup
    col_map: dict[str, ColumnMapping] = {}
    for cm in mapping.column_mappings:
        col_map[cm.column_name] = cm

    instances_created = 0
    instances_updated = 0
    triples_generated = 0
    rows_skipped = 0
    skipped_reasons: list[str] = []

    # Track existing instance URIs for incremental loading
    existing_uris: set[str] = set()
    if existing_graph:
        for s in existing_graph.subjects(RDF.type, None):
            existing_uris.add(str(s))
        # Copy existing triples into new graph
        for triple in existing_graph:
            g.add(triple)

    for i, row in enumerate(data):
        # Get identifier value
        id_value = row.get(mapping.id_column, "")
        if not id_value or (isinstance(id_value, str) and not id_value.strip()):
            rows_skipped += 1
            skipped_reasons.append(f"Row {i+1}: missing identifier in column '{mapping.id_column}'")
            continue

        # Build instance URI
        uri_part = _make_safe_uri_part(str(id_value))
        instance_uri = ns[uri_part]

        # Check if this is an update to an existing instance
        if str(instance_uri) in existing_uris:
            instances_updated += 1
        else:
            instances_created += 1

        # Add type triple
        if target_class_uri:
            g.add((instance_uri, RDF.type, target_class_uri))
            triples_generated += 1

        # Add label if label column is mapped
        label_value = row.get(mapping.label_column, "")
        if label_value and str(label_value).strip():
            g.add((instance_uri, RDFS.label, Literal(str(label_value).strip())))
            triples_generated += 1

        # Process each column mapping
        for cm in mapping.column_mappings:
            if cm.mapping_type in ("skip", "unmapped") or not cm.mapped_property:
                continue

            cell_value = row.get(cm.column_name, "")
            if cell_value is None or (isinstance(cell_value, str) and not cell_value.strip()):
                continue  # Skip empty cells

            prop_uri = URIRef(cm.mapped_property)

            if cm.mapping_type == "datatype":
                # Create typed literal
                literal = _create_typed_literal(str(cell_value))
                g.add((instance_uri, prop_uri, literal))
                triples_generated += 1

            elif cm.mapping_type == "object":
                # Create object property linking to another resource
                target_uri_part = _make_safe_uri_part(str(cell_value))
                target_uri = ns[target_uri_part]
                g.add((instance_uri, prop_uri, target_uri))
                triples_generated += 1

                # Ensure target resource has a type if target_class is specified
                if cm.target_class:
                    g.add((target_uri, RDF.type, URIRef(cm.target_class)))
                    g.add((target_uri, RDFS.label, Literal(str(cell_value).strip())))

    # Check if all rows were skipped
    if instances_created == 0 and instances_updated == 0:
        raise ValueError(f"All rows are missing values in identifier column '{mapping.id_column}'")

    ttl = g.serialize(format="turtle")

    return GenerationResult(
        ttl=ttl,
        instances_created=instances_created,
        instances_updated=instances_updated,
        triples_generated=triples_generated,
        rows_skipped=rows_skipped,
        skipped_reasons=skipped_reasons,
    )


def _create_typed_literal(value: str) -> Literal:
    """Create an appropriately typed RDF literal from a string value."""
    value = value.strip()

    # Try integer
    try:
        int_val = int(value)
        return Literal(int_val, datatype=XSD.integer)
    except (ValueError, TypeError):
        pass

    # Try float
    try:
        float_val = float(value)
        return Literal(float_val, datatype=XSD.float)
    except (ValueError, TypeError):
        pass

    # Try boolean
    if value.lower() in ("true", "false"):
        return Literal(value.lower() == "true", datatype=XSD.boolean)

    # Try date
    if re.match(r'^\d{4}-\d{2}-\d{2}', value):
        return Literal(value, datatype=XSD.date)

    # Default to string
    return Literal(value, datatype=XSD.string)


def merge_instances(existing: RDFGraph, new: RDFGraph) -> dict:
    """Merge new triples into an existing graph, preserving existing data.

    When a new triple has the same subject as an existing instance,
    the new triples are added (merged) rather than creating duplicates.

    Returns:
        Dict with new_instances, updated_instances, triples_added counts.
    """
    # Get existing instance URIs (subjects with rdf:type)
    existing_subjects = set()
    for s in existing.subjects(RDF.type, None):
        existing_subjects.add(str(s))

    new_subjects = set()
    for s in new.subjects(RDF.type, None):
        new_subjects.add(str(s))

    new_instances = 0
    updated_instances = 0
    triples_added = 0

    # Count new vs updated
    for subj in new_subjects:
        if subj in existing_subjects:
            updated_instances += 1
        else:
            new_instances += 1

    # Add all new triples to existing graph
    for s, p, o in new:
        if (s, p, o) not in existing:
            existing.add((s, p, o))
            triples_added += 1

    return {
        "new_instances": new_instances,
        "updated_instances": updated_instances,
        "triples_added": triples_added,
    }
