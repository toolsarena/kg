from abc import ABC, abstractmethod
import os
import yaml
from pathlib import Path
from dotenv import load_dotenv

# Load .env at module import time (Requirement 7.5)
load_dotenv()


class LLMProvider(ABC):
    @abstractmethod
    def generate(self, prompt: str, system: str = "") -> str:
        pass

    @abstractmethod
    def generate_json(self, prompt: str, system: str = "") -> dict:
        pass


def load_config(config_path: str = "config.yaml") -> dict:
    path = Path(config_path)
    if not path.exists():
        # Fall back to defaults if config.yaml is missing
        return {"llm": {"provider": "ollama", "model": "qwen2.5-coder:7b",
                        "base_url": "http://localhost:11434",
                        "temperature": 0.1, "max_tokens": 4096}}
    with open(path) as f:
        return yaml.safe_load(f)


def _build_provider(llm_cfg: dict) -> "LLMProvider":
    """Build an LLMProvider instance from a config dict, overlaying env vars."""
    # Overlay environment variables for secrets
    llm_cfg.setdefault("api_key", os.getenv("OPENAI_API_KEY", ""))
    llm_cfg.setdefault("region", os.getenv("AWS_DEFAULT_REGION", "us-east-1"))

    provider = llm_cfg.get("provider", "ollama")
    if provider == "ollama":
        from llm.ollama import OllamaProvider
        return OllamaProvider(llm_cfg)
    elif provider == "bedrock":
        from llm.bedrock import BedrockProvider
        return BedrockProvider(llm_cfg)
    elif provider == "openai":
        from llm.openai import OpenAIProvider
        return OpenAIProvider(llm_cfg)
    raise ValueError(f"Unknown LLM provider: {provider}")


def get_llm(config_path: str = "config.yaml") -> "LLMProvider":
    """Create an LLMProvider from config.yaml with .env overlay."""
    cfg = load_config(config_path)
    llm_cfg = dict(cfg.get("llm", {}))
    return _build_provider(llm_cfg)


class LLMProviderManager:
    """Holds the active LLM provider instance. Supports runtime reconfiguration.

    This is the single entry point for all LLM calls in the application.
    Routes and agents call generate()/generate_json() on this manager
    instead of importing provider instances directly.
    """

    def __init__(self, config_path: str = "config.yaml"):
        self._config_path = config_path
        cfg = load_config(config_path)
        self._current_config: dict = dict(cfg.get("llm", {}))
        self._provider: LLMProvider = _build_provider(dict(self._current_config))

    @property
    def provider(self) -> LLMProvider:
        """Access the underlying LLMProvider instance (for agent layer)."""
        return self._provider

    @property
    def config(self) -> dict:
        """Access the current LLM configuration dict."""
        return dict(self._current_config)

    def reconfigure(self, new_config: dict):
        """Rebuild provider from new settings (called when UI changes config).

        Args:
            new_config: Dict with keys like provider, model, base_url,
                        temperature, max_tokens, region, api_key.
        """
        self._current_config = dict(new_config)
        self._provider = _build_provider(dict(new_config))

    def generate(self, prompt: str, system: str = "") -> str:
        """Generate text from the active LLM provider."""
        return self._provider.generate(prompt, system)

    def generate_json(self, prompt: str, system: str = "") -> dict:
        """Generate a JSON response from the active LLM provider."""
        return self._provider.generate_json(prompt, system)
