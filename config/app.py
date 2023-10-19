import logging
import os
from functools import lru_cache

from pydantic import AnyUrl, BaseSettings

log = logging.getLogger("uvicorn")


class Settings(BaseSettings):
    ALLOWED_ORIGINS: str
    APP_ENVIRONMENT: str
    DATABASE_HOST: str
    DATABASE_NAME: str
    DATABASE_USERNAME: str
    DATABASE_PASSWORD: str
    
    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"


@lru_cache()
def get_settings() -> BaseSettings:
    log.info("Loading config settings from the environment...")
    return Settings()


settings = Settings()