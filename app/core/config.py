from pathlib import Path

from pydantic_settings import BaseSettings

# Obtener la ruta absoluta basada en la ubicación del script
BASE_DIR = Path(__file__).resolve().parent.parent
google_client_json_path = str(BASE_DIR / "client.json")
google_token_json_path = str(BASE_DIR / "token.json")


class Settings(BaseSettings):
    app_name: str = "AIssistant"
    admin_email: str = ""
    database_url: str = ""
    secret_key: str = ""
    debug: bool = True
    llm_secret_key: str = ""
    google_client_json_path: str = google_client_json_path
    google_token_json_path: str = google_token_json_path

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"


settings = Settings()
