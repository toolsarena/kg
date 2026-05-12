"""
Tests for task 6.1 — Ensure build endpoint produces typed graph structure.
Verifies:
- POST /api/projects/{id}/build with {"filename": "..."} populates nodes/edges
- Every node has a non-empty `type` field
- Every edge has a non-empty `relation` field
- Build response includes graph_data with nodes/edges for frontend rendering
Requirements: 4.1, 4.2, 4.3
"""
import json
from pathlib import Path
from unittest.mock import patch

import pytest
from fastapi.testclient import TestClient


@pytest.fixture(autouse=True)
def setup_projects_dir(tmp_path):
    """Use a temporary directory for projects during tests."""
    import explorer.routes.projects as proj_mod

    original_dir = proj_mod.PROJECTS_DIR
    proj_mod.PROJECTS_DIR = tmp_path
    yield tmp_path
    proj_mod.PROJECTS_DIR = original_dir


@pytest.fixture
def client():
    """Create a test client with only the projects router."""
    from fastapi import FastAPI
    from explorer.routes.projects import router

    app = FastAPI()
    app.include_router(router)
    return TestClient(app)


@pytest.fixture
def project_with_typed_ttl(setup_projects_dir):
    """Create a project with a TTL file containing typed classes and object properties."""
    project_dir = setup_projects_dir / "typed_test"
    project_dir.mkdir()
    meta = {"name": "Typed Test", "id": "typed_test", "created": 1000.0, "modified": 1000.0}
    (project_dir / "meta.json").write_text(json.dumps(meta))

    # TTL with explicit types and object properties (edges)
    ttl = """@prefix ex: <http://example.org/> .
@prefix rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .

ex:Customer a ex:Entity ;
    rdfs:label "Customer" .

ex:Order a ex:Entity ;
    rdfs:label "Order" .

ex:Product a ex:Entity ;
    rdfs:label "Product" .

ex:Customer ex:places ex:Order .
ex:Order ex:contains ex:Product .
"""
    (project_dir / "model.ttl").write_text(ttl, encoding="utf-8")
    return "typed_test"


@pytest.fixture
def project_with_minimal_ttl(setup_projects_dir):
    """Create a project with a TTL file that has no explicit rdf:type (tests default type)."""
    project_dir = setup_projects_dir / "minimal_test"
    project_dir.mkdir()
    meta = {"name": "Minimal Test", "id": "minimal_test", "created": 1000.0, "modified": 1000.0}
    (project_dir / "meta.json").write_text(json.dumps(meta))

    # TTL with no explicit rdf:type — nodes should default to "concept"
    ttl = """@prefix ex: <http://example.org/> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .

ex:Alpha rdfs:label "Alpha" .
ex:Beta rdfs:label "Beta" .
ex:Alpha ex:linksTo ex:Beta .
"""
    (project_dir / "no_types.ttl").write_text(ttl, encoding="utf-8")
    return "minimal_test"


class TestBuildTypedGraphStructure:
    """Tests for POST /api/projects/{id}/build — typed graph output."""

    @patch("explorer.server.new_model_nodes", [])
    @patch("explorer.server.new_model_edges", [])
    def test_build_populates_nodes_and_edges(self, client, project_with_typed_ttl):
        """Build with a filename populates nodes and edges in the response."""
        resp = client.post(
            f"/api/projects/{project_with_typed_ttl}/build",
            json={"filename": "model.ttl"},
        )
        assert resp.status_code == 200
        data = resp.json()

        assert data["built"] is True
        assert data["nodes"] > 0
        assert data["edges"] > 0
        assert data["triples"] > 0

    @patch("explorer.server.new_model_nodes", [])
    @patch("explorer.server.new_model_edges", [])
    def test_every_node_has_nonempty_type(self, client, project_with_typed_ttl):
        """Every node in the build result must have a non-empty type field."""
        resp = client.post(
            f"/api/projects/{project_with_typed_ttl}/build",
            json={"filename": "model.ttl"},
        )
        assert resp.status_code == 200
        data = resp.json()

        graph_data = data["graph_data"]
        assert len(graph_data["nodes"]) > 0

        for node in graph_data["nodes"]:
            assert "type" in node, f"Node {node['id']} missing 'type' field"
            assert node["type"], f"Node {node['id']} has empty 'type' field"
            assert node["type"].strip(), f"Node {node['id']} has whitespace-only 'type' field"

    @patch("explorer.server.new_model_nodes", [])
    @patch("explorer.server.new_model_edges", [])
    def test_every_edge_has_nonempty_relation(self, client, project_with_typed_ttl):
        """Every edge in the build result must have a non-empty relation field."""
        resp = client.post(
            f"/api/projects/{project_with_typed_ttl}/build",
            json={"filename": "model.ttl"},
        )
        assert resp.status_code == 200
        data = resp.json()

        graph_data = data["graph_data"]
        assert len(graph_data["edges"]) > 0

        for edge in graph_data["edges"]:
            assert "relation" in edge, f"Edge {edge} missing 'relation' field"
            assert edge["relation"], f"Edge {edge} has empty 'relation' field"
            assert edge["relation"].strip(), f"Edge {edge} has whitespace-only 'relation' field"

    @patch("explorer.server.new_model_nodes", [])
    @patch("explorer.server.new_model_edges", [])
    def test_build_response_includes_graph_data(self, client, project_with_typed_ttl):
        """Build response includes graph_data with nodes and edges for frontend rendering."""
        resp = client.post(
            f"/api/projects/{project_with_typed_ttl}/build",
            json={"filename": "model.ttl"},
        )
        assert resp.status_code == 200
        data = resp.json()

        # graph_data must be present
        assert "graph_data" in data
        assert "nodes" in data["graph_data"]
        assert "edges" in data["graph_data"]

        # Nodes have required fields
        for node in data["graph_data"]["nodes"]:
            assert "id" in node
            assert "label" in node
            assert "type" in node

        # Edges have required fields
        for edge in data["graph_data"]["edges"]:
            assert "source" in edge
            assert "target" in edge
            assert "relation" in edge

    @patch("explorer.server.new_model_nodes", [])
    @patch("explorer.server.new_model_edges", [])
    def test_nodes_default_to_concept_type(self, client, project_with_minimal_ttl):
        """Nodes without explicit rdf:type default to 'concept'."""
        resp = client.post(
            f"/api/projects/{project_with_minimal_ttl}/build",
            json={"filename": "no_types.ttl"},
        )
        assert resp.status_code == 200
        data = resp.json()

        graph_data = data["graph_data"]
        assert len(graph_data["nodes"]) > 0

        for node in graph_data["nodes"]:
            assert node["type"] == "concept", (
                f"Node {node['id']} should default to 'concept' but got '{node['type']}'"
            )

    @patch("explorer.server.new_model_nodes", [])
    @patch("explorer.server.new_model_edges", [])
    def test_build_file_not_found(self, client, project_with_typed_ttl):
        """Returns 404 when the specified file doesn't exist."""
        resp = client.post(
            f"/api/projects/{project_with_typed_ttl}/build",
            json={"filename": "nonexistent.ttl"},
        )
        assert resp.status_code == 404

    def test_build_project_not_found(self, client):
        """Returns 404 for non-existent project."""
        resp = client.post("/api/projects/nonexistent/build", json={"filename": "x.ttl"})
        assert resp.status_code == 404

    @patch("explorer.server.new_model_nodes", [])
    @patch("explorer.server.new_model_edges", [])
    def test_merge_and_build_includes_graph_data(self, client, setup_projects_dir):
        """Merge-and-build also returns graph_data with typed nodes/edges."""
        project_dir = setup_projects_dir / "merge_typed"
        project_dir.mkdir()
        meta = {"name": "Merge Typed", "id": "merge_typed", "created": 1000.0, "modified": 1000.0}
        (project_dir / "meta.json").write_text(json.dumps(meta))

        ttl_a = """@prefix ex: <http://example.org/> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .
ex:Foo a ex:Thing ; rdfs:label "Foo" .
ex:Bar a ex:Thing ; rdfs:label "Bar" .
ex:Foo ex:knows ex:Bar .
"""
        ttl_b = """@prefix ex: <http://example.org/> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .
ex:Baz a ex:Thing ; rdfs:label "Baz" .
ex:Baz ex:likes ex:Foo .
"""
        (project_dir / "a.ttl").write_text(ttl_a, encoding="utf-8")
        (project_dir / "b.ttl").write_text(ttl_b, encoding="utf-8")

        resp = client.post("/api/projects/merge_typed/merge-and-build", json={})
        assert resp.status_code == 200
        data = resp.json()

        assert "graph_data" in data
        graph_data = data["graph_data"]

        # All nodes have non-empty type
        for node in graph_data["nodes"]:
            assert node["type"], f"Node {node['id']} has empty type"

        # All edges have non-empty relation
        for edge in graph_data["edges"]:
            assert edge["relation"], f"Edge {edge} has empty relation"
