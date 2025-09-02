from pydantic_settings import BaseSettings, SettingsConfigDict
from pydantic import Field

class Settings(BaseSettings):
    # Google / Gemini
    google_api_key: str = Field(alias="GOOGLE_API_KEY")
    gemini_model: str = Field(default="gemini-2.5-flash-lite", alias="GEMINI_MODEL")

    # LangSmith / LangChain
    langchain_tracing_v2: bool = Field(default=True, alias="LANGCHAIN_TRACING_V2")
    langchain_api_key: str | None = Field(default=None, alias="LANGCHAIN_API_KEY")
    langchain_project: str | None = Field(default=None, alias="LANGCHAIN_PROJECT")
    langsmith_endpoint: str | None = Field(default=None, alias="LANGSMITH_ENDPOINT")

    # App
    app_env: str = Field(default="dev", alias="APP_ENV")
    app_timeout: int = Field(default=60, alias="APP_TIMEOUT")

    model_config = SettingsConfigDict(env_file=".env", env_file_encoding="utf-8", extra="ignore")

settings = Settings()
