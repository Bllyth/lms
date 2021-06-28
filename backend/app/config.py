import os

from pydantic import BaseSettings, Field


class Settings(BaseSettings):
    DB_URL: str = Field(..., env='DATABASE_URL')
    SECRET_KEY: str = Field(..., env='SECRET_KEY')
    ALGORITHM: str = Field(..., env='ALGORITHM')
    ACCESS_TOKEN_EXPIRE_MINUTES: str = Field(..., env='ACCESS_TOKEN_EXPIRE_MINUTES')


settings = Settings()
