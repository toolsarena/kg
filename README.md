# KG — Knowledge Graph Pipeline

Ingest PDFs → Build knowledge graph (via graphify) → RDF/Turtle → SPARQL store → LLM Q&A

## Architecture

```
graphify (engine)          → graph.json, graph.html, GRAPH_REPORT.md
  ↓
rdf_export                 → graph.ttl (RDF/Turtle)
  ↓
sparql_store (rdflib)      → in-memory SPARQL endpoint
  ↓
qa_engine + sparql_agent   → LLM answers questions via direct context or agentic SPARQL
```

**What graphify does:** graph building, community detection, vis-network visualization, CLI query/path/explain
**What we add:** PDF ingestion, RDF/OWL ontology modeling, SPARQL store, LLM Q&A with agentic SPARQL

## Setup

```bash
pip install -r requirements.txt
# Ensure Ollama is running with qwen2.5-coder:7b
ollama pull qwen2.5-coder:7b
```

## Usage

```bash
# 1. Ingest PDFs → markdown
python main.py ingest --input exports/my-space.pdf

# 2. Model custom ontology (LLM-assisted)
python main.py model --domain "engineering services" --description "microservices architecture"

# 3. Build knowledge graph (graphify)
python main.py build --input raw/

# 4. Export to RDF/Turtle
python main.py rdf

# 5. Open visualization (graphify's graph.html)
python main.py viz

# 6. Ask questions (LLM + SPARQL)
python main.py ask "What services depend on Authentication?"

# 7. Raw SPARQL
python main.py sparql "SELECT ?s ?p ?o WHERE { ?s ?p ?o } LIMIT 10"

# 8. Import your own .ttl
python main.py import-ttl --ttl ontologies/my_domain.ttl
```

## Config

Edit `config.yaml` to change LLM provider, model, ontology paths.
