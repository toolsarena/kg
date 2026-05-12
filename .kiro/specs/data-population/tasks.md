# Implementation Plan: Data Population

## Overview

This plan implements the data population feature for KG Studio, enabling users to upload datasets (CSV, JSON, XML), connect to SPARQL/Neptune endpoints, map columns to ontology classes/properties with LLM assistance, generate RDF instances, and export or push the populated graph. The implementation follows the existing FastAPI router pattern and uses rdflib for all RDF operations.

## Tasks

- [ ] 1. Set up data models and service scaffolding
  - [ ] 1.1 Create data model definitions in `explorer/services/models.py`
    - Define all dataclasses: `DatasetPreview`, `ColumnInfo`, `OntologySchema`, `OntologyClass`, `OntologyProperty`, `MappingSuggestion`, `ColumnMapping`, `ConfirmedMapping`, `PopulationSession`, `GenerationResult`, `PushResult`, `ConnectionStatus`, `TabularResult`, `ValidationResult`, `MergeResult`
    - Include type annotations and default values as specified in the design
    - Add JSON serialization/deserialization methods to `ConfirmedMapping` for file persistence
    - _Requirements: 1.1, 1.2, 4.1, 6.7, 9.3_

  - [ ] 1.2 Create `explorer/services/__init__.py` and service stubs
    - Create the `explorer/services/` directory with `__init__.py`
    - Create stub files for `dataset_connector.py`, `mapping_service.py`, `instance_generator.py`, `export_service.py` with class skeletons and method signatures
    - _Requirements: 1.1, 2.1, 4.1, 6.1, 9.1_

- [ ] 2. Implement Dataset Connector
  - [ ] 2.1 Implement CSV parsing in `explorer/services/dataset_connector.py`
    - Implement `parse_csv(content: bytes) -> DatasetPreview` method
    - Detect encoding (UTF-8 default, reject unsupported encodings with descriptive error)
    - Parse headers, infer column types from sample values (string, integer, float, boolean, date, uri)
    - Return column headers, row count, sample of up to 10 rows, null counts per column
    - Enforce 50 MB file size limit with appropriate error response
    - _Requirements: 1.1, 1.5, 1.6_

  - [ ]* 2.2 Write property tests for CSV parsing
    - **Property 1: CSV parsing returns accurate metadata**
    - **Validates: Requirements 1.1**

  - [ ] 2.3 Implement JSON parsing in `explorer/services/dataset_connector.py`
    - Implement `parse_json(content: bytes) -> DatasetPreview` for JSON arrays of objects
    - Implement `flatten_json(obj: dict, prefix: str = "") -> dict` for nested objects using dot-notation keys
    - Handle both array-of-objects and single nested object formats
    - Infer types from values, return field names, record count, sample of up to 10 records
    - _Requirements: 1.2, 1.3, 1.6_

  - [ ]* 2.4 Write property tests for JSON parsing and flattening
    - **Property 2: JSON array parsing returns accurate metadata**
    - **Property 3: JSON flattening preserves all leaf values**
    - **Validates: Requirements 1.2, 1.3**

  - [ ] 2.5 Implement XML parsing in `explorer/services/dataset_connector.py`
    - Implement `parse_xml(content: bytes) -> DatasetPreview`
    - Convert XML elements and attributes into a tabular representation
    - Return field names, record count, and sample of up to 10 records
    - _Requirements: 1.4, 1.6_

  - [ ]* 2.6 Write property tests for error handling
    - **Property 4: Invalid input produces descriptive errors without crashes**
    - **Validates: Requirements 1.6**

  - [ ] 2.7 Implement database connection methods in `explorer/services/dataset_connector.py`
    - Implement `connect_neptune(endpoint: str, port: int) -> ConnectionStatus` with 10-second timeout
    - Implement `connect_sparql(endpoint_url: str) -> ConnectionStatus` with test query validation
    - Implement `execute_query(session_id: str, query: str) -> TabularResult` for SPARQL queries
    - Ensure error messages never expose credentials (sanitize passwords/tokens from error strings)
    - _Requirements: 2.1, 2.2, 2.3, 2.4, 2.5_

  - [ ]* 2.8 Write property tests for SPARQL result formatting and credential masking
    - **Property 5: SPARQL results are correctly formatted as tabular data**
    - **Property 6: Error messages never expose credentials**
    - **Validates: Requirements 2.3, 2.4**

- [ ] 3. Checkpoint - Ensure all tests pass
  - Ensure all tests pass, ask the user if questions arise.

- [ ] 4. Implement Mapping Service
  - [ ] 4.1 Implement ontology schema extraction in `explorer/services/mapping_service.py`
    - Implement method to parse a TTL file and extract all OWL classes, object properties, datatype properties with their domains and ranges
    - Return `OntologySchema` with complete class/property information
    - Handle TTL files with no OWL classes (return warning)
    - _Requirements: 3.1, 3.2, 3.3_

  - [ ]* 4.2 Write property test for ontology extraction
    - **Property 7: Ontology extraction is complete**
    - **Validates: Requirements 3.1, 3.2**

  - [ ] 4.3 Implement LLM-assisted mapping suggestion in `explorer/services/mapping_service.py`
    - Implement `suggest_mapping(columns, sample, ontology) -> MappingSuggestion` using `llm_manager.generate_json()`
    - Build prompt with column names, sample data, ontology class labels, and property domain/range constraints
    - Parse LLM response into `MappingSuggestion` with confidence scores in [0.0, 1.0]
    - Assign target class, id_column, label_column, and column_mappings for every input column
    - _Requirements: 4.1, 4.2, 4.3_

  - [ ] 4.4 Implement heuristic fallback mapping in `explorer/services/mapping_service.py`
    - Implement `heuristic_mapping(columns, ontology) -> MappingSuggestion` using string similarity
    - Implement `compute_similarity(col_name, property_label) -> float` using normalized edit distance or token overlap
    - Prioritize exact case-insensitive matches with higher confidence
    - Mark columns with no reasonable match as "unmapped"
    - _Requirements: 4.4, 4.5, 4.6_

  - [ ]* 4.5 Write property tests for mapping suggestions
    - **Property 8: Mapping suggestions contain all required fields and valid confidence scores**
    - **Property 9: Higher similarity yields higher confidence**
    - **Property 10: Heuristic fallback produces valid mappings**
    - **Property 11: Unmapped columns are flagged**
    - **Validates: Requirements 4.1, 4.3, 4.4, 4.5, 4.6**

  - [ ] 4.6 Implement mapping validation in `explorer/services/mapping_service.py`
    - Implement `validate_mapping(mapping, ontology) -> ValidationResult`
    - Check that assigned properties belong to the domain of the target class or have no domain restriction
    - Detect stale references (classes/properties no longer in ontology)
    - _Requirements: 5.4, 10.4_

  - [ ]* 4.7 Write property tests for mapping validation
    - **Property 12: Skipped columns produce no triples**
    - **Property 13: Domain validation rejects invalid assignments**
    - **Property 24: Stale mapping references are flagged**
    - **Validates: Requirements 5.3, 5.4, 10.4**

- [ ] 5. Checkpoint - Ensure all tests pass
  - Ensure all tests pass, ask the user if questions arise.

- [ ] 6. Implement Instance Generator
  - [ ] 6.1 Implement core instance generation in `explorer/services/instance_generator.py`
    - Implement `generate(data, mapping, base_uri, existing_graph) -> GenerationResult`
    - Create one RDF named individual per data row, typed to the mapped ontology class
    - Implement `build_uri(base_uri, identifier) -> URIRef` for unique URI generation
    - Implement `create_typed_literal(value, datatype) -> Literal` for XSD-typed literals
    - Skip rows with missing identifier values, omit triples for empty/null cells
    - Produce valid Turtle syntax parseable by rdflib
    - Report instances_created, triples_generated, rows_skipped with reasons
    - _Requirements: 6.1, 6.2, 6.3, 6.4, 6.5, 6.6, 6.7_

  - [ ]* 6.2 Write property tests for instance generation
    - **Property 14: Instance generation produces correct count and valid RDF**
    - **Property 15: Generated URIs are unique for unique identifiers**
    - **Property 16: Triple generation matches mapping type**
    - **Validates: Requirements 6.1, 6.2, 6.3, 6.4, 6.5, 6.6, 6.7**

  - [ ] 6.3 Implement incremental loading in `explorer/services/instance_generator.py`
    - Implement `merge_instances(existing, new) -> MergeResult`
    - Preserve all existing instances and triples when loading additional data
    - Merge new triples into existing instances when identifier matches (no duplicates)
    - Report new instances created, existing instances updated, total triples added
    - _Requirements: 7.1, 7.2, 7.3_

  - [ ]* 6.4 Write property tests for incremental loading
    - **Property 17: Incremental loading preserves existing triples**
    - **Property 18: Duplicate identifiers merge rather than duplicate**
    - **Validates: Requirements 7.1, 7.2**

- [ ] 7. Implement Export Service
  - [ ] 7.1 Implement multi-format export in `explorer/services/export_service.py`
    - Implement `export_graph(graph, format) -> bytes` supporting Turtle, N-Triples, and JSON-LD
    - Ensure export contains both ontology schema and generated instances
    - _Requirements: 9.1, 9.2_

  - [ ]* 7.2 Write property test for export completeness
    - **Property 19: Export contains both schema and instances**
    - **Validates: Requirements 9.2**

  - [ ] 7.3 Implement Neptune push with batching in `explorer/services/export_service.py`
    - Implement `push_to_neptune(graph, endpoint, batch_size, start_batch) -> PushResult`
    - Implement `create_batches(graph, batch_size) -> list[list[tuple]]` with max 1000 triples per batch
    - Support retry from a specific failed batch index
    - Report total triples pushed, batches completed, and failed batch info
    - _Requirements: 9.3, 9.4, 9.5_

  - [ ]* 7.4 Write property tests for batching and retry
    - **Property 20: Neptune push batches never exceed 1000 triples**
    - **Property 21: Failed batch retry resumes correctly**
    - **Validates: Requirements 9.3, 9.5**

- [ ] 8. Checkpoint - Ensure all tests pass
  - Ensure all tests pass, ask the user if questions arise.

- [ ] 9. Implement Population API Router
  - [ ] 9.1 Create `explorer/routes/population.py` with dataset upload and database connection endpoints
    - Create the router with `APIRouter(prefix="/api/population", tags=["population"])`
    - Implement `POST /upload-dataset` — accept file upload, delegate to DatasetConnector, return DatasetPreview
    - Implement `POST /connect-database` — accept endpoint config, delegate to DatasetConnector
    - Implement `POST /query-database` — execute SPARQL query on connected endpoint
    - Manage in-memory `PopulationSession` objects keyed by session_id
    - _Requirements: 1.1, 1.2, 1.4, 1.5, 1.6, 2.1, 2.2, 2.3, 2.4, 2.5_

  - [ ] 9.2 Add ontology selection and mapping endpoints to `explorer/routes/population.py`
    - Implement `GET /{project_id}/ontologies` — list TTL files with class/property counts
    - Implement `POST /{project_id}/select-ontology` — parse TTL, extract schema, store in session
    - Implement `POST /{project_id}/suggest-mapping` — delegate to MappingService, return suggestion
    - Implement `POST /{project_id}/confirm-mapping` — validate and persist mapping as JSON file
    - _Requirements: 3.1, 3.2, 3.3, 4.1, 4.2, 4.3, 5.1, 5.2, 5.3, 5.4, 5.5_

  - [ ] 9.3 Add instance generation and export endpoints to `explorer/routes/population.py`
    - Implement `POST /{project_id}/generate-instances` — delegate to InstanceGenerator, save TTL file
    - Implement `POST /{project_id}/export` — delegate to ExportService, return file download
    - Implement `POST /{project_id}/push-neptune` — delegate to ExportService for batch push
    - Implement `POST /{project_id}/push-neptune/retry` — retry from failed batch
    - _Requirements: 6.1, 6.7, 7.1, 7.3, 7.4, 9.1, 9.2, 9.3, 9.4, 9.5_

  - [ ] 9.4 Add mapping management endpoints to `explorer/routes/population.py`
    - Implement `GET /{project_id}/sessions` — list active population sessions
    - Implement `GET /{project_id}/mappings` — list saved mappings for project
    - Implement `GET /{project_id}/mappings/{mapping_id}` — view a saved mapping
    - Implement `DELETE /{project_id}/mappings/{mapping_id}` — delete a saved mapping
    - Detect matching column headers for mapping reuse suggestion
    - _Requirements: 10.1, 10.2, 10.3, 10.4_

  - [ ]* 9.5 Write property tests for mapping persistence
    - **Property 22: Mapping serialization round-trip**
    - **Property 23: Mapping reuse suggested on matching headers**
    - **Validates: Requirements 10.1, 10.2**

- [ ] 10. Register router and wire components together
  - [ ] 10.1 Register the population router in `explorer/server.py`
    - Import and include the population router in the FastAPI app
    - Pass `llm_manager` to the MappingService constructor
    - Ensure all service dependencies are properly wired
    - _Requirements: 1.1, 2.1, 4.1, 6.1, 9.1_

  - [ ]* 10.2 Write integration tests in `tests/test_population_api.py`
    - Test full workflow: upload dataset → select ontology → suggest mapping → confirm → generate → export
    - Test error cases: oversized file, invalid format, LLM unavailable fallback
    - Test session lifecycle and mapping reuse detection
    - Use httpx `AsyncClient` with the FastAPI test client
    - _Requirements: 1.1, 1.5, 1.6, 4.5, 6.7, 9.2, 10.2_

- [ ] 11. Final checkpoint - Ensure all tests pass
  - Ensure all tests pass, ask the user if questions arise.

## Notes

- Tasks marked with `*` are optional and can be skipped for faster MVP
- Each task references specific requirements for traceability
- Checkpoints ensure incremental validation
- Property tests validate universal correctness properties from the design document
- Unit tests validate specific examples and edge cases
- The existing `explorer/routes/mapper.py` provides a simpler one-shot mapping; the new population module is a more robust session-based workflow
- All services use `rdflib` for RDF operations, consistent with the existing codebase
- The `llm_manager` from `explorer/server.py` is reused for LLM-assisted mapping

## Task Dependency Graph

```json
{
  "waves": [
    { "id": 0, "tasks": ["1.1", "1.2"] },
    { "id": 1, "tasks": ["2.1", "2.3", "2.5", "2.7"] },
    { "id": 2, "tasks": ["2.2", "2.4", "2.6", "2.8", "4.1"] },
    { "id": 3, "tasks": ["4.2", "4.3", "4.4"] },
    { "id": 4, "tasks": ["4.5", "4.6"] },
    { "id": 5, "tasks": ["4.7", "6.1"] },
    { "id": 6, "tasks": ["6.2", "6.3", "7.1", "7.3"] },
    { "id": 7, "tasks": ["6.4", "7.2", "7.4"] },
    { "id": 8, "tasks": ["9.1", "9.2", "9.3", "9.4"] },
    { "id": 9, "tasks": ["9.5", "10.1"] },
    { "id": 10, "tasks": ["10.2"] }
  ]
}
```
