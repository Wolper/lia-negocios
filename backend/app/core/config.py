from pydantic_settings import BaseSettings
from functools import lru_cache
from typing import List


class Settings(BaseSettings):
    PROJECT_NAME: str = "LIA Negócios Backend"
    DATABASE_URL: str
    SECRET_KEY: str
    JWT_ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 30
    REFRESH_TOKEN_EXPIRE_DAYS: int = 7
    BACKEND_CORS_ORIGINS: List[str] = []

    class Config:
        env_file = ".env"
        case_sensitive = True


@lru_cache
def get_settings() -> Settings:
    settings = Settings()

    if isinstance(settings.BACKEND_CORS_ORIGINS, str):
        origins = [
            o.strip() for o in settings.BACKEND_CORS_ORIGINS.split(",") if o.strip()
        ]
        settings.BACKEND_CORS_ORIGINS = origins

    return settings


settings = get_settings()
