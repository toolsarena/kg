"""
Population routes — session-based data population workflow.
Upload datasets, map columns to ontology, generate RDF instances, export/push.
"""
import json
import time
import uuid
from pathlib import Path

from fastapi import APIRouter, UploadFile, File
from fastapi.responses import JSONResponse, Response
from rdflib import Graph as RDFGraph

from explorer.services.models import (
    ColumnMapping,
    ConfirmedMapping,
    PopulationSession,
)
from explorer.services.dataset_connector import DatasetConnector
from explorer.services import mapping_service
from explorer.services import instance_generator
from explorer.services import export_service

router = APIRouter(prefix="/api/population", tags=["population"])

PROJECTS_DIR = Path("projects")

# In-memory population sessions
_sessions: dict[str, PopulationSession] = {}

# Shared dataset connector instance
_connector = DatasetConnector()


def _get_or_create_session(project_id: str) -> PopulationSession:
    """Get existing session for project or create a new one."""
    for sid, session in _sessions.items():
        if session.project_id == project_id:
            return session
    session = PopulationSession(project_id=project_id)
    _sessions[session.session_id] = session
    return session


# --- Dataset Upload & Connection ---


@router.post("/upload-dataset")
async def upload_dataset(file: UploadFile = File(...)):
    """Upload a CSV, JSON, or XML file and return a parsed preview."""
    if not file.filename:
        return JSONResponse({"error": "No file provided"}, 400)

    content = await file.read()
    filename = file.filename
    suffix = Path(filename).suffix.lower()

    try:
        if suffix == ".csv":
            preview = _connector.parse_csv(content)
        elif suffix == ".json":
            preview = _connector.parse_json(content)
        elif suffix == ".xml":
            preview = _connector.parse_xml(content)
        else:
            return JSONResponse(
                {"error": "Unsupported file format. Use CSV, JSON, or XML."},
                status_code=400,
            )

        preview.filename = filename

        # Store data for later use — parse full rows
        # Re-parse to get all rows for generation
        data_rows = []
        if suffix == ".csv":
            import csv
            import io
            text = content.decode("utf-8")
            reader = csv.DictReader(io.StringIO(text))
            data_rows = [dict(row) for row in reader]
        elif suffix == ".json":
            import json as json_mod
            data = json_mod.loads(content.decode("utf-8"))
            if isinstance(data, list):
                data_rows = [_connector.flatten_json(item) if isinstance(item, dict) else {"value": item} for item in data]
            elif isinstance(data, dict):
                data_rows = [_connector.flatten_json(data)]
        elif suffix == ".xml":
            # Re-use the sample from preview for now; full XML parsing stores all rows
            import xml.etree.ElementTree as ET
            root = ET.fromstring(content)
            children = list(root)
            tag_counts: dict[str, int] = {}
            for child in children:
                tag = child.tag.split("}")[-1] if "}" in child.tag else child.tag
                tag_counts[tag] = tag_counts.get(tag, 0) + 1
            record_tag = max(tag_counts, key=tag_counts.get)
            records = [child for child in children
                       if (child.tag.split("}")[-1] if "}" in child.tag else child.tag) == record_tag]
            for record in records:
                row: dict[str, str] = {}
                for attr_name, attr_value in record.attrib.items():
                    row[f"@{attr_name}"] = attr_value
                for elem in record:
                    tag = elem.tag.split("}")[-1] if "}" in elem.tag else elem.tag
                    row[tag] = elem.text.strip() if elem.text else ""
                    for attr_name, attr_value in elem.attrib.items():
                        row[f"{tag}.@{attr_name}"] = attr_value
                data_rows.append(row)

        # Return preview + session info
        session_id = str(uuid.uuid4())
        session = PopulationSession(
            session_id=session_id,
            dataset=preview,
            data_rows=data_rows,
        )
        _sessions[session_id] = session

        return {
            "session_id": session_id,
            "source_type": preview.source_type,
            "columns": [
                {
                    "name": c.name,
                    "inferred_type": c.inferred_type,
                    "sample_values": c.sample_values,
                    "null_count": c.null_count,
                }
                for c in preview.columns
            ],
            "row_count": preview.row_count,
            "sample": preview.sample,
            "filename": preview.filename,
        }

    except ValueError as e:
        error_msg = str(e)
        if "50 MB" in error_msg:
            return JSONResponse({"error": error_msg}, status_code=413)
        return JSONResponse({"error": error_msg}, status_code=400)
    except Exception as e:
        return JSONResponse({"error": f"Failed to parse file: {e}"}, status_code=400)


@router.post("/connect-database")
async def connect_database(body: dict):
    """Connect to a SPARQL endpoint."""
    endpoint_url = body.get("endpoint_url", "")
    if not endpoint_url:
        return JSONResponse({"error": "No endpoint URL provided"}, 400)

    result = _connector.connect_sparql(endpoint_url)
    if not result.get("connected"):
        return JSONResponse({"error": result.get("message", "Connection failed")}, 502)

    # Create session with db connection
    session_id = str(uuid.uuid4())
    session = PopulationSession(session_id=session_id, db_endpoint=endpoint_url)
    _sessions[session_id] = session

    return {"session_id": session_id, **result}


@router.post("/query-database")
async def query_database(body: dict):
    """Execute a SPARQL query on a connected endpoint."""
    session_id = body.get("session_id", "")
    query = body.get("query", "")
    endpoint_url = body.get("endpoint_url", "")

    if not query:
        return JSONResponse({"error": "No query provided"}, 400)

    # Get endpoint from session or body
    if session_id and session_id in _sessions:
        session = _sessions[session_id]
        if session.db_endpoint:
            endpoint_url = session.db_endpoint

    if not endpoint_url:
        return JSONResponse({"error": "No endpoint URL. Connect to a database first."}, 400)

    try:
        result = _connector.execute_query(endpoint_url, query)

        # Store results as data rows in session
        if session_id and session_id in _sessions:
            session = _sessions[session_id]
            session.data_rows = result.get("rows", [])

        return result
    except ValueError as e:
        return JSONResponse({"error": str(e)}, 400)


# --- Ontology Selection ---


@router.get("/{project_id}/ontologies")
def list_ontologies(project_id: str):
    """List TTL files in a project with class/property counts."""
    project_dir = PROJECTS_DIR / project_id
    if not project_dir.exists():
        return JSONResponse({"error": "Project not found"}, 404)

    ttl_files = sorted(project_dir.glob("*.ttl"))
    ontologies = []

    for ttl_path in ttl_files:
        # Skip instance files
        if ttl_path.name.startswith("instances_"):
            continue
        try:
            content = ttl_path.read_text(encoding="utf-8")
            schema = mapping_service.extract_ontology_schema(content)
            ontologies.append({
                "filename": ttl_path.name,
                "class_count": len(schema.classes),
                "object_property_count": len(schema.object_properties),
                "datatype_property_count": len(schema.datatype_properties),
            })
        except Exception:
            ontologies.append({
                "filename": ttl_path.name,
                "class_count": 0,
                "object_property_count": 0,
                "datatype_property_count": 0,
                "error": "Could not parse file",
            })

    return {"project_id": project_id, "ontologies": ontologies}


@router.post("/{project_id}/select-ontology")
async def select_ontology(project_id: str, body: dict):
    """Parse a TTL file and return the extracted ontology schema."""
    project_dir = PROJECTS_DIR / project_id
    if not project_dir.exists():
        return JSONResponse({"error": "Project not found"}, 404)

    filename = body.get("filename", "model.ttl")
    ttl_path = project_dir / filename
    if not ttl_path.exists():
        return JSONResponse({"error": f"File '{filename}' not found"}, 404)

    try:
        content = ttl_path.read_text(encoding="utf-8")
        schema = mapping_service.extract_ontology_schema(content)

        if not schema.classes:
            return JSONResponse(
                {"error": "Selected file contains no OWL classes to populate", "warning": True},
                status_code=400,
            )

        # Store in session
        session = _get_or_create_session(project_id)
        session.ontology = schema

        return {
            "project_id": project_id,
            "filename": filename,
            "classes": [{"uri": c.uri, "label": c.label, "local_name": c.local_name} for c in schema.classes],
            "object_properties": [
                {"uri": p.uri, "label": p.label, "local_name": p.local_name, "domain": p.domain, "range": p.range}
                for p in schema.object_properties
            ],
            "datatype_properties": [
                {"uri": p.uri, "label": p.label, "local_name": p.local_name, "domain": p.domain, "range": p.range}
                for p in schema.datatype_properties
            ],
        }
    except Exception as e:
        return JSONResponse({"error": f"Failed to parse ontology: {e}"}, 400)


# --- Mapping ---


@router.post("/{project_id}/suggest-mapping")
async def suggest_mapping_endpoint(project_id: str, body: dict):
    """Generate an LLM-assisted mapping suggestion."""
    session_id = body.get("session_id", "")
    session = _sessions.get(session_id)

    if not session:
        # Try to find session by project
        session = _get_or_create_session(project_id)

    # Get columns and sample from session or body
    columns = body.get("columns", [])
    sample = body.get("sample", [])

    if not columns and session.dataset:
        columns = [{"name": c.name, "inferred_type": c.inferred_type} for c in session.dataset.columns]
        sample = session.dataset.sample

    if not columns:
        return JSONResponse({"error": "No dataset columns. Upload a dataset first."}, 400)

    # Get ontology from session or parse from project
    ontology = session.ontology
    if not ontology:
        ontology_file = body.get("ontology_file", "model.ttl")
        ttl_path = PROJECTS_DIR / project_id / ontology_file
        if ttl_path.exists():
            content = ttl_path.read_text(encoding="utf-8")
            ontology = mapping_service.extract_ontology_schema(content)
            session.ontology = ontology
        else:
            return JSONResponse({"error": "No ontology selected. Select an ontology first."}, 400)

    # Generate mapping suggestion
    try:
        from explorer.server import llm_manager
        suggestion = mapping_service.suggest_mapping(columns, sample, ontology, llm_manager)
        fallback = False
    except Exception:
        suggestion = mapping_service.heuristic_mapping(columns, ontology)
        fallback = True

    # Check for saved mappings that match these columns
    col_names = [c["name"] if isinstance(c, dict) else c.name for c in columns]
    reuse_suggestion = _find_matching_mapping(project_id, col_names)

    result = {
        "target_class": suggestion.target_class,
        "id_column": suggestion.id_column,
        "label_column": suggestion.label_column,
        "column_mappings": [
            {
                "column_name": cm.column_name,
                "mapped_property": cm.mapped_property,
                "mapping_type": cm.mapping_type,
                "confidence": cm.confidence,
                "target_class": cm.target_class,
            }
            for cm in suggestion.column_mappings
        ],
    }

    if fallback:
        result["fallback"] = True

    if reuse_suggestion:
        result["reuse_available"] = reuse_suggestion

    return result


@router.post("/{project_id}/confirm-mapping")
async def confirm_mapping(project_id: str, body: dict):
    """Validate and save a confirmed mapping."""
    project_dir = PROJECTS_DIR / project_id
    if not project_dir.exists():
        return JSONResponse({"error": "Project not found"}, 404)

    # Build ConfirmedMapping from request body
    raw_mappings = body.get("column_mappings", [])
    
    # Auto-map any "skip" or "unmapped" columns as new datatype properties
    # so data always gets into the graph
    target_class = body.get("target_class", "")
    ns = target_class.rsplit('#', 1)[0] + '#' if '#' in target_class else target_class.rsplit('/', 1)[0] + '/' if target_class else 'http://kg.local/ontology#'
    
    column_mappings = []
    for cm in raw_mappings:
        col_name = cm.get("column_name", "")
        mapped_prop = cm.get("mapped_property")
        map_type = cm.get("mapping_type", "unmapped")
        
        # If skip/unmapped and not the id/label column, auto-create a datatype property
        if map_type in ("skip", "unmapped", "") and not mapped_prop:
            if col_name and col_name != body.get("id_column") and col_name != body.get("label_column"):
                import re as _re
                prop_name = _re.sub(r'[^a-zA-Z0-9]', '_', col_name).strip('_')
                mapped_prop = ns + prop_name
                map_type = "datatype"
        
        column_mappings.append(ColumnMapping(
            column_name=col_name,
            mapped_property=mapped_prop,
            mapping_type=map_type,
            confidence=cm.get("confidence", 0.0),
            target_class=cm.get("target_class"),
        ))

    mapping = ConfirmedMapping(
        id=body.get("id", str(uuid.uuid4())),
        project_id=project_id,
        ontology_file=body.get("ontology_file", "model.ttl"),
        target_class=target_class,
        id_column=body.get("id_column", ""),
        label_column=body.get("label_column", ""),
        column_mappings=column_mappings,
        dataset_columns=body.get("dataset_columns", []),
    )

    # Validate against ontology
    ontology_path = project_dir / mapping.ontology_file
    if ontology_path.exists():
        content = ontology_path.read_text(encoding="utf-8")
        ontology = mapping_service.extract_ontology_schema(content)
        validation = mapping_service.validate_mapping(mapping, ontology)
        if not validation["valid"]:
            return JSONResponse(
                {"error": "; ".join(validation["errors"])},
                status_code=400,
            )

    # Save mapping as JSON
    mappings_dir = project_dir / "mappings"
    mappings_dir.mkdir(exist_ok=True)
    mapping_path = mappings_dir / f"mapping_{mapping.id}.json"
    mapping_path.write_text(mapping.to_json(), encoding="utf-8")

    # Store in session
    session = _get_or_create_session(project_id)
    session.mapping = mapping

    return {
        "confirmed": True,
        "mapping_id": mapping.id,
        "project_id": project_id,
    }


# --- Instance Generation ---


@router.post("/{project_id}/generate-instances")
async def generate_instances(project_id: str, body: dict):
    """Generate RDF instances from data + confirmed mapping."""
    project_dir = PROJECTS_DIR / project_id
    if not project_dir.exists():
        return JSONResponse({"error": "Project not found"}, 404)

    session_id = body.get("session_id", "")
    mapping_id = body.get("mapping_id", "")
    base_uri = body.get("base_uri", "http://kg.local/resource/")

    # Get mapping
    mapping = None
    if mapping_id:
        mapping_path = project_dir / "mappings" / f"mapping_{mapping_id}.json"
        if mapping_path.exists():
            mapping = ConfirmedMapping.from_json(mapping_path.read_text(encoding="utf-8"))

    if not mapping:
        session = _sessions.get(session_id) or _get_or_create_session(project_id)
        mapping = session.mapping

    if not mapping:
        return JSONResponse({"error": "No confirmed mapping. Confirm a mapping first."}, 400)

    # Get data rows
    data_rows = body.get("data", [])
    if not data_rows:
        session = _sessions.get(session_id)
        if session:
            data_rows = session.data_rows

    if not data_rows:
        return JSONResponse({"error": "No data rows to process"}, 400)

    # Check for existing instance graph (incremental loading)
    # Only use existing graph if explicitly requested
    existing_graph = None
    if body.get("incremental", False):
        existing_files = sorted(project_dir.glob("instances_*.ttl"))
        if existing_files:
            existing_graph = RDFGraph()
            for f in existing_files:
                try:
                    existing_graph.parse(str(f), format="turtle")
                except Exception:
                    pass

    try:
        result = instance_generator.generate(
            data=data_rows,
            mapping=mapping,
            base_uri=base_uri,
            existing_graph=existing_graph,
        )

        # Save generated TTL — ONLY the new instances, not existing graph
        timestamp = int(time.time())
        output_path = project_dir / f"instances_{timestamp}.ttl"
        output_path.write_text(result.ttl, encoding="utf-8")
        
        # Verify the file has actual instance data
        print(f"  [Population] Generated {result.instances_created} instances, {result.triples_generated} triples")
        print(f"  [Population] TTL size: {len(result.ttl)} bytes, saved to {output_path.name}")

        return {
            "generated": True,
            "filename": output_path.name,
            "instances_created": result.instances_created,
            "instances_updated": result.instances_updated,
            "triples_generated": result.triples_generated,
            "rows_skipped": result.rows_skipped,
            "skipped_reasons": result.skipped_reasons,
        }
    except ValueError as e:
        return JSONResponse({"error": str(e)}, 400)
    except Exception as e:
        return JSONResponse({"error": f"Internal error generating RDF: {e}"}, 500)


# --- Export & Push ---


@router.post("/{project_id}/export")
async def export_graph_endpoint(project_id: str, body: dict):
    """Export the populated graph in the requested format."""
    project_dir = PROJECTS_DIR / project_id
    if not project_dir.exists():
        return JSONResponse({"error": "Project not found"}, 404)

    format_name = body.get("format", "turtle")

    # Build combined graph (ontology + instances)
    combined = RDFGraph()
    for ttl_path in project_dir.glob("*.ttl"):
        try:
            combined.parse(str(ttl_path), format="turtle")
        except Exception:
            pass

    if len(combined) == 0:
        return JSONResponse({"error": "No graph data to export"}, 400)

    try:
        data = export_service.export_graph(combined, format_name)

        # Determine content type and extension
        content_types = {
            "turtle": ("text/turtle", ".ttl"),
            "ttl": ("text/turtle", ".ttl"),
            "nt": ("application/n-triples", ".nt"),
            "n-triples": ("application/n-triples", ".nt"),
            "ntriples": ("application/n-triples", ".nt"),
            "json-ld": ("application/ld+json", ".jsonld"),
            "jsonld": ("application/ld+json", ".jsonld"),
        }
        content_type, ext = content_types.get(format_name.lower(), ("text/turtle", ".ttl"))

        return Response(
            content=data,
            media_type=content_type,
            headers={"Content-Disposition": f"attachment; filename={project_id}_export{ext}"},
        )
    except ValueError as e:
        return JSONResponse({"error": str(e)}, 400)


@router.post("/{project_id}/push-neptune")
async def push_neptune(project_id: str, body: dict):
    """Push triples to a Neptune/SPARQL endpoint in batches."""
    project_dir = PROJECTS_DIR / project_id
    if not project_dir.exists():
        return JSONResponse({"error": "Project not found"}, 404)

    endpoint = body.get("endpoint", "")
    batch_size = body.get("batch_size", 1000)

    if not endpoint:
        return JSONResponse({"error": "No Neptune endpoint provided"}, 400)

    # Build combined graph
    combined = RDFGraph()
    for ttl_path in project_dir.glob("*.ttl"):
        try:
            combined.parse(str(ttl_path), format="turtle")
        except Exception:
            pass

    if len(combined) == 0:
        return JSONResponse({"error": "No graph data to push"}, 400)

    result = export_service.push_to_neptune(combined, endpoint, batch_size)

    if not result.success:
        return JSONResponse({
            "error": result.error,
            "batches_completed": result.batches_completed,
            "triples_pushed": result.triples_pushed,
            "retry_from": result.failed_batch,
        }, 502)

    return {
        "success": True,
        "total_triples": result.total_triples,
        "triples_pushed": result.triples_pushed,
        "batches_completed": result.batches_completed,
        "total_batches": result.total_batches,
    }


@router.post("/{project_id}/push-neptune/retry")
async def push_neptune_retry(project_id: str, body: dict):
    """Retry a failed Neptune push from the failed batch."""
    project_dir = PROJECTS_DIR / project_id
    if not project_dir.exists():
        return JSONResponse({"error": "Project not found"}, 404)

    endpoint = body.get("endpoint", "")
    start_batch = body.get("start_batch", 0)
    batch_size = body.get("batch_size", 1000)

    if not endpoint:
        return JSONResponse({"error": "No Neptune endpoint provided"}, 400)

    # Build combined graph
    combined = RDFGraph()
    for ttl_path in project_dir.glob("*.ttl"):
        try:
            combined.parse(str(ttl_path), format="turtle")
        except Exception:
            pass

    if len(combined) == 0:
        return JSONResponse({"error": "No graph data to push"}, 400)

    result = export_service.push_to_neptune(combined, endpoint, batch_size, start_batch)

    if not result.success:
        return JSONResponse({
            "error": result.error,
            "batches_completed": result.batches_completed,
            "triples_pushed": result.triples_pushed,
            "retry_from": result.failed_batch,
        }, 502)

    return {
        "success": True,
        "total_triples": result.total_triples,
        "triples_pushed": result.triples_pushed,
        "batches_completed": result.batches_completed,
        "total_batches": result.total_batches,
    }


# --- Mapping Management ---


@router.get("/{project_id}/mappings")
def list_mappings(project_id: str):
    """List saved mappings for a project."""
    project_dir = PROJECTS_DIR / project_id
    if not project_dir.exists():
        return JSONResponse({"error": "Project not found"}, 404)

    mappings_dir = project_dir / "mappings"
    if not mappings_dir.exists():
        return {"project_id": project_id, "mappings": []}

    mappings = []
    for mapping_path in sorted(mappings_dir.glob("mapping_*.json")):
        try:
            mapping = ConfirmedMapping.from_json(mapping_path.read_text(encoding="utf-8"))
            mappings.append({
                "id": mapping.id,
                "ontology_file": mapping.ontology_file,
                "target_class": mapping.target_class,
                "id_column": mapping.id_column,
                "label_column": mapping.label_column,
                "column_count": len(mapping.column_mappings),
                "created_at": mapping.created_at,
                "dataset_columns": mapping.dataset_columns,
            })
        except Exception:
            continue

    return {"project_id": project_id, "mappings": mappings}


@router.delete("/{project_id}/mappings/{mapping_id}")
def delete_mapping(project_id: str, mapping_id: str):
    """Delete a saved mapping."""
    project_dir = PROJECTS_DIR / project_id
    if not project_dir.exists():
        return JSONResponse({"error": "Project not found"}, 404)

    mapping_path = project_dir / "mappings" / f"mapping_{mapping_id}.json"
    if not mapping_path.exists():
        return JSONResponse({"error": "Mapping not found"}, 404)

    mapping_path.unlink()
    return {"deleted": True, "mapping_id": mapping_id}


# --- Helper Functions ---


def _find_matching_mapping(project_id: str, columns: list[str]) -> dict | None:
    """Find a saved mapping whose dataset_columns match the given columns."""
    mappings_dir = PROJECTS_DIR / project_id / "mappings"
    if not mappings_dir.exists():
        return None

    for mapping_path in mappings_dir.glob("mapping_*.json"):
        try:
            mapping = ConfirmedMapping.from_json(mapping_path.read_text(encoding="utf-8"))
            if mapping.dataset_columns and set(mapping.dataset_columns) == set(columns):
                return {
                    "mapping_id": mapping.id,
                    "ontology_file": mapping.ontology_file,
                    "target_class": mapping.target_class,
                }
        except Exception:
            continue

    return None
