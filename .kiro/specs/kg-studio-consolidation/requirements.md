# Requirements Document

## Introduction

KG Studio is a full-stack knowledge graph platform. The core user flow is: upload/ingest documents → extract entities → model ontology via LLM chat → build & visualize → query (SPARQL agent or context Q&A). This spec consolidates the codebase to make that flow reliable and clean, without breaking existing functionality.

## Glossary

- **Server**: The FastAPI web application in `explorer/server.py`.
- **Studio**: The full UI at `/studio` with Ingest, Model, and Explore tabs.
- **Project**: An isolated workspace containing one or more ontology (.ttl) files.
- **Active_Ontology**: The ontology file the user is currently working on within a project.
- **LLM_Provider**: The abstraction in `llm/provider.py` for calling Ollama/Bedrock/OpenAI.
- **Explorer**: The WebGL force-graph visualization at `/` or embedded in Studio's Explore tab.
- **SPARQL_Agent_Mode**: LLM generates SPARQL queries to answer questions from the graph.
- **Context_QA_Mode**: LLM answers questions using graph neighborhood as context (no SPARQL generation).
- **Merge_and_Build**: User action that merges their new/active ontology with existing project ontologies and rebuilds the visualization.

## Requirements

### Requirement 1: Document Ingestion Flow

**User Story:** As a user, I want to upload documents (PDF, CSV, JSON, TTL, text) and have entities extracted, so that I have a starting point for building my ontology.

#### Acceptance Criteria

1. WHEN a user uploads a file via the Ingest tab, THE system SHALL extract entities using pattern matching (current "old gen" regex extraction) and display them as a preview.
2. WHEN extraction completes, THE system SHALL present the extracted entities to the user for review before committing.
3. WHEN the user confirms extracted entities, THE system SHALL generate TTL and save it as a new file in the user's active project.
4. AFTER committing entities, THE system SHALL navigate the user to the Model tab with the newly created ontology file as the Active_Ontology.
5. THE system SHALL support uploading multiple files in sequence, each producing a separate ontology file within the same project.

### Requirement 2: Model Tab — LLM Ontology Chat

**User Story:** As a user, I want to chat with an LLM to create and refine my RDF ontology, so that I can build a proper knowledge model without writing TTL by hand.

#### Acceptance Criteria

1. WHEN the user is on the Model tab, THE system SHALL show the Active_Ontology (the file they are currently working on).
2. IF the user uploaded/ingested a file, THEN the Active_Ontology SHALL be that file's extracted TTL.
3. THE user SHALL be able to chat with the LLM to add classes, properties, relationships, and instances to the Active_Ontology.
4. WHEN the LLM proposes ontology changes, THE system SHALL update the Active_Ontology TTL in real-time and show a live preview.
5. THE user SHALL be able to switch between ontology files within the same project without losing work on any file.
6. WHEN the user switches files, THE system SHALL save the current Active_Ontology state before switching.

### Requirement 3: Multi-Ontology Project Structure

**User Story:** As a user, I want each project to hold multiple ontology files, so that I can build domain models incrementally and keep them organized.

#### Acceptance Criteria

1. EACH project SHALL support multiple .ttl files, each representing an independent ontology.
2. THE Model tab SHALL display a list of all ontology files in the current project.
3. THE user SHALL be able to create a new empty ontology file within a project.
4. THE user SHALL be able to upload an existing .ttl file directly into a project.
5. WHEN viewing the file list, THE system SHALL indicate which file is the Active_Ontology (currently being edited).
6. Old ontologies SHALL remain accessible and unmodified unless the user explicitly edits or merges them.

### Requirement 4: Build and Visualize

**User Story:** As a user, I want to build and view my ontology as an interactive graph, so that I can see the structure I'm creating.

#### Acceptance Criteria

1. WHEN the user clicks "Build" or "View", THE system SHALL parse the Active_Ontology and render it in the Explorer (WebGL force-graph).
2. THE Explorer SHALL show nodes colored by type and edges labeled by relationship.
3. THE Explorer SHALL support drill-down (click node → expand neighbors), search, and path-finding.
4. THE visualization SHALL only show the Active_Ontology's content (not merged with other files) unless the user explicitly merges.

### Requirement 5: Merge and Build

**User Story:** As a user, I want to merge my new ontology with existing project ontologies and visualize the combined graph, so that I can see how everything connects.

#### Acceptance Criteria

1. WHEN the user clicks "Merge and Build", THE system SHALL combine the Active_Ontology with all other .ttl files in the project (or a user-selected subset).
2. THE merged graph SHALL be rendered in the Explorer showing the full combined ontology.
3. THE merge SHALL NOT modify the individual source .ttl files — it produces a read-only combined view.
4. THE system SHALL save the merged result as a separate file (e.g., `merged.ttl`) in the project for export purposes.
5. IF there are conflicting triples (same subject-predicate with different objects), THE system SHALL include both and let the user resolve later.

### Requirement 6: Explorer Query Modes

**User Story:** As a user, I want to ask questions about my graph in two ways — SPARQL agent mode and context Q&A mode — so that I can query structured data or get natural language answers.

#### Acceptance Criteria

1. THE Explorer SHALL provide two query modes accessible from the chat interface: SPARQL Agent Mode and Context QA Mode.
2. IN SPARQL_Agent_Mode, THE system SHALL use the LLM to generate SPARQL queries, execute them against the loaded graph, and present formatted results.
3. IN Context_QA_Mode, THE system SHALL pull relevant graph neighborhood as context and have the LLM answer the question directly without generating SPARQL.
4. THE user SHALL be able to switch between modes from the UI.
5. WHEN the LLM is unavailable, THE system SHALL fall back to showing raw graph context (neighbors, types) without crashing.

### Requirement 7: Unified LLM Layer

**User Story:** As a developer, I want a single LLM calling mechanism used by both server and CLI, so that config changes apply everywhere.

#### Acceptance Criteria

1. THE Server SHALL use `llm/provider.py` for all LLM calls instead of the inline `call_llm()` function.
2. THE Server SHALL remove the duplicated `call_llm()` and `llm_config` dict from `explorer/server.py`.
3. WHEN LLM settings are changed via the UI, THE system SHALL update the provider instance used for subsequent calls.
4. THE LLM_Provider SHALL load initial settings from `config.yaml` at startup.
5. THE LLM_Provider SHALL load API keys from environment variables (with `.env` fallback via python-dotenv).

### Requirement 8: Complete Dependency Manifest

**User Story:** As a developer, I want all dependencies listed in requirements.txt, so that the project installs cleanly.

#### Acceptance Criteria

1. THE requirements.txt SHALL include: fastapi, uvicorn, python-multipart, networkx, boto3, graphifyy, pdfplumber, rdflib, pyyaml, requests, click, python-slugify, python-dotenv.
2. WHEN `pip install -r requirements.txt` runs in a clean environment, ALL imports across the codebase SHALL resolve.
3. A separate `requirements-dev.txt` SHALL include: pytest, httpx, pytest-asyncio.

### Requirement 9: Move Dead Files to Backups

**User Story:** As a developer, I want dead HTML files moved out of the active static directory into a backups folder, so that the codebase is clean but nothing is lost.

#### Acceptance Criteria

1. THE following files SHALL be moved from `explorer/static/` to `explorer/static/backups/`: `studio_broken.html`, `studio_v2_broken.html`, `studio_all_backups.html`, `studio_before_changes.html`, `index_backup.html`, `view_new_backup.html`.
2. THE `backups/` folder SHALL NOT be served by the static file mount (or shall be excluded from the main static route).
3. THE active routes (`/`, `/studio`, `/view-new`) SHALL continue working after the move.

### Requirement 10: Basic Test Coverage

**User Story:** As a developer, I want automated tests for core functionality, so that refactoring doesn't break things silently.

#### Acceptance Criteria

1. THE test suite SHALL include unit tests for: LLM provider selection, Graph Explorer (expand, search, path), SPARQLStore (load, query).
2. THE test suite SHALL include an integration test that starts the server and verifies `/api/stats` returns valid JSON.
3. THE test suite SHALL use pytest.
4. Tests SHALL be runnable with `pytest` from the project root.
