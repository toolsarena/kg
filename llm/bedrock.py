import json
import boto3
from llm.provider import LLMProvider


class BedrockProvider(LLMProvider):
    def __init__(self, config: dict):
        self.model_id = config.get("model", "anthropic.claude-3-haiku-20240307-v1:0")
        self.region = config.get("region", "us-east-1")
        self.temperature = config.get("temperature", 0.1)
        self.max_tokens = config.get("max_tokens", 4096)
        self.client = boto3.client("bedrock-runtime", region_name=self.region)

    def generate(self, prompt: str, system: str = "") -> str:
        messages = [{"role": "user", "content": [{"type": "text", "text": prompt}]}]
        body = {
            "anthropic_version": "bedrock-2023-05-31",
            "max_tokens": self.max_tokens,
            "temperature": self.temperature,
            "messages": messages,
        }
        if system:
            body["system"] = system

        resp = self.client.invoke_model(
            modelId=self.model_id,
            contentType="application/json",
            accept="application/json",
            body=json.dumps(body),
        )
        result = json.loads(resp["body"].read())
        return result["content"][0]["text"]

    def generate_json(self, prompt: str, system: str = "") -> dict:
        system = (system or "") + "\nYou MUST respond with valid JSON only. No markdown, no explanation."
        raw = self.generate(prompt, system)
        raw = raw.strip()
        if raw.startswith("```"):
            raw = raw.split("\n", 1)[1] if "\n" in raw else raw[3:]
            if raw.endswith("```"):
                raw = raw[:-3]
            raw = raw.strip()
        return json.loads(raw)
