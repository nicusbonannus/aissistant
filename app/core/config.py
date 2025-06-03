import os
from pathlib import Path

from pydantic_settings import BaseSettings

# Defines the absolute route for these files
BASE_DIR = Path(__file__).resolve().parent.parent
GOOGLE_CLIENT_JSON_PATH = str(BASE_DIR / "client.json")
GOOGLE_TOKEN_JSON_PATH = str(BASE_DIR / "token.json")
LANGCHAIN_TRACING_V2 = os.getenv("LANGCHAIN_TRACING_V2")
LANGCHAIN_PROJECT = os.getenv("LANGCHAIN_PROJECT")
LANGCHAIN_API_KEY = os.getenv("LANGCHAIN_API_KEY")

LLM_SYSTEM_PROMPT = (
    "Sos un entrenador de gymnasio y nutricionista. "
    "Tu tarea es ayudar a los usuarios a armar rutinas de ejercicios y controlar sus dietas."
    "Se directo con la rutina."
)


class Settings(BaseSettings):
    APP_NAME: str = "AIssistant"
    DATABASE_URL: str = os.getenv(
        "DATABASE_URL", "mysql://root:zyrl_root@db:3306/aissistant"
    )
    DEBUG: bool = True
    SECRET_KEY: str = ""
    # GOOGLE CALENDAR
    GOOGLE_CLIENT_JSON_PATH: str = GOOGLE_CLIENT_JSON_PATH
    GOOGLE_TOKEN_JSON_PATH: str = GOOGLE_TOKEN_JSON_PATH
    # LLM
    LLM_SECRET_KEY: str = ""
    LLM_SYSTEM_PROMPT: str = LLM_SYSTEM_PROMPT
    LLM_MODEL_NAME: str = "deepseek-ai/DeepSeek-V3"
    LLM_PROVIDER_URL: str = "https://api.kluster.ai/v1"
    # LangChain
    LANGCHAIN_API_KEY: str = ""
    LANGCHAIN_PROJECT: str = "default"
    LANGCHAIN_TRACING_V2: bool = True

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"


settings = Settings()
