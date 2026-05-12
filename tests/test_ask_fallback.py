"""
Tests for Explorer Query Mode endpoints (task 7.1).

Verifies:
- POST /api/ask uses llm_manager.generate() for context QA
- POST /api/ask/project uses llm_manager.generate() for context QA
- POST /api/ask/sparql uses llm_manager.generate() for SPARQL generation when templates don't match
- Fallback behavior: when LLM is unreachable, endpoints return HTTP 200 with raw context

Requirements: 6.1, 6.2, 6.3, 6.5
"""
import pytest
from unittest.mock import patch, MagicMock
from fastapi.testclient import TestClient


@pytest.fixture
def loaded_client(tmp_path, monkeypatch):
    """Create a test client with a loaded graph so context retrieval works."""
    monkeypatch.chdir(tmp_path)
    (tmp_path / "projects").mkdir()

    # Create a minimal TTL file for the graph
    ttl_content = """\
@prefix kg: <http://kg.local/ontology#> .
@prefix kgr: <http://kg.local/resource/> .
@prefix skos: <http://www.w3.org/2004/02/skos/core#> .
@prefix rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .

kgr:Customer a kg:Entity ;
    skos:prefLabel "Customer" ;
    rdfs:comment "A person who buys products" .

kgr:Order a kg:Entity ;
    skos:prefLabel "Order" ;
    kg:belongs_to kgr:Customer .

kgr:Product a kg:Entity ;
    skos:prefLabel "Product" ;
    rdfs:comment "An item for sale" .

kgr:Order kg:contains kgr:Product .
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


class TestAskEndpointFallback:
    """POST /api/ask returns HTTP 200 with raw context when LLM is unreachable."""

    def test_ask_returns_200_with_context_on_llm_failure(self, loaded_client):
        """When LLM raises an exception, /api/ask returns 200 with raw context."""
        with patch("explorer.server.llm_manager") as mock_manager:
            mock_manager.generate.side_effect = ConnectionError("LLM service unreachable")

            resp = loaded_client.post("/api/ask", json={"question": "What is a Customer?"})

        assert resp.status_code == 200
        data = resp.json()
        # Should have an answer field (containing fallback text)
        assert "answer" in data
        # Should have context field with graph data
        assert "context" in data
        # Should indicate LLM error
        assert "llm_error" in data
        # Answer should contain the raw context (not empty)
        assert len(data["answer"]) > 0

    def test_ask_returns_context_nodes_on_llm_failure(self, loaded_client):
        """Fallback response includes context_nodes for UI highlighting."""
        with patch("explorer.server.llm_manager") as mock_manager:
            mock_manager.generate.side_effect = RuntimeError("Connection refused")

            resp = loaded_client.post("/api/ask", json={"question": "Tell me about Customer"})

        assert resp.status_code == 200
        data = resp.json()
        assert "context_nodes" in data
        # Should find Customer node in context
        assert len(data["context_nodes"]) > 0

    def test_ask_no_5xx_on_llm_failure(self, loaded_client):
        """Ensure no 5xx error is returned when LLM fails."""
        with patch("explorer.server.llm_manager") as mock_manager:
            mock_manager.generate.side_effect = Exception("Unexpected LLM error")

            resp = loaded_client.post("/api/ask", json={"question": "What entities exist?"})

        # Must NOT be a 5xx error
        assert resp.status_code < 500
        assert resp.status_code == 200

    def test_ask_success_uses_llm_generate(self, loaded_client):
        """When LLM is available, /api/ask uses llm_manager.generate()."""
        with patch("explorer.server.llm_manager") as mock_manager:
            mock_manager.generate.return_value = "Customer is an entity that buys products."

            resp = loaded_client.post("/api/ask", json={"question": "What is a Customer?"})

        assert resp.status_code == 200
        data = resp.json()
        assert data["answer"] == "Customer is an entity that buys products."
        # Verify generate was called
        mock_manager.generate.assert_called_once()


class TestAskProjectEndpointFallback:
    """POST /api/ask/project returns HTTP 200 with raw context when LLM is unreachable."""

    def test_ask_project_returns_200_on_llm_failure(self, loaded_client):
        """When LLM raises, /api/ask/project returns 200 with raw context."""
        # First, we need to populate new_model_nodes so the endpoint has context
        import explorer.server as srv
        srv.new_model_nodes = [
            {"id": "Customer", "label": "Customer", "type": "Entity"},
            {"id": "Order", "label": "Order", "type": "Entity"},
        ]
        srv.new_model_edges = [
            {"source": "Order", "target": "Customer", "relation": "belongs_to"},
        ]

        with patch("explorer.server.llm_manager") as mock_manager:
            mock_manager.generate.side_effect = ConnectionError("LLM unreachable")

            resp = loaded_client.post("/api/ask/project", json={"question": "What is Customer?"})

        assert resp.status_code == 200
        data = resp.json()
        assert "answer" in data
        assert "context" in data
        assert "llm_error" in data
        assert "context_nodes" in data
        # Answer should contain fallback text with context
        assert len(data["answer"]) > 0

    def test_ask_project_no_5xx_on_llm_failure(self, loaded_client):
        """Ensure no 5xx error when LLM fails on project endpoint."""
        import explorer.server as srv
        srv.new_model_nodes = [
            {"id": "Product", "label": "Product", "type": "Entity"},
        ]
        srv.new_model_edges = []

        with patch("explorer.server.llm_manager") as mock_manager:
            mock_manager.generate.side_effect = TimeoutError("LLM timed out")

            resp = loaded_client.post("/api/ask/project", json={"question": "What is Product?"})

        assert resp.status_code < 500
        assert resp.status_code == 200

    def test_ask_project_success_uses_llm_generate(self, loaded_client):
        """When LLM is available, /api/ask/project uses llm_manager.generate()."""
        import explorer.server as srv
        srv.new_model_nodes = [
            {"id": "Customer", "label": "Customer", "type": "Entity"},
        ]
        srv.new_model_edges = []

        with patch("explorer.server.llm_manager") as mock_manager:
            mock_manager.generate.return_value = "Customer is a core entity."

            resp = loaded_client.post("/api/ask/project", json={"question": "What is Customer?"})

        assert resp.status_code == 200
        data = resp.json()
        assert data["answer"] == "Customer is a core entity."
        mock_manager.generate.assert_called_once()


class TestAskSparqlEndpoint:
    """POST /api/ask/sparql uses template matching first, then LLM for SPARQL generation."""

    def test_sparql_template_matching_no_llm(self, loaded_client):
        """SPARQL endpoint uses template matching for known patterns (no LLM needed)."""
        with patch("explorer.server.llm_manager") as mock_manager:
            # Template-matched questions should NOT call LLM
            resp = loaded_client.post(
                "/api/ask/sparql",
                json={"question": "How many services are there?"},
            )

        assert resp.status_code == 200
        # llm_manager.generate should NOT have been called for template-matched queries
        mock_manager.generate.assert_not_called()

    def test_sparql_uses_llm_when_no_template_matches(self, loaded_client):
        """When no template matches, SPARQL endpoint uses llm_manager.generate() for SPARQL generation."""
        # Use a question that won't match any template
        question = "Find all entities created after 2023"
        generated_sparql = """PREFIX kg: <http://kg.local/ontology#>
PREFIX skos: <http://www.w3.org/2004/02/skos/core#>
SELECT ?label WHERE {
  ?s skos:prefLabel ?label .
  ?s a kg:Entity .
}"""
        with patch("explorer.server.llm_manager") as mock_manager:
            mock_manager.generate.return_value = generated_sparql

            resp = loaded_client.post(
                "/api/ask/sparql",
                json={"question": question},
            )

        assert resp.status_code == 200
        # LLM should have been called to generate SPARQL
        mock_manager.generate.assert_called_once()
        data = resp.json()
        assert "sparql" in data
        assert "answer" in data

    def test_sparql_llm_failure_returns_200_with_fallback(self, loaded_client):
        """When LLM is unreachable and no template matches, returns 200 with keyword-based fallback."""
        # Use a question with keywords that won't match templates but has extractable words
        question = "Describe the architecture of the system"

        with patch("explorer.server.llm_manager") as mock_manager:
            mock_manager.generate.side_effect = ConnectionError("LLM unreachable")

            resp = loaded_client.post(
                "/api/ask/sparql",
                json={"question": question},
            )

        assert resp.status_code == 200
        data = resp.json()
        assert "answer" in data
        assert "sparql" in data

    def test_sparql_llm_failure_no_keywords_returns_200(self, loaded_client):
        """When LLM fails and no keywords can be extracted, returns 200 with context fallback."""
        # Short words that won't pass the length filter and won't match templates
        question = "Do it now"

        with patch("explorer.server.llm_manager") as mock_manager:
            mock_manager.generate.side_effect = ConnectionError("LLM unreachable")

            resp = loaded_client.post(
                "/api/ask/sparql",
                json={"question": question},
            )

        # Should still return 200, not 5xx
        assert resp.status_code == 200

    def test_sparql_no_5xx_on_any_failure(self, loaded_client):
        """Ensure no 5xx error is returned regardless of failure mode."""
        with patch("explorer.server.llm_manager") as mock_manager:
            mock_manager.generate.side_effect = Exception("Total failure")

            resp = loaded_client.post(
                "/api/ask/sparql",
                json={"question": "What is the meaning of everything?"},
            )

        assert resp.status_code < 500

    def test_sparql_returns_results_without_llm(self, loaded_client):
        """SPARQL endpoint returns structured results from template matching."""
        resp = loaded_client.post(
            "/api/ask/sparql",
            json={"question": "What is related to Customer?"},
        )
        assert resp.status_code == 200
        data = resp.json()
        # Should have answer and sparql fields
        assert "answer" in data
        assert "sparql" in data

    def test_sparql_empty_question_returns_400(self, loaded_client):
        """Empty question returns 400."""
        resp = loaded_client.post("/api/ask/sparql", json={"question": ""})
        assert resp.status_code == 400


class TestAskEndpointValidation:
    """Basic validation for ask endpoints."""

    def test_ask_empty_question_returns_400(self, loaded_client):
        """Empty question returns 400."""
        resp = loaded_client.post("/api/ask", json={"question": ""})
        assert resp.status_code == 400

    def test_ask_project_empty_question_returns_400(self, loaded_client):
        """Empty question returns 400."""
        resp = loaded_client.post("/api/ask/project", json={"question": ""})
        assert resp.status_code == 400
