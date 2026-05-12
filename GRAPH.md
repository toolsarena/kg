# KG Studio — Project Status

## What We Built

### 1. Knowledge Graph Pipeline (core)
- **PDF Ingestion** → markdown chunking → LLM extraction → RDF/Turtle
- **RDF Export** → graphify's graph.json → proper OWL/SKOS triples
- **SPARQL Store** → rdflib in-memory, queryable
- **LLM Q&A** → Context mode + SPARQL Agent mode
- **Providers** → Ollama (local), Bedrock (ready), OpenAI (ready)

### 2. Well-Architected Framework Graph
- **2973 triples** manually modeled from 132 source documents
- **763 unique entities**: 275 Concepts, 232 Best Practices, 86 Services, 9 Processes, 6 Pillars
- All 6 pillars fully covered with cross-pillar relationships
- Anti-patterns with `mitigates` links to best practices
- DR strategies with RPO/RTO detail
- WA Questions → Best Practice mappings

### 3. TMF SID Ontology
- Downloaded **988 JSON schemas** from TMF Forum GitHub
- Modeled proper ontology from actual schemas (382 triples)
- Domains: Customer, Product, Service, Resource, EngagedParty, Common, Trouble/Alarm
- Real `$ref` relationships, inheritance hierarchy, property descriptions
- Project saved at `projects/tmf_sid/model.ttl`

### 4. KG Explorer (visualization)
- **WebGL force-graph** (GPU auto-detect, Canvas fallback for CPU)
- **Deep drill-down** — click nodes, accumulates path, hop slider 1-15
- **Search** — fuzzy search across all nodes
- **Path Finder** — BFS shortest path between any two nodes
- **Type Filters** — toggle node types on/off
- **Stats / God Nodes** — most connected nodes, type distribution
- **Legend** — color-coded by domain
- **LLM Chat** — Context Q&A + SPARQL Agent
- **LLM Settings** — configure Ollama/Bedrock/OpenAI from UI (provider, model, URL, temperature, test connection)
- **Auto-coloring** — nodes colored by domain automatically from ontology

### 5. KG Studio (full app)
- **Ingest tab** — upload PDF, CSV, JSON, TTL, text. Multi-file support. Entity extraction preview.
- **Model tab** — 3 paths:
  - Path A: LLM conversation (co-pilot for ontology building)
  - Path B: Upload/paste TTL directly
  - Path C: Visual canvas (drag-drop classes, AI suggest, live TTL preview)
- **Explore tab** — embedded full explorer
- **Project system** — create/select/save projects, each isolated
- **Build Graph** — one button: saves to project → builds → opens premium viewer

### 6. Data Downloaded
- `uploads/tmf_sid/` — 988 TMF SID JSON schemas (6 domains)
- `uploads/tmf_docs/` — 11 TMF API README docs
- `uploads/real_data/fcc_providers_2000.json` — 2000 real US telecom providers
- `uploads/real_data/fcc_broadband_providers.csv` — 418 rows
- `uploads/real_data/nyc_311_requests.csv` — 171 service requests
- `uploads/bt_group.json` — BT Group corporate structure
- `uploads/tmf_sid_data.csv` — sample TMF SID instance data

---

## Architecture

```
kg/
├── explorer/                    # KG Studio + Explorer app
│   ├── server.py               # FastAPI backend (all APIs)
│   ├── __main__.py             # python -m explorer
│   ├── routes/
│   │   ├── ingest.py           # File upload, extraction, commit
│   │   ├── model.py            # TTL validate, merge, LLM conversation, canvas-to-ttl
│   │   ├── export.py           # Download TTL/CSV/JSON-LD
│   │   └── projects.py         # Project CRUD, save, build
│   └── static/
│       ├── index.html          # Original explorer (chat, drill-down, SPARQL)
│       ├── studio.html         # Full studio (Ingest/Model/Explore tabs)
│       ├── view_new.html       # Premium graph viewer (per-project)
│       ├── force-graph.min.js  # Local WebGL lib (no CDN needed)
│       └── 3d-force-graph.min.js
├── llm/
│   ├── provider.py             # Abstract LLM provider
│   ├── ollama.py               # Ollama (local)
│   └── bedrock.py              # AWS Bedrock (ready for access)
├── graph/
│   ├── extractor.py            # LLM extraction prompt
│   ├── rdf_export.py           # graph.json → TTL
│   └── explorer.py             # NetworkX graph operations
├── store/
│   └── sparql_store.py         # rdflib SPARQL wrapper
├── agent/
│   ├── qa_engine.py            # LLM Q&A with graph context
│   ├── sparql_agent.py         # LLM generates SPARQL
│   └── prompts.py              # All system prompts
├── ingest/
│   ├── pdf_to_md.py            # PDF → markdown sections
│   ├── consolidate.py          # Merge small sections
│   ├── build_rdf_direct.py     # Pattern-matching RDF builder (no LLM)
│   └── ttl_import.py           # Import .ttl files
├── model/
│   └── ontology_builder.py     # LLM-assisted ontology generation
├── projects/                    # User projects (isolated)
│   └── tmf_sid/
│       └── model.ttl           # TMF SID ontology
├── graphify-out/
│   ├── graph.ttl               # Main graph (WA Framework, 2973 triples)
│   ├── graph.json              # Graphify format
│   └── graph.html              # Graphify default viz
├── uploads/                     # Uploaded/downloaded data
│   ├── tmf_sid/                # 988 TMF JSON schemas
│   ├── tmf_docs/               # TMF README docs
│   ├── real_data/              # FCC, NYC 311 data
│   └── bt_group.json           # BT Group data
├── batch_build.py              # LLM batch processor (for Bedrock)
├── config.yaml                 # LLM config (provider, model, temp)
├── main.py                     # CLI (ingest, build, rdf, ask, sparql, explorer)
└── requirements.txt
```

---

## How to Run

```bash
cd c:\Users\615418931\kg

# Start the full app
python -m explorer --ttl graphify-out/graph.ttl

# URLs:
# http://127.0.0.1:8899         → Explorer (graph + chat)
# http://127.0.0.1:8899/studio  → Full Studio (Ingest/Model/Explore)
# http://127.0.0.1:8899/view-new?project=tmf_sid → Project viewer
```

---

## Next Steps (Tomorrow)

1. **Map to Ontology** — CSV columns → ontology classes mapping UI
2. **Ingest real data** — FCC 2000 providers into TMF SID ontology
3. **skills.md** — agentic modeling with domain-specific instructions
4. **3D mode** — when GPU arrives
5. **Git-like versioning** — project history, diff, rollback
6. **Collaboration** — multi-user, branching, merge
