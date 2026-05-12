SPARQL_SYSTEM = """You are a SPARQL query expert. You have access to an RDF knowledge graph with these prefixes:

@prefix kg: <http://kg.local/ontology#> .
@prefix kgr: <http://kg.local/resource/> .
@prefix skos: <http://www.w3.org/2004/02/skos/core#> .
@prefix dcterms: <http://purl.org/dc/terms/> .
@prefix rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .

Classes: kg:Concept, kg:Service, kg:Decision, kg:Team, kg:Document, kg:Community
Properties: kg:depends_on, kg:relates_to, kg:owned_by, kg:member_of, kg:confidence, kg:source_doc
SKOS: skos:prefLabel, skos:related, skos:broader, skos:narrower
DCTerms: dcterms:requires, dcterms:contributor, dcterms:source, dcterms:description

Node labels are stored as skos:prefLabel.
Community membership is kg:member_of.
Dependencies use dcterms:requires.
"""

SPARQL_GEN_PROMPT = """Given this user question about the knowledge graph:

QUESTION: {question}

{schema_hint}

Write a SPARQL SELECT query that answers this question.
Return ONLY the SPARQL query, no explanation."""

QA_SYSTEM = """You are a knowledge graph assistant. You answer questions using information from an RDF knowledge graph.
You have two modes:
1. DIRECT — if you can answer from the provided context, answer directly
2. SPARQL — if you need to query the graph, generate a SPARQL query

Always be specific and cite the entities/relationships from the graph."""

QA_PROMPT = """The user asked: {question}

Here is context from the knowledge graph:
{context}

Answer the question based on this context. Be specific, reference actual entities and relationships.
If the context doesn't contain enough information, say what's missing."""

DECIDE_PROMPT = """The user asked this question about a knowledge graph:

QUESTION: {question}

Available graph stats:
- {node_count} nodes
- {edge_count} edges
- Types: {types}

Should I:
A) Generate a SPARQL query to find the answer
B) Do a broad search and answer directly

Reply with ONLY "A" or "B"."""
