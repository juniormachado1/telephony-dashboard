import os
from pydantic_settings import BaseSettings
from typing import List

class Settings(BaseSettings):
    # Configurações do Banco de Dados
    DATABASE_URL: str = "postgresql://user:password@hostname:5432/db_name"
    TEST_DATABASE_URL: str

    # Configurações de Segurança e JWT
    SECRET_KEY: str = "0bdaymjWVF27QR"
    ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 60 * 24 * 7  # 7 dias

    # API externa de chamadas
    EXTERNAL_CALLS_API_URL: str = "http://217.196.61.183/calls"

    # Arquivo .env
    class Config:
        env_file = ".env"
        env_file_encoding = 'utf-8'

# Instância única das configurações para ser importada em outros módulos
settings = Settings()