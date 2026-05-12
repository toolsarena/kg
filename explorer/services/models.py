"""Data models for the data population feature."""
from dataclasses import dataclass, field, asdict
from typing import Any
import json
import time
import uuid


@dataclass
class ColumnInfo:
    """Metadata about a single dataset column."""
    name: str
    inferred_type: str  # "string", "integer", "float", "boolean", "date", "uri"
    sample_values: list[str] = field(default_factory=list)  # up to 5 sample values
    null_count: int = 0


@dataclass
class DatasetPreview:
    """Preview of a parsed dataset."""
    source_type: str  # "csv", "json_array", "json_object", "xml"
    columns: list[ColumnInfo] = field(default_factory=list)
    row_count: int = 0
    sample: list[dict] = field(default_factory=list)  # up to 10 rows
    filename: str | None = None


@dataclass
class OntologyClass:
    """An OWL class extracted from a TTL file."""
    uri: str
    label: str
    local_name: str  # fragment after # or last /


@dataclass
class OntologyProperty:
    """An OWL property (object or datatype) extracted from a TTL file."""
    uri: str
    label: str
    local_name: str
    domain: str | None = None  # class URI or None if unrestricted
    range: str | None = None   # class URI or XSD type


@dataclass
class OntologySchema:
    """Complete schema extracted from an ontology TTL file."""
    classes: list[OntologyClass] = field(default_factory=list)
    object_properties: list[OntologyProperty] = field(default_factory=list)
    datatype_properties: list[OntologyProperty] = field(default_factory=list)


@dataclass
class ColumnMapping:
    """Mapping of a single column to an ontology property."""
    column_name: str
    mapped_property: str | None = None  # ontology property URI, None if unmapped
    mapping_type: str = "unmapped"  # "datatype", "object", "skip", "unmapped"
    confidence: float = 0.0  # 0.0 to 1.0
    target_class: str | None = None  # for object properties, the target class


@dataclass
class MappingSuggestion:
    """A suggested mapping from dataset columns to ontology."""
    target_class: str  # ontology class URI
    id_column: str
    label_column: str
    column_mappings: list[ColumnMapping] = field(default_factory=list)


@dataclass
class ConfirmedMapping:
    """A user-confirmed mapping, persisted as JSON."""
    id: str = field(default_factory=lambda: str(uuid.uuid4()))
    project_id: str = ""
    ontology_file: str = ""
    target_class: str = ""
    id_column: str = ""
    label_column: str = ""
    column_mappings: list[ColumnMapping] = field(default_factory=list)
    created_at: float = field(default_factory=time.time)
    dataset_columns: list[str] = field(default_factory=list)

    def to_json(self) -> str:
        """Serialize to JSON string."""
        data = {
            "id": self.id,
            "project_id": self.project_id,
            "ontology_file": self.ontology_file,
            "target_class": self.target_class,
            "id_column": self.id_column,
            "label_column": self.label_column,
            "column_mappings": [
                {
                    "column_name": cm.column_name,
                    "mapped_property": cm.mapped_property,
                    "mapping_type": cm.mapping_type,
                    "confidence": cm.confidence,
                    "target_class": cm.target_class,
                }
                for cm in self.column_mappings
            ],
            "created_at": self.created_at,
            "dataset_columns": self.dataset_columns,
        }
        return json.dumps(data, indent=2)

    @classmethod
    def from_json(cls, json_str: str) -> "ConfirmedMapping":
        """Deserialize from JSON string."""
        data = json.loads(json_str)
        column_mappings = [
            ColumnMapping(
                column_name=cm["column_name"],
                mapped_property=cm.get("mapped_property"),
                mapping_type=cm.get("mapping_type", "unmapped"),
                confidence=cm.get("confidence", 0.0),
                target_class=cm.get("target_class"),
            )
            for cm in data.get("column_mappings", [])
        ]
        return cls(
            id=data["id"],
            project_id=data["project_id"],
            ontology_file=data["ontology_file"],
            target_class=data["target_class"],
            id_column=data["id_column"],
            label_column=data["label_column"],
            column_mappings=column_mappings,
            created_at=data["created_at"],
            dataset_columns=data.get("dataset_columns", []),
        )


@dataclass
class PopulationSession:
    """Tracks the full lifecycle of a data population operation."""
    session_id: str = field(default_factory=lambda: str(uuid.uuid4()))
    project_id: str = ""
    dataset: DatasetPreview | None = None
    ontology: OntologySchema | None = None
    mapping: ConfirmedMapping | None = None
    data_rows: list[dict] = field(default_factory=list)
    db_endpoint: str | None = None
    created_at: float = field(default_factory=time.time)


@dataclass
class GenerationResult:
    """Result of RDF instance generation."""
    ttl: str = ""  # generated Turtle content
    instances_created: int = 0
    instances_updated: int = 0  # for incremental loads
    triples_generated: int = 0
    rows_skipped: int = 0  # rows with missing identifier
    skipped_reasons: list[str] = field(default_factory=list)


@dataclass
class PushResult:
    """Result of pushing triples to Neptune."""
    success: bool = False
    total_triples: int = 0
    triples_pushed: int = 0
    batches_completed: int = 0
    total_batches: int = 0
    failed_batch: int | None = None  # batch index that failed, for retry
    error: str | None = None


@dataclass
class ConnectionStatus:
    """Result of a database connection attempt."""
    connected: bool = False
    message: str = ""
    endpoint: str = ""


@dataclass
class TabularResult:
    """Tabular result from a SPARQL query."""
    columns: list[str] = field(default_factory=list)
    rows: list[dict] = field(default_factory=list)
    row_count: int = 0


@dataclass
class ValidationResult:
    """Result of mapping validation."""
    valid: bool = True
    errors: list[str] = field(default_factory=list)
    warnings: list[str] = field(default_factory=list)


@dataclass
class MergeResult:
    """Result of incremental instance merging."""
    new_instances: int = 0
    updated_instances: int = 0
    triples_added: int = 0
