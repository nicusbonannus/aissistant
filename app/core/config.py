from pathlib import Path

from pydantic_settings import BaseSettings

# Obtener la ruta absoluta basada en la ubicación del script
BASE_DIR = Path(__file__).resolve().parent.parent
GOOGLE_CLIENT_JSON_PATH = str(BASE_DIR / "client.json")
GOOGLE_TOKEN_JSON_PATH = str(BASE_DIR / "token.json")

SYSTEM_PROMPT = (
    "Eres un asistente que se encarga de llevar mi agenda. "
    "Me gusta trabajar de 9 a 18, con una hora de almuerzo entre las 12 y las 14hs. "
    "Me levanto a las 6.40, no me gusta hacer cosas después de las 20hs."
)


class Settings(BaseSettings):
    app_name: str = "AIssistant"
    admin_email: str = ""
    database_url: str = ""
    secret_key: str = ""
    debug: bool = True
    llm_secret_key: str = ""
    GOOGLE_CLIENT_JSON_PATH: str = GOOGLE_CLIENT_JSON_PATH
    GOOGLE_TOKEN_JSON_PATH: str = GOOGLE_TOKEN_JSON_PATH
    SYSTEM_PROMPT: str = SYSTEM_PROMPT

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"


settings = Settings()
