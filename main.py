"""
KG — Knowledge Graph Pipeline

Uses graphify as the engine for graph building + visualization.
We add: PDF ingestion, RDF/OWL modeling, SPARQL store, LLM Q&A.

Usage:
    python main.py ingest --input exports/my.pdf
    python main.py model --domain "engineering services"
    python main.py build --input raw/
    python main.py rdf
    python main.py import-ttl --ttl ontologies/custom.ttl
    python main.py ask "What depends on Authentication?"
    python main.py sparql "SELECT ?s ?p ?o WHERE { ?s ?p ?o } LIMIT 10"
    python main.py viz              # enhanced Graphistry-inspired explorer
    python main.py viz --basic       # graphify's default graph.html
    python main.py explore <node_id> # drill-down into a node
    python main.py god-nodes         # highest-degree nodes
    python main.py surprises         # cross-community edges
    python main.py graph-stats       # graph statistics
"""
import sys
import click
from pathlib import Path


@click.group()
def cli():
    """KG — Knowledge Graph Pipeline"""
    pass


@cli.command()
@click.option("--input", "input_path", required=True, help="PDF file or folder of PDFs")
@click.option("--out", "out_dir", default="raw", help="Output directory for markdown")
def ingest(input_path, out_dir):
    """Convert PDFs to markdown files."""
    from ingest.pdf_to_md import extract_pages, split_into_sections, save_sections
    input_path = Path(input_path)
    out_dir = Path(out_dir)
    out_dir.mkdir(parents=True, exist_ok=True)

    pdfs = [input_path] if input_path.is_file() else list(input_path.glob("*.pdf"))
    if not pdfs:
        click.echo(f"No PDFs found at {input_path}")
        return

    for pdf in pdfs:
        click.echo(f"Processing: {pdf.name}")
        pages = extract_pages(pdf)
        sections = split_into_sections(pages, pdf.stem)
        save_sections(sections, pdf, out_dir)
    click.echo(f"Done. Markdown in: {out_dir}")


@cli.command()
@click.option("--domain", required=True, help="Domain name")
@click.option("--description", default="", help="Domain description")
@click.option("--out", "out_path", default="ontologies/custom.ttl")
def model(domain, description, out_path):
    """LLM-assisted ontology modeling."""
    from model.ontology_builder import build_ontology, save_ontology
    click.echo(f"Modeling ontology for: {domain}")
    ttl = build_ontology(domain, description)
    save_ontology(ttl, Path(out_path))
    click.echo(f"Ontology saved: {out_path}")
    click.echo("Update config.yaml → ontology.custom to use it.")


@cli.command()
@click.option("--input", "input_dir", default="raw", help="Folder of markdown files")
@click.option("--out", "out_dir", default="graphify-out", help="Graphify output directory")
@click.option("--limit", default=0, help="Limit to N files (0 = all). Use for testing on large PDFs.")
@click.option("--directed/--undirected", default=True, help="Build directed graph")
def build(input_dir, out_dir, limit, directed):
    """Build knowledge graph using graphify's Python API."""
    import json
    import shutil
    from graphify.detect import detect
    from graphify.extract import extract, collect_files
    from graphify.build import build_from_json
    from graphify.cluster import cluster, score_all
    from graphify.analyze import god_nodes, surprising_connections
    from graphify.report import generate
    from graphify.export import to_json, to_html

    input_dir = Path(input_dir)
    out_dir = Path(out_dir)
    out_dir.mkdir(parents=True, exist_ok=True)

    md_files = sorted(input_dir.rglob("*.md"))
    if not md_files:
        click.echo(f"No markdown files in {input_dir}. Run 'ingest' first.")
        return

    # limit for testing
    build_dir = input_dir
    if limit > 0 and limit < len(md_files):
        build_dir = Path("raw/_subset")
        if build_dir.exists():
            shutil.rmtree(build_dir)
        build_dir.mkdir(parents=True)
        for i, f in enumerate(md_files[:limit]):
            # use \\?\ prefix for Windows long paths
            src = f"\\\\?\\{f.resolve()}"
            dst = f"\\\\?\\{(build_dir / f'doc_{i}.md').resolve()}"
            shutil.copy2(src, dst)
        click.echo(f"Using {limit}/{len(md_files)} files for build")
    else:
        click.echo(f"Building from {len(md_files)} files")

    # Step 1: Detect
    click.echo("Step 1/6: Detecting files...")
    detection = detect(build_dir)
    det_path = out_dir / ".graphify_detect.json"
    det_path.write_text(json.dumps(detection, indent=2))
    click.echo(f"  Found {detection.get('total_files', 0)} files, ~{detection.get('total_words', 0)} words")

    # Step 2: AST extract (for code files)
    click.echo("Step 2/6: AST extraction...")
    code_files = []
    for f in detection.get("files", {}).get("code", []):
        p = Path(f)
        code_files.extend(collect_files(p) if p.is_dir() else [p])
    if code_files:
        ast_result = extract(code_files, cache_root=Path("."))
    else:
        ast_result = {"nodes": [], "edges": [], "input_tokens": 0, "output_tokens": 0}
    click.echo(f"  AST: {len(ast_result['nodes'])} nodes, {len(ast_result['edges'])} edges")

    # Step 3: Semantic extraction via LLM
    click.echo("Step 3/6: Semantic extraction (LLM)...")
    doc_files = detection.get("files", {}).get("document", []) + detection.get("files", {}).get("paper", [])
    sem_nodes, sem_edges = [], []
    if doc_files:
        from llm.provider import get_llm
        from graph.extractor import EXTRACTION_PROMPT
        llm = get_llm()
        total_docs = len(doc_files)
        for i, fpath in enumerate(doc_files):
            try:
                content = Path(fpath).read_text(encoding="utf-8")
                click.echo(f"  [{i+1}/{total_docs}] {Path(fpath).name}")
                prompt = EXTRACTION_PROMPT.format(content=content[:8000])  # cap for context window
                result = llm.generate_json(prompt, system="You extract knowledge graphs from documents. Output only valid JSON.")
                for n in result.get("nodes", []):
                    n["source_file"] = fpath
                    n.setdefault("file_type", "document")
                    sem_nodes.append(n)
                sem_edges.extend(result.get("edges", []))
            except Exception as e:
                click.echo(f"  WARNING: Failed on {Path(fpath).name}: {e}")
    sem_result = {"nodes": sem_nodes, "edges": sem_edges, "input_tokens": 0, "output_tokens": 0}
    click.echo(f"  Semantic: {len(sem_nodes)} nodes, {len(sem_edges)} edges")

    # Step 4: Merge AST + semantic
    click.echo("Step 4/6: Merging & building graph...")
    seen = {n["id"] for n in ast_result["nodes"]}
    merged_nodes = list(ast_result["nodes"])
    for n in sem_nodes:
        if n["id"] not in seen:
            merged_nodes.append(n)
            seen.add(n["id"])
    merged = {
        "nodes": merged_nodes,
        "edges": ast_result["edges"] + sem_edges,
        "hyperedges": [],
        "input_tokens": 0, "output_tokens": 0,
    }
    (out_dir / ".graphify_extract.json").write_text(json.dumps(merged, indent=2))

    G = build_from_json(merged, directed=directed)
    click.echo(f"  Graph: {G.number_of_nodes()} nodes, {G.number_of_edges()} edges")

    # Step 5: Cluster
    click.echo("Step 5/6: Community detection...")
    communities = cluster(G)
    cohesion = score_all(G, communities)
    gods = god_nodes(G)
    surprises = surprising_connections(G, communities)

    # Label communities via LLM
    from llm.provider import get_llm
    llm = get_llm()
    labels = {}
    for cid, members in communities.items():
        member_labels = [G.nodes[n].get("label", n) for n in members[:15]]
        prompt = f"These concepts belong to the same cluster:\n{', '.join(member_labels)}\n\nGive a short name (2-4 words). Return ONLY the name."
        try:
            labels[cid] = llm.generate(prompt).strip().strip('"').strip("'")
        except Exception:
            labels[cid] = f"Community {cid}"
    click.echo(f"  {len(communities)} communities detected")
    for cid, name in labels.items():
        click.echo(f"    [{cid}] {name} ({len(communities[cid])} nodes)")

    # Step 6: Export
    click.echo("Step 6/6: Exporting...")
    tokens = {"input": 0, "output": 0}
    report = generate(G, communities, cohesion, labels, gods, surprises, detection, tokens, str(build_dir))
    (out_dir / "GRAPH_REPORT.md").write_text(report, encoding="utf-8")
    to_json(G, communities, str(out_dir / "graph.json"))
    to_html(G, communities, str(out_dir / "graph.html"), community_labels=labels)

    # Save analysis for other commands
    analysis = {
        "communities": {str(k): v for k, v in communities.items()},
        "cohesion": {str(k): v for k, v in cohesion.items()},
        "gods": gods, "surprises": surprises,
    }
    (out_dir / ".graphify_analysis.json").write_text(json.dumps(analysis, indent=2))
    (out_dir / ".graphify_labels.json").write_text(json.dumps({str(k): v for k, v in labels.items()}))

    click.echo(f"\nDone! Outputs in {out_dir}/")
    click.echo(f"  graph.html  - interactive visualization")
    click.echo(f"  graph.json  - raw graph data")
    click.echo(f"  GRAPH_REPORT.md - audit report")


@cli.command()
@click.option("--graph-json", default="graphify-out/graph.json", help="Path to graph.json")
@click.option("--out", "out_path", default="graphify-out/graph.ttl", help="Output .ttl path")
def rdf(graph_json, out_path):
    """Export graph.json to RDF/Turtle."""
    from graph.rdf_export import export
    graph_json = Path(graph_json)
    if not graph_json.exists():
        click.echo(f"Not found: {graph_json}. Run 'build' first.")
        return
    export(graph_json, Path(out_path))


@cli.command("import-ttl")
@click.option("--ttl", "ttl_path", required=True, help=".ttl file or folder")
def import_ttl(ttl_path):
    """Import .ttl files into the SPARQL store."""
    from store.sparql_store import SPARQLStore
    p = Path(ttl_path)
    store = SPARQLStore()
    if p.is_file():
        store.load_ttl(p)
    elif p.is_dir():
        for f in p.glob("*.ttl"):
            store.load_ttl(f)
    click.echo(f"Loaded {store.count()} triples")


@cli.command()
@click.argument("question")
@click.option("--ttl", default="graphify-out/graph.ttl", help="Path to .ttl file")
def ask(question, ttl):
    """Ask a natural language question about the knowledge graph."""
    from store.sparql_store import SPARQLStore
    from llm.provider import get_llm
    from agent.qa_engine import QAEngine

    ttl_path = Path(ttl)
    if not ttl_path.exists():
        click.echo(f"Not found: {ttl_path}. Run 'rdf' first.")
        return

    store = SPARQLStore()
    store.load_ttl(ttl_path)
    # also load any custom ontologies
    for f in Path("ontologies").glob("*.ttl"):
        store.load_ttl(f)

    llm = get_llm()
    engine = QAEngine(store, llm)
    answer = engine.ask(question)
    click.echo(f"\n{answer}")


@cli.command()
@click.argument("query")
@click.option("--ttl", default="graphify-out/graph.ttl", help="Path to .ttl file")
def sparql(query, ttl):
    """Run a raw SPARQL query."""
    from store.sparql_store import SPARQLStore
    store = SPARQLStore()
    store.load_ttl(Path(ttl))
    for f in Path("ontologies").glob("*.ttl"):
        store.load_ttl(f)

    results = store.query(query)
    if not results:
        click.echo("No results.")
        return
    for row in results:
        click.echo(" | ".join(f"{k}: {v}" for k, v in row.items()))


@cli.command()
@click.option("--enhanced/--basic", default=True, help="Use enhanced Graphistry-inspired viz")
def viz(enhanced):
    """Open graph visualization. --basic for graphify's default, --enhanced for our explorer."""
    import webbrowser
    if enhanced:
        graph_json = Path("graphify-out/graph.json")
        if not graph_json.exists():
            click.echo("graph.json not found. Run 'build' first.")
            return
        from viz.graph_viz import generate_enhanced_html
        out = Path("graphify-out/kg-explorer.html")
        generate_enhanced_html(graph_json, out)
        webbrowser.open(str(out.resolve()))
    else:
        html = Path("graphify-out/graph.html")
        if not html.exists():
            click.echo("graph.html not found. Run 'build' first.")
            return
        webbrowser.open(str(html.resolve()))


@cli.command()
@click.argument("node_id")
@click.option("--hops", default=2, help="Number of hops to expand")
def explore(node_id, hops):
    """Drill down into a node — show N-hop neighborhood."""
    from graph.explorer import GraphExplorer
    gj = Path("graphify-out/graph.json")
    if not gj.exists():
        click.echo("graph.json not found. Run 'build' first.")
        return
    ex = GraphExplorer(gj)
    result = ex.expand(node_id, hops)
    click.echo(f"\n{len(result['nodes'])} nodes within {hops} hops of '{node_id}':")
    for nid, attrs in result["nodes"].items():
        click.echo(f"  {attrs.get('label', nid)} [{attrs.get('type', '')}]")


@cli.command("god-nodes")
@click.option("--top", default=10)
def god_nodes(top):
    """Show highest-degree nodes."""
    from graph.explorer import GraphExplorer
    gj = Path("graphify-out/graph.json")
    if not gj.exists():
        click.echo("graph.json not found. Run 'build' first.")
        return
    ex = GraphExplorer(gj)
    for n in ex.god_nodes(top):
        click.echo(f"  [{n['degree']}] {n['label']} ({n['type']})")


@cli.command("surprises")
def surprises():
    """Show cross-community edges — the surprising connections."""
    from graph.explorer import GraphExplorer
    gj = Path("graphify-out/graph.json")
    if not gj.exists():
        click.echo("graph.json not found. Run 'build' first.")
        return
    ex = GraphExplorer(gj)
    for e in ex.cross_community_edges():
        click.echo(f"  {e['source_label']} ({e['source_community']}) --[{e['relation']}]--> {e['target_label']} ({e['target_community']})")


@cli.command("explorer")
@click.option("--ttl", default="graphify-out/graph.ttl", help="Path to .ttl file")
@click.option("--port", default=8899, help="Port")
def explorer_cmd(ttl, port):
    """Launch KG Explorer — WebGL graph visualization + LLM chat."""
    from explorer.server import load_ttl, app
    import uvicorn, webbrowser
    ttl_path = Path(ttl)
    if not ttl_path.exists():
        click.echo(f"Not found: {ttl_path}. Run 'rdf' first.")
        return
    load_ttl(str(ttl_path))
    click.echo(f"\n  🔬 KG Explorer → http://127.0.0.1:{port}\n")
    webbrowser.open(f"http://127.0.0.1:{port}")
    uvicorn.run(app, host="127.0.0.1", port=port, log_level="warning")


@cli.command("graph-stats")
def graph_stats():
    """Show graph statistics."""
    from graph.explorer import GraphExplorer
    gj = Path("graphify-out/graph.json")
    if not gj.exists():
        click.echo("graph.json not found. Run 'build' first.")
        return
    ex = GraphExplorer(gj)
    s = ex.stats()
    click.echo(f"Nodes: {s['nodes']}  Edges: {s['edges']}")
    click.echo(f"Types: {s['types']}")
    click.echo(f"Communities: {s['communities']}")
    click.echo(f"Relations: {s['relations']}")


if __name__ == "__main__":
    cli()
