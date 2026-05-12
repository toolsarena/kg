import json
import requests
from llm.provider import LLMProvider


class OllamaProvider(LLMProvider):
    def __init__(self, config: dict):
        self.model = config.get("model", "qwen2.5-coder:7b")
        self.base_url = config.get("base_url", "http://localhost:11434")
        self.temperature = config.get("temperature", 0.1)
        self.max_tokens = config.get("max_tokens", 4096)

    def generate(self, prompt: str, system: str = "") -> str:
        payload = {
            "model": self.model,
            "prompt": prompt,
            "system": system,
            "stream": False,
            "options": {
                "temperature": self.temperature,
                "num_predict": self.max_tokens,
            },
        }
        resp = requests.post(f"{self.base_url}/api/generate", json=payload, timeout=300)
        resp.raise_for_status()
        return resp.json()["response"]

    def generate_json(self, prompt: str, system: str = "") -> dict:
        system = system + "\nYou MUST respond with valid JSON only. No markdown, no explanation."
        raw = self.generate(prompt, system)
        # strip markdown fences if model wraps it
        raw = raw.strip()
        if raw.startswith("```"):
            raw = raw.split("\n", 1)[1] if "\n" in raw else raw[3:]
            if raw.endswith("```"):
                raw = raw[:-3]
            raw = raw.strip()
        return json.loads(raw)
