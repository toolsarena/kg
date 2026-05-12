"""
Semantic extraction prompt for LLM-based entity/relationship extraction.
Used by the build command to extract knowledge from documents.
"""

EXTRACTION_PROMPT = """Read the following document and extract ALL entities and relationships.

DOCUMENT:
---
{content}
---

Extract as JSON with this exact structure:
{{"nodes": [{{"id": "short_snake_case_id", "label": "Human Readable Name", "type": "concept|service|decision|team|process|technology", "description": "one line description"}}], "edges": [{{"source": "node_id", "target": "node_id", "relation": "depends_on|relates_to|owned_by|uses|implements|calls|part_of|rationale_for", "confidence": "EXTRACTED|INFERRED", "description": "why this relationship exists"}}]}}

Rules:
- Extract EVERY named system, service, concept, team, technology, decision, best practice
- Extract ALL relationships - explicit and implied
- Use consistent IDs (snake_case, lowercase, only a-z0-9_)
- EXTRACTED = stated explicitly in text, INFERRED = reasoned by you
- For AWS services, use ids like: aws_lambda, aws_s3, amazon_cloudwatch
- For architectural concepts: well_architected, operational_excellence, etc.

Return ONLY valid JSON."""
