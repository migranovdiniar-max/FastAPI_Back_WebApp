from os import getenv
from pydantic_settings import BaseSettings
from pydantic import BaseModel


class DBSettings(BaseModel):
    url: str = "sqlite+aiosqlite:///./db.sqlite3"
    echo: bool = False

class Settings(BaseSettings):
    api_v1_prefix: str = "/api/v1"

    db: DBSettings = DBSettings()


settings = Settings()