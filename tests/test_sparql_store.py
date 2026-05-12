"""
Tests for task 10.3 — Unit tests for SPARQLStore (load, query).
Verifies:
- Loading TTL string/file into the store's graph
- Running SPARQL SELECT query returns expected results
- Handling empty graphs and invalid queries gracefully
Requirements: 10.1
"""
from pathlib import Path

import pytest
from rdflib import Graph

from store.sparql_store import SPARQLStore


SAMPLE_TTL = """\
@prefix ex: <http://example.org/> .
@prefix rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .

ex:Alice a ex:Person ;
    rdfs:label "Alice" ;
    ex:knows ex:Bob .

ex:Bob a ex:Person ;
    rdfs:label "Bob" ;
    ex:worksAt ex:Acme .

ex:Acme a ex:Company ;
    rdfs:label "Acme Corp" .
"""


class TestSPARQLStoreLoad:
    """Tests for loading TTL into the store."""

    def test_load_ttl_from_file(self, tmp_path):
        """Loading a TTL file populates the graph with expected triples."""
        ttl_file = tmp_path / "sample.ttl"
        ttl_file.write_text(SAMPLE_TTL, encoding="utf-8")

        store = SPARQLStore()
        store.load_ttl(ttl_file)

        assert store.count() > 0

    def test_load_ttl_file_triple_count(self, tmp_path):
        """Loading a known TTL file results in the correct number of triples."""
        ttl_file = tmp_path / "sample.ttl"
        ttl_file.write_text(SAMPLE_TTL, encoding="utf-8")

        store = SPARQLStore()
        store.load_ttl(ttl_file)

        # 3 type triples + 2 label triples + 1 knows + 1 worksAt + 1 label = 8
        assert store.count() == 8

    def test_load_rdf_graph(self):
        """Loading an rdflib Graph object merges triples into the store."""
        g = Graph()
        g.parse(data=SAMPLE_TTL, format="turtle")

        store = SPARQLStore()
        store.load_rdf_graph(g)

        assert store.count() == len(g)

    def test_load_multiple_files_accumulates(self, tmp_path):
        """Loading multiple TTL files accumulates triples."""
        ttl1 = tmp_path / "a.ttl"
        ttl1.write_text(
            '@prefix ex: <http://example.org/> .\nex:X a ex:Thing .\n',
            encoding="utf-8",
        )
        ttl2 = tmp_path / "b.ttl"
        ttl2.write_text(
            '@prefix ex: <http://example.org/> .\nex:Y a ex:Thing .\n',
            encoding="utf-8",
        )

        store = SPARQLStore()
        store.load_ttl(ttl1)
        count_after_first = store.count()
        store.load_ttl(ttl2)

        assert store.count() > count_after_first

    def test_empty_store_has_zero_triples(self):
        """A freshly created store has zero triples."""
        store = SPARQLStore()
        assert store.count() == 0


class TestSPARQLStoreQuery:
    """Tests for running SPARQL queries against the store."""

    @pytest.fixture
    def loaded_store(self):
        """Return a store pre-loaded with sample TTL."""
        store = SPARQLStore()
        g = Graph()
        g.parse(data=SAMPLE_TTL, format="turtle")
        store.load_rdf_graph(g)
        return store

    def test_select_query_returns_results(self, loaded_store):
        """A SELECT query on a populated graph returns non-empty results."""
        results = loaded_store.query(
            "SELECT ?s ?label WHERE { ?s <http://www.w3.org/2000/01/rdf-schema#label> ?label }"
        )
        assert len(results) == 3  # Alice, Bob, Acme Corp

    def test_select_query_returns_dicts(self, loaded_store):
        """Each result row is a dict with variable names as keys."""
        results = loaded_store.query(
            "SELECT ?s ?label WHERE { ?s <http://www.w3.org/2000/01/rdf-schema#label> ?label }"
        )
        for row in results:
            assert isinstance(row, dict)
            assert "s" in row
            assert "label" in row

    def test_query_with_filter(self, loaded_store):
        """A SPARQL query with FILTER returns only matching results."""
        results = loaded_store.query("""
            PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
            SELECT ?s WHERE {
                ?s rdfs:label "Alice" .
            }
        """)
        assert len(results) == 1
        assert "Alice" in results[0]["s"]

    def test_query_types(self, loaded_store):
        """Querying for rdf:type returns typed resources."""
        results = loaded_store.query("""
            PREFIX ex: <http://example.org/>
            PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
            SELECT ?s WHERE {
                ?s rdf:type ex:Person .
            }
        """)
        assert len(results) == 2  # Alice and Bob

    def test_query_empty_graph_returns_empty(self):
        """Querying an empty store returns an empty list."""
        store = SPARQLStore()
        results = store.query("SELECT ?s ?p ?o WHERE { ?s ?p ?o }")
        assert results == []

    def test_query_no_matches_returns_empty(self, loaded_store):
        """A query with no matches returns an empty list."""
        results = loaded_store.query("""
            PREFIX ex: <http://example.org/>
            SELECT ?s WHERE {
                ?s a ex:NonExistentType .
            }
        """)
        assert results == []

    def test_query_raw_returns_rdflib_result(self, loaded_store):
        """query_raw returns an rdflib query result object."""
        result = loaded_store.query_raw(
            "SELECT ?s WHERE { ?s a <http://example.org/Person> }"
        )
        # rdflib Result object has bindings
        rows = list(result)
        assert len(rows) == 2

    def test_invalid_sparql_raises_exception(self, loaded_store):
        """An invalid SPARQL query raises an exception."""
        with pytest.raises(Exception):
            loaded_store.query("THIS IS NOT VALID SPARQL")

    def test_describe_returns_properties(self, loaded_store):
        """describe() returns predicate-object pairs for a given URI."""
        props = loaded_store.describe("http://example.org/Alice")
        assert len(props) > 0
        predicates = [p for p, o in props]
        assert any("label" in p for p in predicates)

    def test_get_all_types(self, loaded_store):
        """get_all_types() returns distinct type URIs."""
        types = loaded_store.get_all_types()
        assert "http://example.org/Person" in types
        assert "http://example.org/Company" in types

    def test_get_nodes_by_type(self, loaded_store):
        """get_nodes_by_type() returns nodes of the specified type."""
        persons = loaded_store.get_nodes_by_type("http://example.org/Person")
        assert len(persons) == 2
        assert "http://example.org/Alice" in persons
        assert "http://example.org/Bob" in persons
