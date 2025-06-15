from functools import lru_cache
from pydantic import BaseSettings

class Settings(BaseSettings):
    api_v1_prefix: str = "/api/v1"
    secret_key: str
    postgres_dsn: str

    class Config:
        env_file = ".env"

@lru_cache
def get_settings() -> Settings:
    return Settings()
