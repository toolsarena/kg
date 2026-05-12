# Requirements Document

## Introduction

This feature adds data population capabilities to KG Studio. Users who have already built an ontology (TTL file with classes, properties, and relationships) can now populate that ontology with actual data instances from real datasets. The system provides LLM-assisted mapping from dataset columns/fields to ontology classes and properties, generates RDF instances, and supports visualization, export, and incremental loading of the populated graph.

## Glossary

- **Data_Population_Engine**: The backend system responsible for ingesting datasets, managing mappings, generating RDF instances, and coordinating export operations.
- **Mapping_Service**: The component that uses LLM assistance to suggest and manage column-to-ontology mappings.
- **Instance_Generator**: The component that transforms data rows into RDF triples based on confirmed mappings.
- **Dataset_Connector**: The component responsible for connecting to and reading data from external sources (files or databases).
- **Ontology**: A TTL file containing OWL classes, properties, and relationships that defines the schema/model for a knowledge graph.
- **Mapping**: A configuration that associates dataset columns/fields with ontology classes and properties.
- **Instance**: An RDF individual (named resource) that is a member of an ontology class, created from a data row.
- **Population_Session**: A stateful session tracking the dataset, ontology, mapping, and generated instances for a single population operation.

## Requirements

### Requirement 1: Dataset File Upload

**User Story:** As a knowledge engineer, I want to upload CSV, JSON, or XML data files, so that I can use their contents to populate my ontology with instances.

#### Acceptance Criteria

1. WHEN a user uploads a CSV file, THE Dataset_Connector SHALL parse the file and return column headers, data types, row count, and a sample of up to 10 rows.
2. WHEN a user uploads a JSON file containing an array of objects, THE Dataset_Connector SHALL parse the file and return field names, inferred data types, record count, and a sample of up to 10 records.
3. WHEN a user uploads a JSON file containing a nested object, THE Dataset_Connector SHALL flatten the structure to one level using dot-notation keys and return the resulting field names.
4. WHEN a user uploads an XML file, THE Dataset_Connector SHALL parse elements and attributes into a tabular representation and return field names, record count, and a sample of up to 10 records.
5. IF a file exceeds 50 MB in size, THEN THE Dataset_Connector SHALL reject the upload and return an error message indicating the maximum file size.
6. IF a file cannot be parsed due to encoding or format errors, THEN THE Dataset_Connector SHALL return a descriptive error message identifying the parsing failure.

### Requirement 2: Database Connection

**User Story:** As a knowledge engineer, I want to connect to Neptune or a SPARQL endpoint, so that I can pull existing data to populate or extend my ontology instances.

#### Acceptance Criteria

1. WHEN a user provides a Neptune cluster endpoint and port, THE Dataset_Connector SHALL establish a connection and confirm connectivity within 10 seconds.
2. WHEN a user provides a SPARQL endpoint URL, THE Dataset_Connector SHALL validate the endpoint by executing a test query and return the connection status.
3. WHEN a database connection is established, THE Dataset_Connector SHALL allow the user to execute a SPARQL query and return results as tabular data with column headers and rows.
4. IF a connection attempt fails due to network or authentication errors, THEN THE Dataset_Connector SHALL return a descriptive error message without exposing credentials.
5. WHILE a database connection is active, THE Dataset_Connector SHALL reuse the connection for subsequent queries within the same Population_Session.

### Requirement 3: Ontology Selection for Population

**User Story:** As a knowledge engineer, I want to select which ontology file from my project to populate, so that the mapping targets the correct schema.

#### Acceptance Criteria

1. WHEN a user initiates data population for a project, THE Data_Population_Engine SHALL list all TTL files in the project with their class count and property count.
2. WHEN a user selects an ontology file, THE Data_Population_Engine SHALL parse the file and extract all OWL classes, object properties, datatype properties, and their domains and ranges.
3. IF the selected TTL file contains no OWL classes, THEN THE Data_Population_Engine SHALL display a warning indicating the file has no classes to populate.

### Requirement 4: LLM-Assisted Column-to-Ontology Mapping

**User Story:** As a knowledge engineer, I want the system to suggest how my dataset columns map to ontology classes and properties, so that I can quickly configure the data transformation without manual effort.

#### Acceptance Criteria

1. WHEN a dataset and ontology are both loaded, THE Mapping_Service SHALL generate a suggested mapping within 15 seconds that includes: a target class for each row, an identifier column, a label column, datatype property assignments, and object property assignments.
2. THE Mapping_Service SHALL use the column names, sample data values, ontology class labels, and property domain/range constraints to determine mapping suggestions.
3. WHEN the Mapping_Service generates a suggestion, THE Mapping_Service SHALL assign a confidence score between 0 and 1 to each column mapping.
4. WHEN a column name or sample values closely match an ontology property label or class label, THE Mapping_Service SHALL prioritize that mapping over less similar alternatives.
5. IF the LLM is unavailable, THEN THE Mapping_Service SHALL fall back to a heuristic mapping based on string similarity between column names and ontology property labels.
6. WHEN a dataset contains columns that do not match any ontology property, THE Mapping_Service SHALL mark those columns as "unmapped" in the suggestion.

### Requirement 5: User Mapping Confirmation and Adjustment

**User Story:** As a knowledge engineer, I want to review, adjust, and confirm the suggested mapping before generating instances, so that I maintain control over data quality.

#### Acceptance Criteria

1. WHEN a mapping suggestion is presented, THE Data_Population_Engine SHALL allow the user to change the target class for any column.
2. WHEN a mapping suggestion is presented, THE Data_Population_Engine SHALL allow the user to reassign any column to a different ontology property.
3. WHEN a mapping suggestion is presented, THE Data_Population_Engine SHALL allow the user to mark any column as "skip" to exclude it from instance generation.
4. WHEN a user modifies a mapping, THE Data_Population_Engine SHALL validate that the assigned property belongs to the domain of the target class or has no domain restriction.
5. WHEN a user confirms the mapping, THE Data_Population_Engine SHALL persist the mapping configuration within the Population_Session for reuse.

### Requirement 6: RDF Instance Generation

**User Story:** As a knowledge engineer, I want the system to generate RDF instances from my data rows based on the confirmed mapping, so that my ontology is populated with real data.

#### Acceptance Criteria

1. WHEN a user triggers instance generation with a confirmed mapping, THE Instance_Generator SHALL create one RDF named individual per data row, typed to the mapped ontology class.
2. THE Instance_Generator SHALL generate a unique URI for each instance using the project base URI and the value from the designated identifier column.
3. WHEN a column is mapped to a datatype property, THE Instance_Generator SHALL create a triple with the instance as subject, the property as predicate, and the cell value as a typed literal.
4. WHEN a column is mapped to an object property, THE Instance_Generator SHALL create a triple linking the instance to a target resource URI derived from the cell value.
5. WHEN a cell value is empty or null, THE Instance_Generator SHALL omit the corresponding triple rather than creating a triple with an empty literal.
6. THE Instance_Generator SHALL produce valid Turtle (TTL) syntax that can be parsed by any RDF-compliant parser without errors.
7. WHEN instance generation completes, THE Instance_Generator SHALL report the total number of instances created, total triples generated, and any rows skipped due to missing identifier values.

### Requirement 7: Incremental Data Loading

**User Story:** As a knowledge engineer, I want to add more data to an already-populated graph without losing existing instances, so that I can build up my knowledge graph over time.

#### Acceptance Criteria

1. WHEN a user loads additional data into a project that already contains instance data, THE Data_Population_Engine SHALL preserve all existing instances and triples.
2. WHEN a new data row has the same identifier value as an existing instance, THE Data_Population_Engine SHALL merge new triples into the existing instance rather than creating a duplicate.
3. WHEN incremental loading completes, THE Data_Population_Engine SHALL report the count of new instances created, existing instances updated, and total triples added.
4. THE Data_Population_Engine SHALL allow the user to reuse a previously confirmed mapping for the same dataset structure without re-running the mapping suggestion step.

### Requirement 8: Populated Graph Visualization

**User Story:** As a knowledge engineer, I want to visualize the populated graph showing both schema classes and data instances, so that I can verify the population results and explore relationships.

#### Acceptance Criteria

1. WHEN a populated graph is built, THE Data_Population_Engine SHALL render instances as nodes visually distinct from ontology class nodes using different colors or shapes.
2. WHEN a populated graph is displayed, THE Data_Population_Engine SHALL show rdf:type edges linking instances to their ontology classes.
3. WHEN a user clicks on an instance node, THE Data_Population_Engine SHALL display all datatype property values and object property links for that instance.
4. WHEN a populated graph contains more than 500 instance nodes, THE Data_Population_Engine SHALL apply clustering by class type and allow the user to expand individual clusters.
5. THE Data_Population_Engine SHALL support the existing three visualization views (nodes, mind map, tree) for populated graphs.

### Requirement 9: Export and Push to Neptune

**User Story:** As a knowledge engineer, I want to export the populated graph as RDF or push it directly to a Neptune endpoint, so that I can use the data in production systems.

#### Acceptance Criteria

1. WHEN a user requests export, THE Data_Population_Engine SHALL offer export in Turtle (TTL), N-Triples, and JSON-LD formats.
2. WHEN a user selects an export format, THE Data_Population_Engine SHALL generate a downloadable file containing both the ontology schema and all generated instances.
3. WHEN a user provides a Neptune SPARQL endpoint for push, THE Data_Population_Engine SHALL upload the generated triples using SPARQL INSERT operations in batches of no more than 1000 triples per request.
4. WHEN a push to Neptune completes, THE Data_Population_Engine SHALL report the total triples pushed and confirm successful insertion.
5. IF a push to Neptune fails mid-operation, THEN THE Data_Population_Engine SHALL report which batch failed, how many triples were successfully pushed, and allow the user to retry from the failed batch.

### Requirement 10: Mapping Persistence and Reuse

**User Story:** As a knowledge engineer, I want to save my confirmed mappings so that I can reapply them when new data arrives with the same structure.

#### Acceptance Criteria

1. WHEN a user confirms a mapping, THE Data_Population_Engine SHALL save the mapping configuration as a JSON file within the project directory.
2. WHEN a user uploads a new dataset with column headers matching a saved mapping, THE Data_Population_Engine SHALL suggest reusing the saved mapping.
3. THE Data_Population_Engine SHALL allow the user to list, view, and delete saved mappings for a project.
4. WHEN a saved mapping references ontology classes or properties that no longer exist in the current ontology, THE Data_Population_Engine SHALL flag those references as invalid and prompt the user to update the mapping.
