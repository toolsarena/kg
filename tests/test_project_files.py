"""
Tests for project file management endpoints (task 4.1).
Tests POST /api/projects/{id}/files, POST /api/projects/{id}/upload,
and GET /api/projects/{id} file metadata.
"""
import json
import shutil
import tempfile
from pathlib import Path
from unittest.mock import patch

import pytest
from fastapi.testclient import TestClient

# Patch PROJECTS_DIR before importing the router
_test_projects_dir = Path(tempfile.mkdtemp())


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
def sample_project(setup_projects_dir):
    """Create a sample project for testing."""
    project_dir = setup_projects_dir / "test_project"
    project_dir.mkdir()
    meta = {"name": "Test Project", "id": "test_project", "created": 1000.0, "modified": 1000.0}
    (project_dir / "meta.json").write_text(json.dumps(meta))
    return "test_project"


class TestCreateFile:
    """Tests for POST /api/projects/{id}/files."""

    def test_create_empty_file(self, client, sample_project):
        resp = client.post(f"/api/projects/{sample_project}/files", json={"filename": "ontology.ttl"})
        assert resp.status_code == 200
        data = resp.json()
        assert data["created"] is True
        assert data["filename"] == "ontology.ttl"
        assert data["project_id"] == sample_project

    def test_create_file_adds_ttl_extension(self, client, sample_project):
        resp = client.post(f"/api/projects/{sample_project}/files", json={"filename": "mymodel"})
        assert resp.status_code == 200
        assert resp.json()["filename"] == "mymodel.ttl"

    def test_create_file_no_filename(self, client, sample_project):
        resp = client.post(f"/api/projects/{sample_project}/files", json={"filename": ""})
        assert resp.status_code == 400
        assert "No filename" in resp.json()["error"]

    def test_create_file_project_not_found(self, client):
        resp = client.post("/api/projects/nonexistent/files", json={"filename": "test.ttl"})
        assert resp.status_code == 404

    def test_create_file_already_exists(self, client, sample_project, setup_projects_dir):
        # Create the file first
        (setup_projects_dir / sample_project / "existing.ttl").write_text("# existing")
        resp = client.post(f"/api/projects/{sample_project}/files", json={"filename": "existing.ttl"})
        assert resp.status_code == 400
        assert "already exists" in resp.json()["error"]

    def test_create_file_sanitizes_filename(self, client, sample_project):
        resp = client.post(f"/api/projects/{sample_project}/files", json={"filename": "my file!@#.ttl"})
        assert resp.status_code == 200
        # Only safe chars remain
        assert resp.json()["filename"] == "myfile.ttl"


class TestUploadFile:
    """Tests for POST /api/projects/{id}/upload."""

    def test_upload_valid_ttl(self, client, sample_project):
        ttl_content = b"""@prefix ex: <http://example.org/> .
ex:Thing a ex:Class .
"""
        resp = client.post(
            f"/api/projects/{sample_project}/upload",
            files={"file": ("test.ttl", ttl_content, "text/turtle")},
        )
        assert resp.status_code == 200
        data = resp.json()
        assert data["uploaded"] is True
        assert data["filename"] == "test.ttl"
        assert data["project_id"] == sample_project
        assert data["triples"] >= 1
        assert data["size"] == len(ttl_content)

    def test_upload_invalid_ttl(self, client, sample_project):
        bad_content = b"this is not valid turtle syntax {{{"
        resp = client.post(
            f"/api/projects/{sample_project}/upload",
            files={"file": ("bad.ttl", bad_content, "text/turtle")},
        )
        assert resp.status_code == 400
        assert "Invalid TTL" in resp.json()["error"]

    def test_upload_non_ttl_extension(self, client, sample_project):
        resp = client.post(
            f"/api/projects/{sample_project}/upload",
            files={"file": ("data.csv", b"a,b,c", "text/csv")},
        )
        assert resp.status_code == 400
        assert "Only .ttl" in resp.json()["error"]

    def test_upload_project_not_found(self, client):
        ttl_content = b"@prefix ex: <http://example.org/> .\nex:A a ex:B .\n"
        resp = client.post(
            "/api/projects/nonexistent/upload",
            files={"file": ("test.ttl", ttl_content, "text/turtle")},
        )
        assert resp.status_code == 404


class TestGetProjectFileMetadata:
    """Tests for GET /api/projects/{id} returning full file metadata."""

    def test_get_project_returns_file_metadata(self, client, sample_project, setup_projects_dir):
        # Create a TTL file with known content
        ttl = "@prefix ex: <http://example.org/> .\nex:A a ex:B .\nex:C ex:rel ex:D .\n"
        project_dir = setup_projects_dir / sample_project
        (project_dir / "model.ttl").write_text(ttl, encoding="utf-8")

        resp = client.get(f"/api/projects/{sample_project}")
        assert resp.status_code == 200
        data = resp.json()

        assert "files" in data
        assert len(data["files"]) == 1

        file_info = data["files"][0]
        assert file_info["name"] == "model.ttl"
        assert "size" in file_info
        assert file_info["size"] > 0
        assert "modified" in file_info
        assert file_info["modified"] > 0
        assert "triples" in file_info
        assert file_info["triples"] >= 1

    def test_get_project_multiple_files(self, client, sample_project, setup_projects_dir):
        project_dir = setup_projects_dir / sample_project
        (project_dir / "a.ttl").write_text("@prefix ex: <http://example.org/> .\nex:A a ex:B .\n")
        (project_dir / "b.ttl").write_text("@prefix ex: <http://example.org/> .\nex:C a ex:D .\n")

        resp = client.get(f"/api/projects/{sample_project}")
        data = resp.json()

        assert data["file_count"] == 2
        assert len(data["files"]) == 2
        # Each file has full metadata
        for f in data["files"]:
            assert "name" in f
            assert "size" in f
            assert "modified" in f
            assert "triples" in f
