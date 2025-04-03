from pathlib import Path

from pydantic_settings import BaseSettings

# Obtener la ruta absoluta basada en la ubicación del script
BASE_DIR = Path(__file__).resolve().parent.parent
GOOGLE_CLIENT_JSON_PATH = str(BASE_DIR / "client.json")
GOOGLE_TOKEN_JSON_PATH = str(BASE_DIR / "token.json")

LLM_SYSTEM_PROMPT = (
    "Eres un asistente que se encarga de llevar mi agenda. Se eficiente y conciso. "
    "Me gusta trabajar de 9 a 18, con una hora de almuerzo entre las 12 y las 14hs. "
    "Mi horario de trabajo mas fuerte es de 14 a 18hs."
    "Me levanto a las 6.40, no me gusta hacer cosas después de las 20hs."
)


class Settings(BaseSettings):
    APP_NAME: str = "AIssistant"
    DATABASE_URL: str = ""
    SECRET_KEY: str = ""
    DEBUG: bool = True
    # GOOGLE CALENDAR
    GOOGLE_CLIENT_JSON_PATH: str = GOOGLE_CLIENT_JSON_PATH
    GOOGLE_TOKEN_JSON_PATH: str = GOOGLE_TOKEN_JSON_PATH
    # LLM
    LLM_SECRET_KEY: str = ""
    LLM_SYSTEM_PROMPT: str = LLM_SYSTEM_PROMPT
    LLM_MODEL_NAME: str = "deepseek-ai/DeepSeek-V3"
    LLM_PROVIDER_URL: str = "https://api.kluster.ai/v1"

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"


settings = Settings()
