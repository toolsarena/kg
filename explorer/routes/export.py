"""
Export routes — download graph as TTL, CSV, JSON-LD.
"""
from pathlib import Path
from fastapi import APIRouter
from fastapi.responses import FileResponse, Response, JSONResponse

router = APIRouter(prefix="/api/export", tags=["export"])


@router.get("/ttl")
def export_ttl():
    """Download the main graph as TTL."""
    p = Path("graphify-out/graph.ttl")
    if not p.exists():
        return JSONResponse({"error": "No graph.ttl found"}, 404)
    return FileResponse(str(p), media_type="text/turtle", filename="graph.ttl")


@router.get("/csv")
def export_csv():
    """Export graph as CSV (subject, predicate, object)."""
    from explorer.server import g as graph
    if not graph:
        return JSONResponse({"error": "No graph loaded"}, 404)
    lines = ["subject,predicate,object"]
    for s, p, o in graph:
        lines.append(f'"{s}","{p}","{o}"')
    return Response(content="\n".join(lines), media_type="text/csv",
                    headers={"Content-Disposition": "attachment; filename=graph.csv"})


@router.get("/jsonld")
def export_jsonld():
    """Export graph as JSON-LD."""
    from explorer.server import g as graph
    if not graph:
        return JSONResponse({"error": "No graph loaded"}, 404)
    jsonld = graph.serialize(format="json-ld")
    return Response(content=jsonld, media_type="application/ld+json",
                    headers={"Content-Disposition": "attachment; filename=graph.jsonld"})
