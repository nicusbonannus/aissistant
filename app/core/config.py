import openai
from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    app_name: str = "AIssistant"
    admin_email: str = ""
    database_url: str = ""
    secret_key: str = ""
    debug: bool = True
    llm_secret_key: str

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"


settings = Settings()

openai.api_key = settings.llm_secret_key
