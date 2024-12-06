from enum import Enum
from functools import lru_cache

from pydantic import Field, PostgresDsn
from pydantic_settings import BaseSettings, SettingsConfigDict


class LogLevel(str, Enum):
    critical = "critical"
    error = "error"
    warning = "warning"
    info = "info"
    debug = "debug"
    trace = "trace"


class Settings(BaseSettings):
    database_uri: PostgresDsn

    host: str = "127.0.0.1"
    port: int = Field(default=8000, gt=0, lt=65535)
    workers: int | None = None
    proxy_headers: bool = False
    log_level: LogLevel = LogLevel.info
    
    model_config = SettingsConfigDict(env_file=(".env", ".env.local", ".env.prod"), extra="ignore")


@lru_cache
def get_settings():
    return Settings()


settings = get_settings()