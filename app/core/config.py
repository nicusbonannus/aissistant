from pathlib import Path

from pydantic_settings import BaseSettings

# Obtener la ruta absoluta basada en la ubicación del script
BASE_DIR = Path(__file__).resolve().parent.parent
GOOGLE_CLIENT_JSON_PATH = str(BASE_DIR / "client.json")
GOOGLE_TOKEN_JSON_PATH = str(BASE_DIR / "token.json")


class Settings(BaseSettings):
    app_name: str = "AIssistant"
    admin_email: str = ""
    database_url: str = ""
    secret_key: str = ""
    debug: bool = True
    llm_secret_key: str = ""
    GOOGLE_CLIENT_JSON_PATH: str = GOOGLE_CLIENT_JSON_PATH
    GOOGLE_TOKEN_JSON_PATH: str = GOOGLE_TOKEN_JSON_PATH

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"


settings = Settings()
