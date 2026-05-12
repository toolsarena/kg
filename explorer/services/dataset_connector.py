"""Dataset Connector — parses uploaded files and connects to SPARQL endpoints."""
import csv
import io
import json
import re
import xml.etree.ElementTree as ET
from typing import Any

import requests

from explorer.services.models import (
    ColumnInfo,
    ConnectionStatus,
    DatasetPreview,
    TabularResult,
)

MAX_FILE_SIZE = 50 * 1024 * 1024  # 50 MB


def _infer_type(values: list[str]) -> str:
    """Infer column type from sample values."""
    if not values:
        return "string"

    non_empty = [v for v in values if v and v.strip()]
    if not non_empty:
        return "string"

    # Check URI
    if all(re.match(r'^https?://', v) for v in non_empty):
        return "uri"

    # Check boolean
    if all(v.lower() in ("true", "false", "yes", "no", "1", "0") for v in non_empty):
        return "boolean"

    # Check integer
    try:
        for v in non_empty:
            int(v)
        return "integer"
    except (ValueError, TypeError):
        pass

    # Check float
    try:
        for v in non_empty:
            float(v)
        return "float"
    except (ValueError, TypeError):
        pass

    # Check date patterns
    date_pattern = re.compile(r'^\d{4}[-/]\d{1,2}[-/]\d{1,2}')
    if all(date_pattern.match(v) for v in non_empty):
        return "date"

    return "string"


def _sanitize_error(message: str, *credentials: str) -> str:
    """Remove any credential values from error messages."""
    result = message
    for cred in credentials:
        if cred and len(cred) > 0:
            result = result.replace(cred, "***")
    return result


class DatasetConnector:
    """Parses uploaded files and connects to external data sources."""

    def parse_csv(self, content: bytes) -> DatasetPreview:
        """Parse CSV content and return a preview with metadata."""
        if len(content) > MAX_FILE_SIZE:
            raise ValueError("File exceeds maximum size of 50 MB")

        try:
            text = content.decode("utf-8")
        except UnicodeDecodeError:
            raise ValueError("File encoding not supported. Use UTF-8.")

        try:
            reader = csv.DictReader(io.StringIO(text))
            headers = reader.fieldnames or []
            if not headers:
                raise ValueError("Could not parse file as CSV: no headers found")

            all_rows = []
            for row in reader:
                all_rows.append(dict(row))

            row_count = len(all_rows)
            sample = all_rows[:10]

            # Build column info
            columns = []
            for header in headers:
                col_values = [row.get(header, "") for row in all_rows]
                non_empty = [v for v in col_values if v and v.strip()]
                sample_vals = non_empty[:5]
                null_count = sum(1 for v in col_values if not v or not v.strip())
                inferred = _infer_type(non_empty[:20])
                columns.append(ColumnInfo(
                    name=header,
                    inferred_type=inferred,
                    sample_values=sample_vals,
                    null_count=null_count,
                ))

            return DatasetPreview(
                source_type="csv",
                columns=columns,
                row_count=row_count,
                sample=sample,
            )
        except ValueError:
            raise
        except Exception as e:
            raise ValueError(f"Could not parse file as CSV: {e}")

    def parse_json(self, content: bytes) -> DatasetPreview:
        """Parse JSON content and return a preview with metadata."""
        if len(content) > MAX_FILE_SIZE:
            raise ValueError("File exceeds maximum size of 50 MB")

        try:
            text = content.decode("utf-8")
        except UnicodeDecodeError:
            raise ValueError("File encoding not supported. Use UTF-8.")

        try:
            data = json.loads(text)
        except json.JSONDecodeError as e:
            raise ValueError(f"Could not parse file as JSON: {e}")

        if isinstance(data, list):
            if not data:
                raise ValueError("Could not parse file as JSON: empty array")
            # Flatten each object if nested
            flat_rows = [self.flatten_json(item) if isinstance(item, dict) else {"value": item} for item in data]
            row_count = len(flat_rows)
            sample = flat_rows[:10]

            # Collect all field names across all rows
            all_fields = []
            seen = set()
            for row in flat_rows:
                for key in row.keys():
                    if key not in seen:
                        seen.add(key)
                        all_fields.append(key)

            columns = []
            for field_name in all_fields:
                col_values = [str(row.get(field_name, "")) for row in flat_rows]
                non_empty = [v for v in col_values if v and v.strip()]
                sample_vals = non_empty[:5]
                null_count = sum(1 for row in flat_rows if field_name not in row or row[field_name] is None or row[field_name] == "")
                inferred = _infer_type(non_empty[:20])
                columns.append(ColumnInfo(
                    name=field_name,
                    inferred_type=inferred,
                    sample_values=sample_vals,
                    null_count=null_count,
                ))

            return DatasetPreview(
                source_type="json_array",
                columns=columns,
                row_count=row_count,
                sample=sample,
            )

        elif isinstance(data, dict):
            # Single nested object — flatten with dot-notation
            flat = self.flatten_json(data)
            columns = []
            for key, value in flat.items():
                val_str = str(value) if value is not None else ""
                inferred = _infer_type([val_str] if val_str else [])
                columns.append(ColumnInfo(
                    name=key,
                    inferred_type=inferred,
                    sample_values=[val_str] if val_str else [],
                    null_count=0 if val_str else 1,
                ))

            return DatasetPreview(
                source_type="json_object",
                columns=columns,
                row_count=1,
                sample=[flat],
            )
        else:
            raise ValueError("Could not parse file as JSON: expected array or object")

    def flatten_json(self, obj: dict, prefix: str = "") -> dict:
        """Flatten a nested JSON object using dot-notation keys."""
        result = {}
        for key, value in obj.items():
            full_key = f"{prefix}.{key}" if prefix else key
            if isinstance(value, dict):
                nested = self.flatten_json(value, full_key)
                result.update(nested)
            elif isinstance(value, list):
                # Flatten list items with index
                for i, item in enumerate(value):
                    if isinstance(item, dict):
                        nested = self.flatten_json(item, f"{full_key}.{i}")
                        result.update(nested)
                    else:
                        result[f"{full_key}.{i}"] = item
            else:
                result[full_key] = value
        return result

    def parse_xml(self, content: bytes) -> DatasetPreview:
        """Parse XML content into a tabular representation."""
        if len(content) > MAX_FILE_SIZE:
            raise ValueError("File exceeds maximum size of 50 MB")

        try:
            root = ET.fromstring(content)
        except ET.ParseError as e:
            raise ValueError(f"Could not parse file as XML: {e}")

        # Find repeating child elements (records)
        children = list(root)
        if not children:
            raise ValueError("Could not parse file as XML: no child elements found")

        # Group children by tag to find the repeating record element
        tag_counts: dict[str, int] = {}
        for child in children:
            tag = child.tag.split("}")[-1] if "}" in child.tag else child.tag
            tag_counts[tag] = tag_counts.get(tag, 0) + 1

        # Use the most common child tag as the record element
        record_tag = max(tag_counts, key=tag_counts.get)
        records = [child for child in children
                   if (child.tag.split("}")[-1] if "}" in child.tag else child.tag) == record_tag]

        # Extract fields from records (elements + attributes)
        all_rows = []
        all_fields: list[str] = []
        seen_fields: set[str] = set()

        for record in records:
            row: dict[str, str] = {}
            # Attributes of the record element
            for attr_name, attr_value in record.attrib.items():
                field_name = f"@{attr_name}"
                row[field_name] = attr_value
                if field_name not in seen_fields:
                    seen_fields.add(field_name)
                    all_fields.append(field_name)

            # Child elements
            for elem in record:
                tag = elem.tag.split("}")[-1] if "}" in elem.tag else elem.tag
                text = elem.text.strip() if elem.text else ""
                row[tag] = text
                if tag not in seen_fields:
                    seen_fields.add(tag)
                    all_fields.append(tag)

                # Element attributes
                for attr_name, attr_value in elem.attrib.items():
                    field_name = f"{tag}.@{attr_name}"
                    row[field_name] = attr_value
                    if field_name not in seen_fields:
                        seen_fields.add(field_name)
                        all_fields.append(field_name)

            all_rows.append(row)

        row_count = len(all_rows)
        sample = all_rows[:10]

        columns = []
        for field_name in all_fields:
            col_values = [row.get(field_name, "") for row in all_rows]
            non_empty = [v for v in col_values if v and v.strip()]
            sample_vals = non_empty[:5]
            null_count = sum(1 for v in col_values if not v or not v.strip())
            inferred = _infer_type(non_empty[:20])
            columns.append(ColumnInfo(
                name=field_name,
                inferred_type=inferred,
                sample_values=sample_vals,
                null_count=null_count,
            ))

        return DatasetPreview(
            source_type="xml",
            columns=columns,
            row_count=row_count,
            sample=sample,
        )

    def connect_sparql(self, endpoint_url: str) -> dict:
        """Test SPARQL endpoint connectivity with a simple ASK query."""
        try:
            test_query = "ASK { ?s ?p ?o }"
            response = requests.get(
                endpoint_url,
                params={"query": test_query},
                headers={"Accept": "application/sparql-results+json"},
                timeout=10,
            )
            if response.status_code == 200:
                return {"connected": True, "message": "SPARQL endpoint is reachable", "endpoint": endpoint_url}
            else:
                return {"connected": False, "message": f"Endpoint returned status {response.status_code}", "endpoint": endpoint_url}
        except requests.Timeout:
            return {"connected": False, "message": "Connection timed out after 10 seconds", "endpoint": endpoint_url}
        except requests.ConnectionError:
            sanitized = _sanitize_error(endpoint_url)
            return {"connected": False, "message": f"Could not reach endpoint: {sanitized}", "endpoint": endpoint_url}
        except Exception as e:
            sanitized = _sanitize_error(str(e))
            return {"connected": False, "message": f"Connection failed: {sanitized}", "endpoint": endpoint_url}

    def execute_query(self, endpoint_url: str, query: str) -> dict:
        """Execute a SPARQL query and return tabular results."""
        try:
            response = requests.get(
                endpoint_url,
                params={"query": query},
                headers={"Accept": "application/sparql-results+json"},
                timeout=30,
            )
            if response.status_code != 200:
                raise ValueError(f"SPARQL query error: endpoint returned status {response.status_code}")

            result = response.json()
            variables = result.get("head", {}).get("vars", [])
            bindings = result.get("results", {}).get("bindings", [])

            rows = []
            for binding in bindings:
                row = {}
                for var in variables:
                    if var in binding:
                        row[var] = binding[var].get("value", "")
                    else:
                        row[var] = ""
                rows.append(row)

            return {
                "columns": variables,
                "rows": rows,
                "row_count": len(rows),
            }
        except ValueError:
            raise
        except requests.Timeout:
            raise ValueError("SPARQL query timed out")
        except Exception as e:
            sanitized = _sanitize_error(str(e))
            raise ValueError(f"SPARQL query error: {sanitized}")
