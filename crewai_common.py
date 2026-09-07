"""
CrewAI Shared Helper - Dynamic LLM resolution & configuration
Supports standard OpenAI, TokenRouter, Groq, Ollama, or custom endpoints.
"""
import os
from crewai import LLM


def resolve_llm(model: str = None) -> LLM:
    """
    Constructs a configured CrewAI LLM instance dynamically.
    Detects OPENAI_API_KEY or TOKENROUTER_API_KEY and custom OPENAI_BASE_URL.
    """
    api_key = os.getenv("OPENAI_API_KEY") or os.getenv("TOKENROUTER_API_KEY") or "mock-key-for-local-init"
    base_url = os.getenv("OPENAI_BASE_URL")
    model_name = model or os.getenv("OPENAI_MODEL_NAME") or "gpt-4o-mini"

    kwargs = {
        "model": model_name,
        "api_key": api_key
    }
    if base_url:
        kwargs["base_url"] = base_url

    return LLM(**kwargs)


def has_valid_api_key() -> bool:
    """Checks if an actual API key is present in environment"""
    key = os.getenv("OPENAI_API_KEY") or os.getenv("TOKENROUTER_API_KEY")
    return bool(key and key != "your_openai_api_key_here" and len(key) > 5)
