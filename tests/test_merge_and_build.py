"""
Tests for the merge-and-build endpoint (task 4.2).
Tests POST /api/projects/{id}/merge-and-build.
"""
import json
from pathlib import Path
from unittest.mock import patch, MagicMock

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
def project_with_files(setup_projects_dir):
    """Create a project with two TTL files for merge testing."""
    project_dir = setup_projects_dir / "merge_test"
    project_dir.mkdir()
    meta = {"name": "Merge Test", "id": "merge_test", "created": 1000.0, "modified": 1000.0}
    (project_dir / "meta.json").write_text(json.dumps(meta))

    ttl_a = """@prefix ex: <http://example.org/> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .

ex:Customer a ex:Class ;
    rdfs:label "Customer" .
ex:Customer ex:hasProperty ex:Name .
"""
    ttl_b = """@prefix ex: <http://example.org/> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .

ex:Order a ex:Class ;
    rdfs:label "Order" .
ex:Order ex:belongsTo ex:Customer .
"""
    (project_dir / "customers.ttl").write_text(ttl_a, encoding="utf-8")
    (project_dir / "orders.ttl").write_text(ttl_b, encoding="utf-8")
    return "merge_test"


class TestMergeAndBuild:
    """Tests for POST /api/projects/{id}/merge-and-build."""

    @patch("explorer.server.new_model_nodes", [])
    @patch("explorer.server.new_model_edges", [])
    def test_merge_and_build_all_files(self, client, project_with_files, setup_projects_dir):
        """When no files specified, merges all .ttl files in project."""
        resp = client.post(f"/api/projects/{project_with_files}/merge-and-build", json={})
        assert resp.status_code == 200
        data = resp.json()

        assert data["merged"] is True
        assert data["built"] is True
        assert data["output"] == "merged.ttl"
        assert data["triples"] > 0
        assert data["nodes"] > 0
        assert data["edges"] > 0
        assert set(data["source_files"]) == {"customers.ttl", "orders.ttl"}

        # Verify merged.ttl was saved
        merged_path = setup_projects_dir / project_with_files / "merged.ttl"
        assert merged_path.exists()
        content = merged_path.read_text(encoding="utf-8")
        assert "Customer" in content
        assert "Order" in content

    @patch("explorer.server.new_model_nodes", [])
    @patch("explorer.server.new_model_edges", [])
    def test_merge_and_build_selected_files(self, client, project_with_files):
        """When files list is provided, only merges those files."""
        resp = client.post(
            f"/api/projects/{project_with_files}/merge-and-build",
            json={"files": ["customers.ttl"]},
        )
        assert resp.status_code == 200
        data = resp.json()

        assert data["merged"] is True
        assert data["built"] is True
        assert data["source_files"] == ["customers.ttl"]
        assert data["triples"] > 0

    @patch("explorer.server.new_model_nodes", [])
    @patch("explorer.server.new_model_edges", [])
    def test_merge_and_build_custom_output(self, client, project_with_files, setup_projects_dir):
        """Supports custom output filename."""
        resp = client.post(
            f"/api/projects/{project_with_files}/merge-and-build",
            json={"output": "combined.ttl"},
        )
        assert resp.status_code == 200
        data = resp.json()
        assert data["output"] == "combined.ttl"

        combined_path = setup_projects_dir / project_with_files / "combined.ttl"
        assert combined_path.exists()

    def test_merge_and_build_project_not_found(self, client):
        """Returns 404 for non-existent project."""
        resp = client.post("/api/projects/nonexistent/merge-and-build", json={})
        assert resp.status_code == 404

    def test_merge_and_build_no_files(self, client, setup_projects_dir):
        """Returns 400 when project has no .ttl files."""
        project_dir = setup_projects_dir / "empty_project"
        project_dir.mkdir()
        meta = {"name": "Empty", "id": "empty_project", "created": 1000.0, "modified": 1000.0}
        (project_dir / "meta.json").write_text(json.dumps(meta))

        resp = client.post("/api/projects/empty_project/merge-and-build", json={})
        assert resp.status_code == 400
        assert "No .ttl files" in resp.json()["error"]

    @patch("explorer.server.new_model_nodes", [])
    @patch("explorer.server.new_model_edges", [])
    def test_merge_and_build_excludes_merged_ttl(self, client, project_with_files, setup_projects_dir):
        """When defaulting to all files, excludes existing merged.ttl."""
        # Create a pre-existing merged.ttl
        project_dir = setup_projects_dir / project_with_files
        (project_dir / "merged.ttl").write_text(
            "@prefix ex: <http://example.org/> .\nex:Old a ex:Stale .\n", encoding="utf-8"
        )

        resp = client.post(f"/api/projects/{project_with_files}/merge-and-build", json={})
        assert resp.status_code == 200
        data = resp.json()

        # merged.ttl should not be in source_files
        assert "merged.ttl" not in data["source_files"]
        assert "customers.ttl" in data["source_files"]
        assert "orders.ttl" in data["source_files"]

    @patch("explorer.server.new_model_nodes", [])
    @patch("explorer.server.new_model_edges", [])
    def test_merge_and_build_returns_correct_stats(self, client, project_with_files):
        """Verifies the response contains all required stat fields."""
        resp = client.post(f"/api/projects/{project_with_files}/merge-and-build", json={})
        assert resp.status_code == 200
        data = resp.json()

        # All required fields present
        assert "triples" in data
        assert "nodes" in data
        assert "edges" in data
        assert "source_files" in data
        assert "merged" in data
        assert "built" in data
        assert "output" in data

        # Types are correct
        assert isinstance(data["triples"], int)
        assert isinstance(data["nodes"], int)
        assert isinstance(data["edges"], int)
        assert isinstance(data["source_files"], list)
