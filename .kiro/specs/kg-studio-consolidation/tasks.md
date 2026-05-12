# Implementation Plan: KG Studio Consolidation

## Overview

This plan consolidates the KG Studio codebase to make the core flow reliable: Ingest → Model → Build → Explore/Query. The implementation proceeds in layers: unified LLM first (since everything depends on it), then wiring the flow end-to-end, then cleanup and tests.

## Tasks

- [x] 1. Unified LLM Layer
  - [x] 1.1 Create `LLMProviderManager` class in `llm/provider.py`
    - Add `LLMProviderManager` with `generate()`, `generate_json()`, and `reconfigure()` methods
    - Load initial config from `config.yaml` with `.env` overlay via `python-dotenv`
    - Ensure `load_dotenv()` is called at module load
    - _Requirements: 7.1, 7.4, 7.5_

  - [x] 1.2 Replace inline `call_llm()` in `explorer/server.py` with `llm_manager`
    - Instantiate `LLMProviderManager` at module level in `server.py`
    - Remove the `call_llm()` function and `llm_config` dict
    - Update `/api/llm/config` GET/POST endpoints to delegate to `llm_manager.reconfigure()`
    - _Requirements: 7.1, 7.2, 7.3_

  - [x] 1.3 Migrate all route files to use `llm_manager`
    - Update `routes/rdf_agent.py`: replace `from explorer.server import call_llm` with `from explorer.server import llm_manager`
    - Update `routes/model.py`: same migration
    - Update `routes/mapper.py`: same migration
    - Update `routes/ingest.py`: same migration (if it uses `call_llm`)
    - Replace all `call_llm(prompt, system=...)` calls with `llm_manager.generate(prompt, system=...)`
    - _Requirements: 7.1, 7.2_

  - [x] 1.4 Wire agent layer to shared LLM provider
    - Update `explorer/server.py` to pass `llm_manager.provider` to `QAEngine` and `SPARQLAgent`
    - Ensure `qa_engine` is re-initialized when graph is loaded
    - _Requirements: 7.1, 6.2, 6.3_

- [x] 2. Checkpoint — Ensure LLM layer works
  - Ensure all tests pass, ask the user if questions arise.

- [x] 3. Ingest → Model Flow Wiring
  - [x] 3.1 Update `routes/ingest.py` commit endpoint to save to project
    - Add `project_id` and `filename` parameters to the commit request body
    - When `project_id` is provided, save generated TTL to `projects/{project_id}/{filename}`
    - Auto-generate filename if not provided (e.g., `ingest_{timestamp}.ttl`)
    - Return `saved_to` and `project_id` in response
    - _Requirements: 1.3, 1.5, 3.1_

  - [x] 3.2 Update `routes/model.py` conversation endpoint to be project-aware
    - Add `project_id` and `active_file` parameters to the conversation request body
    - When generating/updating TTL, save to `projects/{project_id}/{active_file}`
    - _Requirements: 2.1, 2.3, 2.4_

  - [x] 3.3 Update `studio.html` frontend to track `activeOntology` state
    - Add `currentProject` and `activeOntology` JavaScript state variables
    - Pass `project_id` and `active_file` in Model tab API calls
    - After ingest commit, navigate to Model tab with new file as `activeOntology`
    - Show file list in Model tab sidebar with active indicator
    - Implement file switching with auto-save of current state
    - _Requirements: 1.4, 2.1, 2.2, 2.5, 2.6, 3.2, 3.5_

  - [ ]* 3.4 Write property test for entity extraction (Property 1)
    - **Property 1: Entity extraction produces well-formed output**
    - Generate random text with headings, CSV rows, and JSON schemas
    - Verify extraction returns non-empty `entities` list with valid `id` and `label` fields
    - **Validates: Requirements 1.1**

  - [ ]* 3.5 Write property test for commit round-trip (Property 2)
    - **Property 2: Commit round-trip produces valid TTL**
    - Generate random entity dicts with varying types/labels/relationships
    - Verify commit produces parseable Turtle RDF with at least one triple per entity
    - **Validates: Requirements 1.3**

- [x] 4. Multi-Ontology Project Structure
  - [x] 4.1 Add project file management endpoints to `routes/projects.py`
    - Add `POST /api/projects/{id}/files` — create new empty .ttl file
    - Add `POST /api/projects/{id}/upload` — upload existing .ttl file into project
    - Ensure `GET /api/projects/{id}` returns full file list with metadata
    - _Requirements: 3.1, 3.3, 3.4_

  - [x] 4.2 Add `merge-and-build` endpoint to `routes/projects.py`
    - Implement `POST /api/projects/{id}/merge-and-build` as designed
    - Merge selected files (or all) using rdflib, save as `merged.ttl`
    - Build graph for visualization (populate nodes/edges)
    - Return merge stats (triples, nodes, edges, source_files)
    - _Requirements: 5.1, 5.2, 5.3, 5.4, 5.5_

  - [ ]* 4.3 Write property test for multi-file project integrity (Property 3)
    - **Property 3: Multi-file project integrity**
    - Generate N random valid TTL strings, save as separate files
    - Verify listing returns exactly N entries, each parsing independently
    - **Validates: Requirements 3.1, 3.2, 3.4**

  - [ ]* 4.4 Write property test for file immutability (Property 4)
    - **Property 4: File immutability invariant**
    - Create project with files A and B, perform operations on A only
    - Verify B remains byte-for-byte identical
    - **Validates: Requirements 3.6, 5.3**

  - [ ]* 4.5 Write property test for merge completeness (Property 6)
    - **Property 6: Merge preserves all source triples**
    - Generate N valid TTL files, merge them
    - Verify merged triple count >= max individual count and all source triples exist in result
    - **Validates: Requirements 5.1, 5.5**

- [x] 5. Checkpoint — Ensure ingest and project flow works
  - Ensure all tests pass, ask the user if questions arise.

- [x] 6. Build and Visualize
  - [x] 6.1 Ensure build endpoint produces typed graph structure
    - Verify `POST /api/projects/{id}/build` with `{"filename": "..."}` populates nodes/edges
    - Ensure every node has a non-empty `type` field and every edge has a non-empty `relation` field
    - Wire build result to Explorer frontend (nodes/edges data)
    - _Requirements: 4.1, 4.2, 4.3_

  - [x] 6.2 Update `studio.html` Explore tab to support build and merge-and-build
    - Add "Build" button that builds Active_Ontology only
    - Add "Merge & Build" button that calls merge-and-build endpoint
    - Render resulting graph in embedded Explorer (force-graph)
    - Ensure visualization only shows Active_Ontology unless user merges
    - _Requirements: 4.1, 4.4, 5.1, 5.2_

  - [ ]* 6.3 Write property test for build structure (Property 5)
    - **Property 5: Build produces typed graph structure**
    - Generate random TTL with classes and instances
    - Verify build produces nodes with `type` and edges with `relation`
    - **Validates: Requirements 4.1, 4.2**

- [x] 7. Explorer Query Modes
  - [x] 7.1 Formalize SPARQL Agent and Context QA endpoints
    - Ensure `POST /api/ask/sparql` uses `llm_manager.generate()` for SPARQL generation
    - Ensure `POST /api/ask` and `POST /api/ask/project` use `llm_manager.generate()` for context QA
    - Verify fallback behavior when LLM is unreachable (return raw context, HTTP 200)
    - _Requirements: 6.1, 6.2, 6.3, 6.5_

  - [x] 7.2 Update Explorer chat UI for mode switching
    - Add mode toggle (SPARQL Agent / Context QA) in chat interface
    - Route requests to appropriate endpoint based on selected mode
    - _Requirements: 6.1, 6.4_

  - [ ]* 7.3 Write property test for context retrieval (Property 7)
    - **Property 7: Context QA retrieves relevant neighborhood**
    - Generate graphs with known nodes, ask questions containing node labels
    - Verify context includes the node's label and at least one direct neighbor
    - **Validates: Requirements 6.3**

  - [ ]* 7.4 Write property test for LLM fallback (Property 8)
    - **Property 8: Graceful LLM fallback**
    - Configure broken LLM, send random questions
    - Verify HTTP 200 with non-empty `context` or `answer` field, no 5xx
    - **Validates: Requirements 6.5**

- [x] 8. Checkpoint — Ensure query modes work
  - Ensure all tests pass, ask the user if questions arise.

- [x] 9. Cleanup and Dependencies
  - [x] 9.1 Move dead HTML files to `explorer/static/backups/`
    - Create `explorer/static/backups/` directory
    - Move: `studio_broken.html`, `studio_v2_broken.html`, `studio_all_backups.html`, `studio_before_changes.html`, `index_backup.html`, `view_new_backup.html`
    - Verify active routes (`/`, `/studio`, `/view-new`) still work
    - _Requirements: 9.1, 9.2, 9.3_

  - [x] 9.2 Create/update `requirements.txt` and `requirements-dev.txt`
    - Write `requirements.txt` with: fastapi, uvicorn[standard], python-multipart, networkx, boto3, graphifyy, pdfplumber, rdflib, pyyaml, requests, click, python-slugify, python-dotenv
    - Write `requirements-dev.txt` with: pytest, httpx, pytest-asyncio, hypothesis
    - _Requirements: 8.1, 8.2, 8.3_

  - [x] 9.3 Create `.env.example` and update `.gitignore`
    - Create `.env.example` with template keys (OPENAI_API_KEY, AWS_DEFAULT_REGION, AWS_PROFILE)
    - Add `.env` to `.gitignore`
    - _Requirements: 7.5_

- [x] 10. Unit and Integration Tests
  - [x] 10.1 Write unit tests for LLM provider selection and reconfiguration
    - Test `get_llm()` returns correct provider class for each config (ollama, bedrock, openai)
    - Test `LLMProviderManager.reconfigure()` switches provider type
    - _Requirements: 7.1, 10.1_

  - [x] 10.2 Write unit tests for Graph Explorer (expand, search, path)
    - Test expand from known node returns subgraph
    - Test search by label returns matching nodes
    - _Requirements: 10.1_

  - [x] 10.3 Write unit tests for SPARQLStore (load, query)
    - Test loading TTL into store
    - Test running SPARQL query returns expected results
    - _Requirements: 10.1_

  - [ ]* 10.4 Write integration test for server startup and `/api/stats`
    - Start app with httpx AsyncClient
    - GET `/api/stats`, verify JSON response with expected keys
    - _Requirements: 10.2_

- [x] 11. Final Checkpoint — Ensure all tests pass
  - Ensure all tests pass, ask the user if questions arise.

## Notes

- Tasks marked with `*` are optional and can be skipped for faster MVP
- Each task references specific requirements for traceability
- Checkpoints ensure incremental validation
- Property tests validate universal correctness properties from the design document
- Unit tests validate specific examples and edge cases
- The design uses Python (FastAPI + pytest + hypothesis) throughout
- All LLM migration is mechanical (find/replace `call_llm` → `llm_manager.generate`)

## Task Dependency Graph

```json
{
  "waves": [
    { "id": 0, "tasks": ["1.1"] },
    { "id": 1, "tasks": ["1.2", "9.1", "9.2", "9.3"] },
    { "id": 2, "tasks": ["1.3", "1.4"] },
    { "id": 3, "tasks": ["3.1", "3.2", "4.1"] },
    { "id": 4, "tasks": ["3.3", "3.4", "3.5", "4.2"] },
    { "id": 5, "tasks": ["4.3", "4.4", "4.5", "6.1"] },
    { "id": 6, "tasks": ["6.2", "6.3", "7.1"] },
    { "id": 7, "tasks": ["7.2", "7.3", "7.4"] },
    { "id": 8, "tasks": ["10.1", "10.2", "10.3"] },
    { "id": 9, "tasks": ["10.4"] }
  ]
}
```
