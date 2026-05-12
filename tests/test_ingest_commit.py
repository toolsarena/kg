"""
Tests for ingest commit endpoint project-awareness (task 3.1).
Tests that POST /api/ingest/commit saves TTL to project when project_id is provided.
"""
import json
import time
from pathlib import Path

import pytest
from fastapi.testclient import TestClient


@pytest.fixture(autouse=True)
def setup_projects_dir(tmp_path, monkeypatch):
    """Use a temporary directory for projects during tests."""
    monkeypatch.chdir(tmp_path)
    (tmp_path / "projects").mkdir()
    (tmp_path / "uploads").mkdir()
    return tmp_path


@pytest.fixture
def client():
    """Create a test client with only the ingest router."""
    from fastapi import FastAPI
    from explorer.routes.ingest import router

    app = FastAPI()
    app.include_router(router)
    return TestClient(app)


@pytest.fixture
def sample_entities():
    """Sample entities for commit."""
    return [
        {"id": "customer", "label": "Customer", "type": "concept", "description": "A customer entity"},
        {"id": "order", "label": "Order", "type": "concept", "relationships": [
            {"target": "customer", "relation": "belongs_to"}
        ]},
    ]


class TestCommitWithoutProject:
    """Existing behavior: commit without project_id returns TTL only."""

    def test_commit_returns_ttl(self, client, sample_entities):
        resp = client.post("/api/ingest/commit", json={"entities": sample_entities})
        assert resp.status_code == 200
        data = resp.json()
        assert "ttl" in data
        assert data["entity_count"] == 2
        assert "saved_to" not in data
        assert "project_id" not in data

    def test_commit_empty_entities(self, client):
        resp = client.post("/api/ingest/commit", json={"entities": []})
        assert resp.status_code == 400
        assert "No entities" in resp.json()["error"]


class TestCommitWithProject:
    """New behavior: commit with project_id saves TTL to project directory."""

    def test_commit_saves_to_project(self, client, sample_entities, setup_projects_dir):
        project_id = "test_project"
        filename = "extracted.ttl"
        resp = client.post("/api/ingest/commit", json={
            "entities": sample_entities,
            "project_id": project_id,
            "filename": filename,
        })
        assert resp.status_code == 200
        data = resp.json()
        assert data["saved_to"] == filename
        assert data["project_id"] == project_id
        assert data["entity_count"] == 2
        assert "ttl" in data

        # Verify file was actually written
        saved_path = setup_projects_dir / "projects" / project_id / filename
        assert saved_path.exists()
        content = saved_path.read_text(encoding="utf-8")
        assert "Customer" in content
        assert "Order" in content

    def test_commit_auto_generates_filename(self, client, sample_entities, setup_projects_dir):
        project_id = "auto_name_project"
        resp = client.post("/api/ingest/commit", json={
            "entities": sample_entities,
            "project_id": project_id,
        })
        assert resp.status_code == 200
        data = resp.json()
        assert data["project_id"] == project_id
        assert data["saved_to"].startswith("ingest_")
        assert data["saved_to"].endswith(".ttl")

        # Verify file exists
        saved_path = setup_projects_dir / "projects" / project_id / data["saved_to"]
        assert saved_path.exists()

    def test_commit_creates_project_dir_if_missing(self, client, sample_entities, setup_projects_dir):
        project_id = "new_project"
        resp = client.post("/api/ingest/commit", json={
            "entities": sample_entities,
            "project_id": project_id,
            "filename": "first.ttl",
        })
        assert resp.status_code == 200
        project_dir = setup_projects_dir / "projects" / project_id
        assert project_dir.exists()
        assert (project_dir / "first.ttl").exists()

    def test_commit_response_includes_all_fields(self, client, sample_entities):
        resp = client.post("/api/ingest/commit", json={
            "entities": sample_entities,
            "project_id": "my_project",
            "filename": "data.ttl",
        })
        data = resp.json()
        assert "ttl" in data
        assert "entity_count" in data
        assert "saved_to" in data
        assert "project_id" in data

    def test_commit_saved_ttl_is_valid(self, client, sample_entities, setup_projects_dir):
        """Verify the saved TTL can be parsed by rdflib."""
        from rdflib import Graph

        resp = client.post("/api/ingest/commit", json={
            "entities": sample_entities,
            "project_id": "valid_project",
            "filename": "valid.ttl",
        })
        assert resp.status_code == 200

        saved_path = setup_projects_dir / "projects" / "valid_project" / "valid.ttl"
        g = Graph()
        g.parse(str(saved_path), format="turtle")
        assert len(g) >= 2  # At least one triple per entity
