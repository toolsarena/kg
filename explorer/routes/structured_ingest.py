"""
Structured Data Ingest — takes tabular data (CSV/TSV/pasted table) and builds
a connected graph with proper relationships between columns.

This is an ADDITIONAL ingest mode. Does not modify existing ingest routes.

Flow:
1. User pastes or uploads tabular data
2. /api/ingest/structured/analyze — detects columns, suggests graph structure
3. /api/ingest/structured/build — generates RDF with relationships and saves to project
"""
import re
import csv
import io
import time
from pathlib import Path
from fastapi import APIRouter, UploadFile, File
from fastapi.responses import JSONResponse

router = APIRouter(prefix="/api/ingest/structured", tags=["structured-ingest"])


def parse_table(text: str) -> tuple:
    """Parse tabular text (CSV, TSV, or pipe-separated). Returns (headers, rows)."""
    text = text.strip()
    if not text:
        return [], []

    # Detect separator
    first_line = text.split('\n')[0]
    if '\t' in first_line:
        sep = '\t'
    elif '|' in first_line and first_line.count('|') > 1:
        sep = '|'
    else:
        sep = ','

    if sep == '|':
        lines = [l.strip().strip('|') for l in text.split('\n') if l.strip() and not all(c in '-|+ ' for c in l.strip())]
        headers = [h.strip() for h in lines[0].split('|')]
        rows = []
        for line in lines[1:]:
            cells = [c.strip() for c in line.split('|')]
            if len(cells) == len(headers):
                rows.append(dict(zip(headers, cells)))
    else:
        reader = csv.DictReader(io.StringIO(text), delimiter=sep)
        headers = reader.fieldnames or []
        rows = [row for row in reader]

    return headers, rows


def detect_graph_structure(headers: list, rows: list) -> dict:
    """Analyze columns and suggest how to build the graph.
    
    Returns a structure suggestion:
    - entity_column: which column has the main entities (usually first or 'Name'/'Person')
    - group_columns: columns that create hub nodes (e.g. Area, Department, Team)
    - attribute_columns: columns that become properties (e.g. Resource Type)
    - activity_columns: columns with pipe-separated activities that become leaf nodes
    """
    if not headers or not rows:
        return {"entity_column": None, "group_columns": [], "attribute_columns": [], "activity_columns": []}

    entity_col = headers[0]  # Default: first column is the entity
    group_cols = []
    attr_cols = []
    activity_cols = []

    for h in headers:
        hl = h.lower().strip()
        col_values = [row.get(h, '').strip() for row in rows if row.get(h, '').strip()]
        unique_ratio = len(set(col_values)) / max(len(col_values), 1)

        # Check if values contain pipe separators (multi-value / activities)
        has_pipes = any('|' in v for v in col_values)

        if hl in ('name', 'person', 'people', 'member', 'employee', 'resource', 'stakeholder'):
            entity_col = h
        elif has_pipes:
            activity_cols.append(h)
        elif hl in ('area', 'department', 'team', 'group', 'division', 'unit', 'function', 'domain', 'category', 'type', 'resource type'):
            group_cols.append(h)
        elif unique_ratio < 0.5 and len(set(col_values)) <= 20:
            # Low cardinality = grouping column
            group_cols.append(h)
        else:
            attr_cols.append(h)

    # If entity_col ended up in group/attr, remove it
    group_cols = [c for c in group_cols if c != entity_col]
    attr_cols = [c for c in attr_cols if c != entity_col]
    activity_cols = [c for c in activity_cols if c != entity_col]

    return {
        "entity_column": entity_col,
        "group_columns": group_cols,
        "attribute_columns": attr_cols,
        "activity_columns": activity_cols,
    }


def build_graph_from_table(headers: list, rows: list, structure: dict, title: str = "Structured Data") -> str:
    """Build RDF/TTL from tabular data using the detected structure."""
    entity_col = structure["entity_column"]
    group_cols = structure["group_columns"]
    attr_cols = structure["attribute_columns"]
    activity_cols = structure["activity_columns"]

    def to_id(text):
        return re.sub(r'[^a-z0-9_]', '_', text.strip().lower())[:80]

    lines = [
        "@prefix kg: <http://kg.local/ontology#> .",
        "@prefix kgr: <http://kg.local/resource/> .",
        "@prefix skos: <http://www.w3.org/2004/02/skos/core#> .",
        "@prefix rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> .",
        "@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .",
        "@prefix owl: <http://www.w3.org/2002/07/owl#> .",
        "",
        f'# Generated from structured data: {title}',
        f'# {len(rows)} rows, {len(headers)} columns',
        "",
    ]

    # Create central hub node only if title is explicitly provided
    hub_id = None
    if title and title != "Structured Data":
        hub_id = to_id(title)
        lines.append(f'kgr:{hub_id} a kg:Project ; skos:prefLabel "{title}" .')
        lines.append("")

    # Create group nodes (Areas, Departments, etc.)
    group_nodes = {}  # {col: {value: id}}
    for col in group_cols:
        col_id = to_id(col)
        lines.append(f'# --- {col} groups ---')
        unique_values = sorted(set(row.get(col, '').strip() for row in rows if row.get(col, '').strip()))
        group_nodes[col] = {}
        for val in unique_values:
            vid = to_id(val)
            group_nodes[col][val] = vid
            label = val.replace('"', '\\"')
            lines.append(f'kgr:{vid} a kg:Group ; skos:prefLabel "{label}" ; kg:groupType "{col}" .')
            if hub_id:
                lines.append(f'kgr:{vid} kg:partOf kgr:{hub_id} .')
        lines.append("")

    # Create entity nodes (People, Items, etc.)
    lines.append(f'# --- {entity_col} entities ---')
    entity_ids = {}
    for row in rows:
        name = row.get(entity_col, '').strip()
        if not name:
            continue
        eid = to_id(name)
        entity_ids[name] = eid
        label = name.replace('"', '\\"')
        lines.append(f'kgr:{eid} a kg:Entity ; skos:prefLabel "{label}" .')

        # Link to groups
        for col in group_cols:
            val = row.get(col, '').strip()
            if val and val in group_nodes.get(col, {}):
                gid = group_nodes[col][val]
                rel = to_id(f"belongs_to_{col}")
                lines.append(f'kgr:{eid} kg:{rel} kgr:{gid} .')

        # Add attributes
        for col in attr_cols:
            val = row.get(col, '').strip()
            if val:
                prop = to_id(col)
                val_escaped = val.replace('"', '\\"')[:200]
                lines.append(f'kgr:{eid} kg:{prop} "{val_escaped}" .')

        # Link to activities (pipe-separated values become nodes)
        for col in activity_cols:
            val = row.get(col, '').strip()
            if val:
                activities = [a.strip() for a in val.split('|') if a.strip()]
                for act in activities:
                    aid = to_id(act)
                    act_label = act.replace('"', '\\"')
                    lines.append(f'kgr:{aid} a kg:Activity ; skos:prefLabel "{act_label}" .')
                    rel = to_id(f"does_{col}")
                    lines.append(f'kgr:{eid} kg:{rel} kgr:{aid} .')

    lines.append("")
    return "\n".join(lines)


@router.post("/analyze")
async def analyze_structured(body: dict):
    """Analyze tabular data and suggest graph structure."""
    text = body.get("text", "")
    title = body.get("title", "Structured Data")
    if not text:
        return JSONResponse({"error": "No data provided"}, 400)

    headers, rows = parse_table(text)
    if not headers or not rows:
        return JSONResponse({"error": "Could not parse table. Ensure data has headers and rows."}, 400)

    structure = detect_graph_structure(headers, rows)

    return {
        "headers": headers,
        "row_count": len(rows),
        "structure": structure,
        "title": title,
        "preview_rows": rows[:5],
    }


@router.post("/build")
async def build_structured(body: dict):
    """Build RDF graph from structured data and save to project."""
    text = body.get("text", "")
    title = body.get("title", "")
    project_id = body.get("project_id")
    filename = body.get("filename")
    structure_override = body.get("structure")  # Optional: user can override detected structure

    if not text:
        return JSONResponse({"error": "No data provided"}, 400)
    if not project_id:
        return JSONResponse({"error": "No project_id provided"}, 400)

    headers, rows = parse_table(text)
    if not headers or not rows:
        return JSONResponse({"error": "Could not parse table"}, 400)

    # Use override or auto-detect
    structure = structure_override or detect_graph_structure(headers, rows)

    # Build TTL
    ttl = build_graph_from_table(headers, rows, structure, title)

    # Save to project
    project_dir = Path("projects") / project_id
    project_dir.mkdir(parents=True, exist_ok=True)
    if not filename:
        filename = f"structured_{int(time.time())}.ttl"
    if not filename.endswith('.ttl'):
        filename += '.ttl'

    (project_dir / filename).write_text(ttl, encoding="utf-8")

    # Count what was generated
    entity_count = len([r for r in rows if r.get(structure["entity_column"], '').strip()])
    group_count = sum(len(set(r.get(col, '').strip() for r in rows if r.get(col, '').strip())) for col in structure["group_columns"])

    return {
        "ttl": ttl,
        "filename": filename,
        "project_id": project_id,
        "entity_count": entity_count,
        "group_count": group_count,
        "row_count": len(rows),
        "structure": structure,
    }
