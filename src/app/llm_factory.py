import os
from typing import Any
from langchain_google_genai import ChatGoogleGenerativeAI
from .settings import settings

def configure_langsmith_env() -> None:
    # Propaga variáveis para o runtime do LangChain/LangSmith
    os.environ["LANGCHAIN_TRACING_V2"] = "true" if settings.langchain_tracing_v2 else "false"
    if settings.langchain_api_key:
        os.environ["LANGCHAIN_API_KEY"] = settings.langchain_api_key
    if settings.langchain_project:
        os.environ["LANGCHAIN_PROJECT"] = settings.langchain_project
    if settings.langsmith_endpoint:
        os.environ["LANGSMITH_ENDPOINT"] = settings.langsmith_endpoint

def make_llm(**overrides: Any) -> ChatGoogleGenerativeAI:
    """
    Fabrica um ChatGoogleGenerativeAI baseado no .env
    Permite overrides como: temperature=0.2, max_output_tokens=...
    """
    configure_langsmith_env()
    llm = ChatGoogleGenerativeAI(
        model=settings.gemini_model,
        google_api_key=settings.google_api_key,
        # parâmetros comuns; ajuste conforme necessidade:
        temperature=overrides.get("temperature", 0.2),
        convert_system_message_to_human=True,  # ajuda com alguns providers
    )
    return llm
