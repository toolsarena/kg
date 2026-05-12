"""Unit tests for LLM provider selection and reconfiguration.

Validates: Requirements 7.1, 10.1
"""

import os
import tempfile
from pathlib import Path
from unittest.mock import patch, MagicMock

import yaml
import pytest

from llm.provider import get_llm, load_config, _build_provider, LLMProviderManager
from llm.ollama import OllamaProvider
from llm.bedrock import BedrockProvider
from llm.openai import OpenAIProvider


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------

def _write_config(tmp_dir: Path, provider: str, **extra) -> str:
    """Write a config.yaml with the given provider and return its path."""
    cfg = {"llm": {"provider": provider, **extra}}
    config_path = tmp_dir / "config.yaml"
    config_path.write_text(yaml.dump(cfg), encoding="utf-8")
    return str(config_path)


# ---------------------------------------------------------------------------
# Tests: get_llm() returns correct provider class
# ---------------------------------------------------------------------------

class TestGetLlmProviderSelection:
    """Test that get_llm() returns the correct provider class for each config."""

    def test_get_llm_returns_ollama_provider(self, tmp_path):
        config_path = _write_config(tmp_path, "ollama", model="llama3", base_url="http://localhost:11434")
        provider = get_llm(config_path)
        assert isinstance(provider, OllamaProvider)
        assert provider.model == "llama3"
        assert provider.base_url == "http://localhost:11434"

    @patch("llm.bedrock.boto3.client")
    def test_get_llm_returns_bedrock_provider(self, mock_boto_client, tmp_path):
        mock_boto_client.return_value = MagicMock()
        config_path = _write_config(tmp_path, "bedrock", model="anthropic.claude-3-haiku-20240307-v1:0", region="us-west-2")
        provider = get_llm(config_path)
        assert isinstance(provider, BedrockProvider)
        assert provider.model_id == "anthropic.claude-3-haiku-20240307-v1:0"
        assert provider.region == "us-west-2"

    def test_get_llm_returns_openai_provider(self, tmp_path):
        config_path = _write_config(tmp_path, "openai", model="gpt-4o", api_key="sk-test123")
        provider = get_llm(config_path)
        assert isinstance(provider, OpenAIProvider)
        assert provider.model == "gpt-4o"
        assert provider.api_key == "sk-test123"

    def test_get_llm_defaults_to_ollama_when_config_missing(self):
        """When config.yaml doesn't exist, defaults to Ollama."""
        provider = get_llm("/nonexistent/path/config.yaml")
        assert isinstance(provider, OllamaProvider)
        assert provider.model == "qwen2.5-coder:7b"

    def test_get_llm_raises_on_unknown_provider(self, tmp_path):
        config_path = _write_config(tmp_path, "unknown_provider")
        with pytest.raises(ValueError, match="Unknown LLM provider: unknown_provider"):
            get_llm(config_path)


# ---------------------------------------------------------------------------
# Tests: LLMProviderManager.reconfigure() switches provider type
# ---------------------------------------------------------------------------

class TestLLMProviderManagerReconfigure:
    """Test that LLMProviderManager.reconfigure() switches between provider types."""

    def test_initial_provider_from_config(self, tmp_path):
        config_path = _write_config(tmp_path, "ollama", model="test-model")
        manager = LLMProviderManager(config_path)
        assert isinstance(manager.provider, OllamaProvider)
        assert manager.provider.model == "test-model"

    @patch("llm.bedrock.boto3.client")
    def test_reconfigure_ollama_to_bedrock(self, mock_boto_client, tmp_path):
        mock_boto_client.return_value = MagicMock()
        config_path = _write_config(tmp_path, "ollama")
        manager = LLMProviderManager(config_path)
        assert isinstance(manager.provider, OllamaProvider)

        manager.reconfigure({"provider": "bedrock", "model": "anthropic.claude-3-haiku-20240307-v1:0", "region": "eu-west-1"})
        assert isinstance(manager.provider, BedrockProvider)
        assert manager.provider.region == "eu-west-1"

    def test_reconfigure_ollama_to_openai(self, tmp_path):
        config_path = _write_config(tmp_path, "ollama")
        manager = LLMProviderManager(config_path)
        assert isinstance(manager.provider, OllamaProvider)

        manager.reconfigure({"provider": "openai", "model": "gpt-4o", "api_key": "sk-new"})
        assert isinstance(manager.provider, OpenAIProvider)
        assert manager.provider.model == "gpt-4o"
        assert manager.provider.api_key == "sk-new"

    @patch("llm.bedrock.boto3.client")
    def test_reconfigure_openai_to_bedrock(self, mock_boto_client, tmp_path):
        mock_boto_client.return_value = MagicMock()
        config_path = _write_config(tmp_path, "openai", api_key="sk-old")
        manager = LLMProviderManager(config_path)
        assert isinstance(manager.provider, OpenAIProvider)

        manager.reconfigure({"provider": "bedrock", "model": "anthropic.claude-3-sonnet-20240229-v1:0"})
        assert isinstance(manager.provider, BedrockProvider)

    def test_reconfigure_updates_config_property(self, tmp_path):
        config_path = _write_config(tmp_path, "ollama", model="old-model")
        manager = LLMProviderManager(config_path)
        assert manager.config["model"] == "old-model"

        manager.reconfigure({"provider": "ollama", "model": "new-model"})
        assert manager.config["provider"] == "ollama"
        assert manager.config["model"] == "new-model"


# ---------------------------------------------------------------------------
# Tests: Manager delegates generate() and generate_json() to active provider
# ---------------------------------------------------------------------------

class TestLLMProviderManagerDelegation:
    """Test that the manager delegates generate/generate_json to the active provider."""

    def test_generate_delegates_to_provider(self, tmp_path):
        config_path = _write_config(tmp_path, "ollama")
        manager = LLMProviderManager(config_path)

        with patch.object(manager._provider, "generate", return_value="test response") as mock_gen:
            result = manager.generate("hello", system="sys")
            mock_gen.assert_called_once_with("hello", "sys")
            assert result == "test response"

    def test_generate_json_delegates_to_provider(self, tmp_path):
        config_path = _write_config(tmp_path, "ollama")
        manager = LLMProviderManager(config_path)

        with patch.object(manager._provider, "generate_json", return_value={"key": "value"}) as mock_gen:
            result = manager.generate_json("give json", system="be json")
            mock_gen.assert_called_once_with("give json", "be json")
            assert result == {"key": "value"}

    @patch("llm.bedrock.boto3.client")
    def test_generate_uses_new_provider_after_reconfigure(self, mock_boto_client, tmp_path):
        mock_boto_client.return_value = MagicMock()
        config_path = _write_config(tmp_path, "ollama")
        manager = LLMProviderManager(config_path)

        # Reconfigure to bedrock
        manager.reconfigure({"provider": "bedrock", "model": "claude-test"})

        with patch.object(manager._provider, "generate", return_value="bedrock response") as mock_gen:
            result = manager.generate("prompt")
            mock_gen.assert_called_once_with("prompt", "")
            assert result == "bedrock response"


# ---------------------------------------------------------------------------
# Tests: load_config and _build_provider edge cases
# ---------------------------------------------------------------------------

class TestLoadConfigAndBuildProvider:
    """Test config loading and provider building edge cases."""

    def test_load_config_returns_defaults_for_missing_file(self):
        cfg = load_config("/does/not/exist.yaml")
        assert cfg["llm"]["provider"] == "ollama"
        assert cfg["llm"]["model"] == "qwen2.5-coder:7b"

    def test_load_config_reads_yaml_file(self, tmp_path):
        config_path = _write_config(tmp_path, "openai", model="gpt-4")
        cfg = load_config(config_path)
        assert cfg["llm"]["provider"] == "openai"
        assert cfg["llm"]["model"] == "gpt-4"

    def test_build_provider_sets_default_api_key_from_env(self, tmp_path):
        with patch.dict(os.environ, {"OPENAI_API_KEY": "sk-env-key"}, clear=False):
            provider = _build_provider({"provider": "openai", "model": "gpt-4o"})
            assert isinstance(provider, OpenAIProvider)
            assert provider.api_key == "sk-env-key"

    def test_build_provider_config_api_key_takes_precedence(self, tmp_path):
        """Config-specified api_key should take precedence over env var (setdefault behavior)."""
        with patch.dict(os.environ, {"OPENAI_API_KEY": "sk-env-key"}, clear=False):
            provider = _build_provider({"provider": "openai", "model": "gpt-4o", "api_key": "sk-config-key"})
            assert isinstance(provider, OpenAIProvider)
            assert provider.api_key == "sk-config-key"

    @patch("llm.bedrock.boto3.client")
    def test_build_provider_sets_default_region_from_env(self, mock_boto_client, tmp_path):
        mock_boto_client.return_value = MagicMock()
        with patch.dict(os.environ, {"AWS_DEFAULT_REGION": "ap-southeast-1"}, clear=False):
            provider = _build_provider({"provider": "bedrock", "model": "claude-test"})
            assert isinstance(provider, BedrockProvider)
            assert provider.region == "ap-southeast-1"
