import os

from dotenv import load_dotenv
from pydantic import BaseSettings, Field

load_dotenv()


class Settings(BaseSettings):
    DATABASE_URL: str
    SECRET_KEY: str
    ALGORITHM: str
    ACCESS_TOKEN_EXPIRE_MINUTES: int

    # class Config:
    #     env_file = '.env'
    class Config:
        env_file = ".env"
        case_sensitive = True


settings = Settings()
