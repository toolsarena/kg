"""
Project routes — multi-file projects.
Each project is a folder with meta.json + multiple .ttl files.
Each .ttl is an independent ontology. Build = single file. Merge = explicit combine.
"""
import json
import time
from pathlib import Path
from fastapi import APIRouter, UploadFile, File
from fastapi.responses import JSONResponse
from rdflib import Graph as RDFGraph

router = APIRouter(prefix="/api/projects", tags=["projects"])

PROJECTS_DIR = Path("projects")
PROJECTS_DIR.mkdir(exist_ok=True)


def get_file_info(ttl_path: Path) -> dict:
    """Get metadata for a .ttl file including name, size, modified timestamp, and triples count."""
    stat = ttl_path.stat()
    try:
        g = RDFGraph()
        g.parse(str(ttl_path), format="turtle")
        triples = len(g)
    except Exception:
        triples = 0
    return {
        "name": ttl_path.name,
        "size": stat.st_size,
        "modified": stat.st_mtime,
        "triples": triples,
    }


@router.get("/")
def list_projects():
    """List all projects."""
    projects = []
    for d in sorted(PROJECTS_DIR.iterdir()):
        if d.is_dir():
            meta_path = d / "meta.json"
            meta = json.loads(meta_path.read_text()) if meta_path.exists() else {"name": d.name}
            meta["id"] = d.name
            # List all .ttl files
            ttl_files = sorted(d.glob("*.ttl"))
            meta["files"] = [get_file_info(f) for f in ttl_files]
            meta["file_count"] = len(ttl_files)
            meta["total_triples"] = sum(f["triples"] for f in meta["files"])
            projects.append(meta)
    return projects


@router.post("/create")
async def create_project(body: dict):
    """Create a new project."""
    name = body.get("name", "").strip()
    if not name:
        return JSONResponse({"error": "No project name"}, 400)
    pid = name.lower().replace(" ", "_").replace("-", "_")
    pid = "".join(c for c in pid if c.isalnum() or c == "_")[:40]
    project_dir = PROJECTS_DIR / pid
    if project_dir.exists():
        return JSONResponse({"error": f"Project '{pid}' already exists"}, 400)
    project_dir.mkdir()
    meta = {"name": name, "id": pid, "created": time.time(), "modified": time.time()}
    (project_dir / "meta.json").write_text(json.dumps(meta, indent=2))
    return meta


@router.get("/{project_id}")
def get_project(project_id: str):
    """Get project details + list of files."""
    project_dir = PROJECTS_DIR / project_id
    if not project_dir.exists():
        return JSONResponse({"error": "Project not found"}, 404)
    meta_path = project_dir / "meta.json"
    meta = json.loads(meta_path.read_text()) if meta_path.exists() else {"name": project_id}
    meta["id"] = project_id
    ttl_files = sorted(project_dir.glob("*.ttl"))
    meta["files"] = [get_file_info(f) for f in ttl_files]
    meta["file_count"] = len(ttl_files)
    meta["total_triples"] = sum(f["triples"] for f in meta["files"])
    # For backward compat: if model.ttl exists, include its content as "ttl"
    model_path = project_dir / "model.ttl"
    if model_path.exists():
        meta["ttl"] = model_path.read_text(encoding="utf-8")
    return meta


@router.get("/{project_id}/file/{filename}")
def get_file(project_id: str, filename: str):
    """Get content of a specific .ttl file."""
    fpath = PROJECTS_DIR / project_id / filename
    if not fpath.exists():
        return JSONResponse({"error": "File not found"}, 404)
    content = fpath.read_text(encoding="utf-8")
    info = get_file_info(fpath)
    return {"filename": filename, "content": content, "triples": info["triples"]}


@router.post("/{project_id}/files")
async def create_file(project_id: str, body: dict):
    """Create a new empty .ttl file within a project."""
    project_dir = PROJECTS_DIR / project_id
    if not project_dir.exists():
        return JSONResponse({"error": "Project not found"}, 404)

    filename = body.get("filename", "").strip()
    if not filename:
        return JSONResponse({"error": "No filename provided"}, 400)
    # Ensure .ttl extension
    if not filename.endswith(".ttl"):
        filename += ".ttl"
    # Sanitize: only allow safe characters in filename
    safe_name = "".join(c for c in filename if c.isalnum() or c in ("_", "-", "."))
    if not safe_name or safe_name == ".ttl":
        return JSONResponse({"error": "Invalid filename"}, 400)

    file_path = project_dir / safe_name
    if file_path.exists():
        return JSONResponse({"error": f"File '{safe_name}' already exists"}, 400)

    # Create empty TTL file with minimal header
    empty_ttl = f"# {safe_name} — created {time.strftime('%Y-%m-%d %H:%M:%S')}\n"
    file_path.write_text(empty_ttl, encoding="utf-8")

    # Update project meta
    meta_path = project_dir / "meta.json"
    if meta_path.exists():
        meta = json.loads(meta_path.read_text())
        meta["modified"] = time.time()
        meta_path.write_text(json.dumps(meta, indent=2))

    return {"created": True, "filename": safe_name, "project_id": project_id}


@router.post("/{project_id}/upload")
async def upload_file(project_id: str, file: UploadFile = File(...)):
    """Upload an existing .ttl file into a project."""
    project_dir = PROJECTS_DIR / project_id
    if not project_dir.exists():
        return JSONResponse({"error": "Project not found"}, 404)

    if not file.filename:
        return JSONResponse({"error": "No file provided"}, 400)

    # Ensure .ttl extension
    filename = file.filename
    if not filename.endswith(".ttl"):
        return JSONResponse({"error": "Only .ttl files are supported"}, 400)

    # Sanitize filename
    safe_name = "".join(c for c in filename if c.isalnum() or c in ("_", "-", "."))
    if not safe_name or safe_name == ".ttl":
        return JSONResponse({"error": "Invalid filename"}, 400)

    # Read file content
    content = await file.read()
    try:
        ttl_text = content.decode("utf-8")
    except UnicodeDecodeError:
        return JSONResponse({"error": "File must be UTF-8 encoded"}, 400)

    # Validate TTL
    try:
        g = RDFGraph()
        g.parse(data=ttl_text, format="turtle")
        triples = len(g)
    except Exception as e:
        return JSONResponse({"error": f"Invalid TTL: {e}"}, 400)

    # Save file
    file_path = project_dir / safe_name
    file_path.write_text(ttl_text, encoding="utf-8")

    # Update project meta
    meta_path = project_dir / "meta.json"
    if meta_path.exists():
        meta = json.loads(meta_path.read_text())
        meta["modified"] = time.time()
        meta_path.write_text(json.dumps(meta, indent=2))

    return {
        "uploaded": True,
        "filename": safe_name,
        "project_id": project_id,
        "triples": triples,
        "size": len(content),
    }


@router.post("/{project_id}/save")
async def save_project(project_id: str, body: dict):
    """Save TTL as a new file or overwrite existing in project."""
    project_dir = PROJECTS_DIR / project_id
    if not project_dir.exists():
        return JSONResponse({"error": "Project not found"}, 404)
    ttl = body.get("ttl", "")
    filename = body.get("filename", "model.ttl")
    if not ttl:
        return JSONResponse({"error": "No TTL"}, 400)
    # Validate
    try:
        g = RDFGraph()
        g.parse(data=ttl, format="turtle")
    except Exception as e:
        return JSONResponse({"error": f"Invalid TTL: {e}"}, 400)
    # Save
    (project_dir / filename).write_text(ttl, encoding="utf-8")
    # Update meta
    meta_path = project_dir / "meta.json"
    meta = json.loads(meta_path.read_text()) if meta_path.exists() else {}
    meta["modified"] = time.time()
    meta_path.write_text(json.dumps(meta, indent=2))
    return {"saved": True, "filename": filename, "triples": len(g)}


@router.post("/{project_id}/build")
async def build_project(project_id: str, body: dict = None):
    """Build graph from a single file or all files in project."""
    project_dir = PROJECTS_DIR / project_id
    if not project_dir.exists():
        return JSONResponse({"error": "Project not found"}, 404)

    # Determine which file(s) to build
    filename = body.get("filename") if body else None
    if filename:
        ttl_files = [project_dir / filename]
        if not ttl_files[0].exists():
            return JSONResponse({"error": f"File '{filename}' not found"}, 404)
    else:
        # Default: build model.ttl for backward compat
        ttl_files = [project_dir / "model.ttl"]
        if not ttl_files[0].exists():
            # Try first .ttl file
            ttl_files = sorted(project_dir.glob("*.ttl"))[:1]
        if not ttl_files:
            return JSONResponse({"error": "No .ttl files in project"}, 404)

    try:
        import explorer.server as srv
        from rdflib import Graph as RG, RDF, RDFS
        from rdflib.namespace import SKOS

        ng = RG()
        for f in ttl_files:
            ng.parse(str(f), format="turtle")

        srv.new_model_nodes = []
        srv.new_model_edges = []
        all_uris = set()
        for s, p, o in ng:
            if hasattr(s, 'n3'):
                all_uris.add(s)
            if hasattr(o, 'n3') and str(o).startswith('http'):
                all_uris.add(o)

        skip_preds = {str(RDF.type), str(SKOS.prefLabel), str(RDFS.label), str(RDFS.comment)}
        # Skip well-known vocabulary URIs from becoming nodes
        _VOCAB_URIS = {'http://www.w3.org/2002/07/owl#Class', 'http://www.w3.org/2002/07/owl#ObjectProperty',
                       'http://www.w3.org/2002/07/owl#DatatypeProperty', 'http://www.w3.org/2002/07/owl#Ontology',
                       'http://www.w3.org/2002/07/owl#NamedIndividual', 'http://www.w3.org/2000/01/rdf-schema#Class',
                       'http://www.w3.org/2000/01/rdf-schema#Resource'}
        node_ids = set()
        for uri in all_uris:
            if str(uri) in _VOCAB_URIS:
                continue
            uid = str(uri).split('/')[-1].split('#')[-1]
            label = uid.replace('_', ' ').title()
            for _, _, o in ng.triples((uri, RDFS.label, None)):
                label = str(o)
            for _, _, o in ng.triples((uri, SKOS.prefLabel, None)):
                label = str(o)
            ntype = 'concept'
            for _, _, o in ng.triples((uri, RDF.type, None)):
                t = str(o).split('#')[-1].split('/')[-1]
                if t in ('Ontology',):
                    ntype = None  # skip only Ontology declarations
                    break
                elif t in ('Class', 'ObjectProperty', 'DatatypeProperty'):
                    ntype = t.lower()  # keep as class/objectproperty/datatypeproperty
                elif t not in ('NamedIndividual',):
                    ntype = t.lower()
            if ntype is None:
                continue  # skip Ontology nodes only
            # Ensure type is never empty — default to "concept"
            if not ntype or not ntype.strip():
                ntype = 'concept'
            srv.new_model_nodes.append({'id': uid, 'label': label, 'type': ntype, 'uri': str(uri)})
            node_ids.add(uid)

        for s, p, o in ng:
            if str(p) in skip_preds:
                continue
            sid = str(s).split('/')[-1].split('#')[-1]
            oid = str(o).split('/')[-1].split('#')[-1] if hasattr(o, 'n3') else None
            if oid and sid in node_ids and oid in node_ids:
                rel = str(p).split('/')[-1].split('#')[-1]
                # Ensure relation is never empty — default to "relatedTo"
                if not rel or not rel.strip():
                    rel = 'relatedTo'
                srv.new_model_edges.append({'source': sid, 'target': oid, 'relation': rel})

        return {
            "built": True,
            "nodes": len(srv.new_model_nodes),
            "edges": len(srv.new_model_edges),
            "triples": len(ng),
            "graph_data": {
                "nodes": srv.new_model_nodes,
                "edges": srv.new_model_edges,
            },
        }
    except Exception as e:
        return JSONResponse({"error": str(e)}, 500)


@router.post("/{project_id}/merge")
async def merge_files(project_id: str, body: dict):
    """Merge selected .ttl files into a new combined file."""
    project_dir = PROJECTS_DIR / project_id
    if not project_dir.exists():
        return JSONResponse({"error": "Project not found"}, 404)
    filenames = body.get("files", [])
    output_name = body.get("output", "merged.ttl")
    if not filenames:
        return JSONResponse({"error": "No files selected"}, 400)

    combined = RDFGraph()
    for fname in filenames:
        fpath = project_dir / fname
        if fpath.exists():
            combined.parse(str(fpath), format="turtle")

    ttl = combined.serialize(format="turtle")
    (project_dir / output_name).write_text(ttl, encoding="utf-8")

    # Update meta
    meta_path = project_dir / "meta.json"
    meta = json.loads(meta_path.read_text()) if meta_path.exists() else {}
    meta["modified"] = time.time()
    meta_path.write_text(json.dumps(meta, indent=2))

    return {"merged": True, "output": output_name, "triples": len(combined), "source_files": filenames}


@router.post("/{project_id}/merge-and-build")
async def merge_and_build(project_id: str, body: dict = None):
    """Merge selected files (or all), save merged.ttl, then build for visualization."""
    project_dir = PROJECTS_DIR / project_id
    if not project_dir.exists():
        return JSONResponse({"error": "Project not found"}, 404)

    body = body or {}
    filenames = body.get("files")  # None or empty = all files
    output_name = body.get("output", "merged.ttl")

    if not filenames:
        filenames = [f.name for f in sorted(project_dir.glob("*.ttl"))
                     if f.name != "merged.ttl"]

    if not filenames:
        return JSONResponse({"error": "No .ttl files to merge"}, 400)

    # Merge all selected files into a single graph
    combined = RDFGraph()
    for fname in filenames:
        fpath = project_dir / fname
        if fpath.exists():
            combined.parse(str(fpath), format="turtle")

    # Save merged output
    ttl = combined.serialize(format="turtle")
    (project_dir / output_name).write_text(ttl, encoding="utf-8")

    # Build graph for visualization (populate nodes/edges)
    try:
        import explorer.server as srv
        from rdflib import Graph as RG, RDF, RDFS
        from rdflib.namespace import SKOS

        srv.new_model_nodes = []
        srv.new_model_edges = []
        all_uris = set()
        for s, p, o in combined:
            if hasattr(s, 'n3'):
                all_uris.add(s)
            if hasattr(o, 'n3') and str(o).startswith('http'):
                all_uris.add(o)

        skip_preds = {str(RDF.type), str(SKOS.prefLabel), str(RDFS.label), str(RDFS.comment)}
        _VOCAB_URIS = {'http://www.w3.org/2002/07/owl#Class', 'http://www.w3.org/2002/07/owl#ObjectProperty',
                       'http://www.w3.org/2002/07/owl#DatatypeProperty', 'http://www.w3.org/2002/07/owl#Ontology',
                       'http://www.w3.org/2002/07/owl#NamedIndividual', 'http://www.w3.org/2000/01/rdf-schema#Class',
                       'http://www.w3.org/2000/01/rdf-schema#Resource'}
        node_ids = set()
        for uri in all_uris:
            if str(uri) in _VOCAB_URIS:
                continue
            uid = str(uri).split('/')[-1].split('#')[-1]
            label = uid.replace('_', ' ').title()
            for _, _, o in combined.triples((uri, RDFS.label, None)):
                label = str(o)
            for _, _, o in combined.triples((uri, SKOS.prefLabel, None)):
                label = str(o)
            ntype = 'concept'
            for _, _, o in combined.triples((uri, RDF.type, None)):
                t = str(o).split('#')[-1].split('/')[-1]
                if t in ('Ontology',):
                    ntype = None
                    break
                elif t in ('Class', 'ObjectProperty', 'DatatypeProperty'):
                    ntype = t.lower()
                elif t not in ('NamedIndividual',):
                    ntype = t.lower()
            if ntype is None:
                continue
            # Ensure type is never empty — default to "concept"
            if not ntype or not ntype.strip():
                ntype = 'concept'
            srv.new_model_nodes.append({'id': uid, 'label': label, 'type': ntype, 'uri': str(uri)})
            node_ids.add(uid)

        for s, p, o in combined:
            if str(p) in skip_preds:
                continue
            sid = str(s).split('/')[-1].split('#')[-1]
            oid = str(o).split('/')[-1].split('#')[-1] if hasattr(o, 'n3') else None
            if oid and sid in node_ids and oid in node_ids:
                rel = str(p).split('/')[-1].split('#')[-1]
                # Ensure relation is never empty — default to "relatedTo"
                if not rel or not rel.strip():
                    rel = 'relatedTo'
                srv.new_model_edges.append({'source': sid, 'target': oid, 'relation': rel})

        # Update project meta
        meta_path = project_dir / "meta.json"
        if meta_path.exists():
            meta = json.loads(meta_path.read_text())
            meta["modified"] = time.time()
            meta_path.write_text(json.dumps(meta, indent=2))

        return {
            "merged": True,
            "built": True,
            "output": output_name,
            "triples": len(combined),
            "nodes": len(srv.new_model_nodes),
            "edges": len(srv.new_model_edges),
            "source_files": filenames,
            "graph_data": {
                "nodes": srv.new_model_nodes,
                "edges": srv.new_model_edges,
            },
        }
    except Exception as e:
        return JSONResponse({"error": str(e)}, 500)


@router.delete("/{project_id}/file/{filename}")
async def delete_file(project_id: str, filename: str):
    """Delete a .ttl file from project."""
    fpath = PROJECTS_DIR / project_id / filename
    if not fpath.exists():
        return JSONResponse({"error": "File not found"}, 404)
    fpath.unlink()
    return {"deleted": filename}
