"""
Batch RDF builder with LLM extraction.
Processes markdown files in batches, saves TTL after each batch.
Resumes from where it left off. Works with any LLM provider (Bedrock/Ollama).

Usage:
    python batch_build.py                    # process all, resume if interrupted
    python batch_build.py --batch-size 50    # custom batch size
    python batch_build.py --reset            # start fresh
    python batch_build.py --dry-run          # show what would be processed
"""
import json
import re
import time
import click
from pathlib import Path
from rdflib import Graph as RDFGraph, Namespace, Literal, URIRef, RDF, RDFS
from rdflib.namespace import SKOS, DCTERMS, OWL

KG = Namespace("http://kg.local/ontology#")
KGR = Namespace("http://kg.local/resource/")

RAW_DIR = Path("raw/consolidated")
OUT_TTL = Path("graphify-out/graph.ttl")
PROGRESS_FILE = Path("graphify-out/.llm_batch_progress.json")
BASE_ONTOLOGY = Path("model/templates/base_ontology.ttl")

EDGE_MAP = {
    "depends_on": DCTERMS.requires,
    "relates_to": SKOS.related,
    "owned_by": DCTERMS.contributor,
    "uses": KG.uses,
    "implements": KG.implements,
    "part_of": SKOS.broader,
    "recommends": KG.recommends,
    "mitigates": KG.mitigates,
}

TYPE_MAP = {
    "concept": KG.Concept,
    "service": KG.Service,
    "decision": KG.Decision,
    "team": KG.Team,
    "process": KG.Process,
    "best_practice": KG.BestPractice,
    "pillar": KG.Pillar,
    "role": KG.Role,
    "technology": KG.Concept,
}

EXTRACTION_PROMPT = """Read this document and extract ALL entities and relationships.

DOCUMENT:
---
{content}
---

Extract as JSON:
{{"nodes": [{{"id": "snake_case_id", "label": "Human Name", "type": "concept|service|decision|process|best_practice|role", "description": "one line"}}], "edges": [{{"source": "node_id", "target": "node_id", "relation": "depends_on|relates_to|uses|implements|part_of|recommends|mitigates"}}]}}

Rules:
- Extract EVERY named system, service, concept, best practice, process
- Use consistent snake_case IDs (a-z0-9_ only)
- For AWS services use: aws_lambda, amazon_cloudwatch, etc.
- For WA pillars: operational_excellence, security, reliability, performance_efficiency, cost_optimization, sustainability
- Return ONLY valid JSON."""


def init_graph():
    g = RDFGraph()
    g.bind("kg", KG)
    g.bind("kgr", KGR)
    g.bind("skos", SKOS)
    g.bind("dcterms", DCTERMS)
    if BASE_ONTOLOGY.exists():
        g.parse(str(BASE_ONTOLOGY), format="turtle")
    return g


def add_extraction_to_graph(g, result, source_file):
    for node in result.get("nodes", []):
        nid = re.sub(r'[^a-z0-9_]', '_', node.get("id", "").lower().strip())[:80]
        if not nid:
            continue
        uri = KGR[nid]
        ntype = node.get("type", "concept")
        g.add((uri, RDF.type, TYPE_MAP.get(ntype, KG.Concept)))
        g.add((uri, SKOS.prefLabel, Literal(node.get("label", nid))))
        if node.get("description"):
            g.add((uri, RDFS.comment, Literal(node["description"])))
        g.add((uri, DCTERMS.source, Literal(source_file)))

    for edge in result.get("edges", []):
        src = re.sub(r'[^a-z0-9_]', '_', edge.get("source", "").lower())[:80]
        tgt = re.sub(r'[^a-z0-9_]', '_', edge.get("target", "").lower())[:80]
        if not src or not tgt:
            continue
        rel = edge.get("relation", "relates_to")
        pred = EDGE_MAP.get(rel, SKOS.related)
        g.add((KGR[src], pred, KGR[tgt]))


def load_progress():
    if PROGRESS_FILE.exists():
        return json.loads(PROGRESS_FILE.read_text())
    return {"processed_files": [], "total_extracted": 0, "errors": []}


def save_progress(progress):
    PROGRESS_FILE.write_text(json.dumps(progress, indent=2))


@click.command()
@click.option("--batch-size", default=30, help="Files per batch")
@click.option("--reset", is_flag=True, help="Start fresh, ignore previous progress")
@click.option("--dry-run", is_flag=True, help="Show what would be processed")
@click.option("--max-batches", default=0, help="Stop after N batches (0=all)")
def main(batch_size, reset, dry_run, max_batches):
    all_files = sorted([f for f in RAW_DIR.iterdir() if f.suffix == ".md"])
    click.echo(f"Total files: {len(all_files)}")

    progress = {"processed_files": [], "total_extracted": 0, "errors": []} if reset else load_progress()
    done = set(progress["processed_files"])
    remaining = [f for f in all_files if f.name not in done]
    click.echo(f"Already done: {len(done)}, remaining: {len(remaining)}")

    if dry_run:
        for f in remaining[:batch_size]:
            click.echo(f"  Would process: {f.name}")
        return

    from llm.provider import get_llm
    llm = get_llm()

    # Load existing TTL or start fresh
    g = init_graph()
    if not reset and OUT_TTL.exists() and len(done) > 0:
        g.parse(str(OUT_TTL), format="turtle")
        click.echo(f"Loaded existing: {len(g)} triples")

    batch_count = 0
    for i in range(0, len(remaining), batch_size):
        batch = remaining[i:i + batch_size]
        batch_count += 1
        batch_extracted = 0
        click.echo(f"\n--- Batch {batch_count}: {len(batch)} files ---")

        for j, filepath in enumerate(batch):
            try:
                text = filepath.read_text(encoding="utf-8", errors="ignore")
                content = text[:6000]  # cap for context window
                click.echo(f"  [{j+1}/{len(batch)}] {filepath.name}", nl=False)

                prompt = EXTRACTION_PROMPT.format(content=content)
                result = llm.generate_json(
                    prompt,
                    system="You extract knowledge graphs from documents. Output only valid JSON."
                )

                n_nodes = len(result.get("nodes", []))
                n_edges = len(result.get("edges", []))
                add_extraction_to_graph(g, result, filepath.name)
                batch_extracted += n_nodes + n_edges
                click.echo(f" → {n_nodes}n {n_edges}e")

            except Exception as e:
                click.echo(f" → ERROR: {e}")
                progress["errors"].append({"file": filepath.name, "error": str(e)})

            progress["processed_files"].append(filepath.name)
            # small delay to avoid rate limits
            time.sleep(0.1)

        # Save after each batch
        g.serialize(str(OUT_TTL), format="turtle")
        progress["total_extracted"] += batch_extracted
        save_progress(progress)
        click.echo(f"  Saved: {len(g)} triples total | +{batch_extracted} this batch ✓")

        if max_batches and batch_count >= max_batches:
            click.echo(f"\nStopped after {max_batches} batches")
            break

    click.echo(f"\nDone! {len(progress['processed_files'])}/{len(all_files)} files → {len(g)} triples")
    if progress["errors"]:
        click.echo(f"Errors: {len(progress['errors'])} (see {PROGRESS_FILE})")


if __name__ == "__main__":
    main()
