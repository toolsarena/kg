"""
Tests for task 10.2 — Graph Explorer endpoints (expand, search, path).

Verifies:
- GET /api/expand?node_id=X&hops=N returns a subgraph with nodes and edges within N hops
- GET /api/search?q=X returns nodes matching the search query
- GET /api/path?source=X&target=Y returns shortest path between two nodes

Requirements: 10.1
"""
import pytest
from fastapi.testclient import TestClient


@pytest.fixture
def loaded_client(tmp_path, monkeypatch):
    """Create a test client with a loaded graph containing known nodes and edges."""
    monkeypatch.chdir(tmp_path)
    (tmp_path / "projects").mkdir()

    # Create a graph with a clear topology:
    #   Alice --knows--> Bob --knows--> Charlie --knows--> Diana
    #   Alice --worksAt--> Acme
    #   Bob --worksAt--> Acme
    ttl_content = """\
@prefix kg: <http://kg.local/ontology#> .
@prefix kgr: <http://kg.local/resource/> .
@prefix skos: <http://www.w3.org/2004/02/skos/core#> .
@prefix rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .

kgr:Alice a kg:Person ;
    skos:prefLabel "Alice" ;
    rdfs:comment "A software engineer" .

kgr:Bob a kg:Person ;
    skos:prefLabel "Bob" ;
    rdfs:comment "A data scientist" .

kgr:Charlie a kg:Person ;
    skos:prefLabel "Charlie" ;
    rdfs:comment "A product manager" .

kgr:Diana a kg:Person ;
    skos:prefLabel "Diana" ;
    rdfs:comment "A designer" .

kgr:Acme a kg:Company ;
    skos:prefLabel "Acme Corp" ;
    rdfs:comment "A technology company" .

kgr:Alice kg:knows kgr:Bob .
kgr:Bob kg:knows kgr:Charlie .
kgr:Charlie kg:knows kgr:Diana .
kgr:Alice kg:worksAt kgr:Acme .
kgr:Bob kg:worksAt kgr:Acme .
"""
    ttl_path = tmp_path / "test_graph.ttl"
    ttl_path.write_text(ttl_content, encoding="utf-8")

    # Create a minimal config.yaml so LLMProviderManager doesn't fail
    config_path = tmp_path / "config.yaml"
    config_path.write_text(
        "llm:\n  provider: ollama\n  model: test\n  base_url: http://localhost:11434\n",
        encoding="utf-8",
    )

    # Import and load the server with our test graph
    import explorer.server as srv
    srv.load_ttl(str(ttl_path))

    client = TestClient(srv.app)
    return client


class TestExpandEndpoint:
    """GET /api/expand?node_id=X&hops=N returns subgraph within N hops."""

    def test_expand_known_node_returns_subgraph(self, loaded_client):
        """Expanding from a known node returns nodes and edges."""
        resp = loaded_client.get("/api/expand", params={"node_id": "Alice", "hops": 1})
        assert resp.status_code == 200
        data = resp.json()

        assert "nodes" in data
        assert "edges" in data
        assert "center" in data
        assert data["center"] == "Alice"
        assert len(data["nodes"]) > 0
        assert len(data["edges"]) > 0

    def test_expand_1_hop_includes_direct_neighbors(self, loaded_client):
        """1-hop expansion from Alice should include Bob and Acme (direct neighbors)."""
        resp = loaded_client.get("/api/expand", params={"node_id": "Alice", "hops": 1})
        assert resp.status_code == 200
        data = resp.json()

        node_ids = {n["id"] for n in data["nodes"]}
        assert "Alice" in node_ids
        assert "Bob" in node_ids
        assert "Acme" in node_ids

    def test_expand_1_hop_excludes_distant_nodes(self, loaded_client):
        """1-hop expansion from Alice should NOT include Charlie or Diana."""
        resp = loaded_client.get("/api/expand", params={"node_id": "Alice", "hops": 1})
        assert resp.status_code == 200
        data = resp.json()

        node_ids = {n["id"] for n in data["nodes"]}
        assert "Charlie" not in node_ids
        assert "Diana" not in node_ids

    def test_expand_2_hops_includes_further_neighbors(self, loaded_client):
        """2-hop expansion from Alice should include Charlie (via Bob)."""
        resp = loaded_client.get("/api/expand", params={"node_id": "Alice", "hops": 2})
        assert resp.status_code == 200
        data = resp.json()

        node_ids = {n["id"] for n in data["nodes"]}
        assert "Alice" in node_ids
        assert "Bob" in node_ids
        assert "Charlie" in node_ids

    def test_expand_returns_edges_within_subgraph(self, loaded_client):
        """Edges in the result connect only nodes within the subgraph."""
        resp = loaded_client.get("/api/expand", params={"node_id": "Alice", "hops": 1})
        assert resp.status_code == 200
        data = resp.json()

        node_ids = {n["id"] for n in data["nodes"]}
        for edge in data["edges"]:
            assert edge["source"] in node_ids
            assert edge["target"] in node_ids

    def test_expand_unknown_node_returns_404(self, loaded_client):
        """Expanding from a non-existent node returns 404."""
        resp = loaded_client.get("/api/expand", params={"node_id": "NonExistent", "hops": 1})
        assert resp.status_code == 404

    def test_expand_includes_hops_in_response(self, loaded_client):
        """Response includes the hops parameter used."""
        resp = loaded_client.get("/api/expand", params={"node_id": "Alice", "hops": 3})
        assert resp.status_code == 200
        data = resp.json()
        assert data["hops"] == 3


class TestSearchEndpoint:
    """GET /api/search?q=X returns nodes matching the search query."""

    def test_search_by_exact_label(self, loaded_client):
        """Searching for an exact label returns the matching node."""
        resp = loaded_client.get("/api/search", params={"q": "Alice"})
        assert resp.status_code == 200
        data = resp.json()

        assert len(data) > 0
        labels = [n["label"] for n in data]
        assert "Alice" in labels

    def test_search_by_partial_label(self, loaded_client):
        """Searching for a partial label returns matching nodes."""
        resp = loaded_client.get("/api/search", params={"q": "Acme"})
        assert resp.status_code == 200
        data = resp.json()

        assert len(data) > 0
        # Should find "Acme Corp"
        labels = [n["label"] for n in data]
        assert any("Acme" in label for label in labels)

    def test_search_case_insensitive(self, loaded_client):
        """Search is case-insensitive."""
        resp = loaded_client.get("/api/search", params={"q": "alice"})
        assert resp.status_code == 200
        data = resp.json()

        assert len(data) > 0
        labels = [n["label"] for n in data]
        assert "Alice" in labels

    def test_search_by_description(self, loaded_client):
        """Searching for text in description returns matching nodes."""
        resp = loaded_client.get("/api/search", params={"q": "software"})
        assert resp.status_code == 200
        data = resp.json()

        assert len(data) > 0
        # Alice has "A software engineer" as description
        node_ids = [n["id"] for n in data]
        assert "Alice" in node_ids

    def test_search_no_results(self, loaded_client):
        """Searching for a non-existent term returns empty list."""
        resp = loaded_client.get("/api/search", params={"q": "zzzznonexistent"})
        assert resp.status_code == 200
        data = resp.json()
        assert data == []

    def test_search_results_have_required_fields(self, loaded_client):
        """Each search result has id, label, and type fields."""
        resp = loaded_client.get("/api/search", params={"q": "Bob"})
        assert resp.status_code == 200
        data = resp.json()

        assert len(data) > 0
        for node in data:
            assert "id" in node
            assert "label" in node
            assert "type" in node

    def test_search_results_sorted_by_score(self, loaded_client):
        """Search results are sorted by relevance score (highest first)."""
        resp = loaded_client.get("/api/search", params={"q": "Alice"})
        assert resp.status_code == 200
        data = resp.json()

        if len(data) > 1:
            scores = [n["score"] for n in data]
            assert scores == sorted(scores, reverse=True)


class TestPathEndpoint:
    """GET /api/path?source=X&target=Y returns shortest path between two nodes."""

    def test_path_between_connected_nodes(self, loaded_client):
        """Finding path between directly connected nodes returns a valid path."""
        resp = loaded_client.get("/api/path", params={"source": "Alice", "target": "Bob"})
        assert resp.status_code == 200
        data = resp.json()

        assert "path" in data
        assert "nodes" in data
        assert "edges" in data
        assert len(data["path"]) > 0
        assert data["path"][0] == "Alice"
        assert data["path"][-1] == "Bob"

    def test_path_between_distant_nodes(self, loaded_client):
        """Finding path between distant nodes returns intermediate steps."""
        resp = loaded_client.get("/api/path", params={"source": "Alice", "target": "Diana"})
        assert resp.status_code == 200
        data = resp.json()

        assert len(data["path"]) > 2  # Alice -> ... -> Diana
        assert data["path"][0] == "Alice"
        assert data["path"][-1] == "Diana"

    def test_path_includes_nodes_and_edges(self, loaded_client):
        """Path response includes node details and edge details."""
        resp = loaded_client.get("/api/path", params={"source": "Alice", "target": "Charlie"})
        assert resp.status_code == 200
        data = resp.json()

        assert len(data["nodes"]) > 0
        assert len(data["edges"]) > 0
        # Nodes should have id and label
        for node in data["nodes"]:
            assert "id" in node
            assert "label" in node

    def test_path_no_path_exists(self, loaded_client):
        """When no path exists, returns empty path."""
        # Create a disconnected scenario - use a node that exists but is isolated
        # In our graph, all nodes are connected, so we test with non-existent node
        resp = loaded_client.get("/api/path", params={"source": "Alice", "target": "NonExistent"})
        assert resp.status_code == 404

    def test_path_source_not_found(self, loaded_client):
        """Returns 404 when source node doesn't exist."""
        resp = loaded_client.get("/api/path", params={"source": "NonExistent", "target": "Alice"})
        assert resp.status_code == 404

    def test_path_target_not_found(self, loaded_client):
        """Returns 404 when target node doesn't exist."""
        resp = loaded_client.get("/api/path", params={"source": "Alice", "target": "NonExistent"})
        assert resp.status_code == 404

    def test_path_same_source_and_target(self, loaded_client):
        """Path from a node to itself returns just that node."""
        resp = loaded_client.get("/api/path", params={"source": "Alice", "target": "Alice"})
        assert resp.status_code == 200
        data = resp.json()

        assert data["path"] == ["Alice"]
        assert len(data["nodes"]) == 1

    def test_path_edges_connect_consecutive_nodes(self, loaded_client):
        """Edges in the path connect consecutive nodes in the path list."""
        resp = loaded_client.get("/api/path", params={"source": "Alice", "target": "Charlie"})
        assert resp.status_code == 200
        data = resp.json()

        path = data["path"]
        edges = data["edges"]
        # For each consecutive pair in path, there should be an edge
        for i in range(len(path) - 1):
            found = False
            for e in edges:
                if (e["source"] == path[i] and e["target"] == path[i + 1]) or \
                   (e["source"] == path[i + 1] and e["target"] == path[i]):
                    found = True
                    break
            assert found, f"No edge found between {path[i]} and {path[i+1]}"
