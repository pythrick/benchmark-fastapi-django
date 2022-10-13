from functools import lru_cache
from pathlib import Path

from pydantic import BaseSettings
from pydantic import PostgresDsn

BASE_PATH = Path(__file__).parent.parent


class Settings(BaseSettings):
    app_name: str = "FastAPI POC"
    database_url: PostgresDsn

    class Config:
        env_file = BASE_PATH / ".env"


@lru_cache()
def get_settings() -> Settings:
    return Settings()


settings = get_settings()
