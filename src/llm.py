import json, os
import httpx
from dotenv import load_dotenv
load_dotenv()

def llm_json(prompt: str, fallback: dict) -> dict:
    key = os.getenv("LLM_API_KEY")
    url = os.getenv("LLM_API_URL")
    model = os.getenv("LLM_MODEL")
    if not key or not url or not model:
        return {**fallback, "mode": "demo"}

    # Generic OpenAI-compatible request. Adapt this small adapter for Claude or another provider.
    payload = {
        "model": model,
        "messages": [
            {"role": "system", "content": "Return valid JSON only. Never invent missing business facts."},
            {"role": "user", "content": prompt},
        ],
        "temperature": 0.2,
        "response_format": {"type": "json_object"},
    }
    headers = {"Authorization": f"Bearer {key}", "Content-Type": "application/json"}
    with httpx.Client(timeout=30) as client:
        response = client.post(url, headers=headers, json=payload)
        response.raise_for_status()
        content = response.json()["choices"][0]["message"]["content"]
        return {**json.loads(content), "mode": "live_llm"}
