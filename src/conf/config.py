from pydantic_settings import BaseSettings
from pydantic import BaseModel, EmailStr, SecretStr, HttpUrl, Field
from typing import Optional, List
from pathlib import Path


class Settings(BaseSettings):
    # Database settings
    POSTGRES_DB: str = "hw7_db"
    POSTGRES_USER: str = "postgres"
    POSTGRES_PASSWORD: str = "123456"
    POSTGRES_HOST: str = "localhost"
    POSTGRES_PORT: str = "5432"
    DB_URL: str = "postgresql+asyncpg://postgres:123456@localhost:5432/hw7_db"

    # Redis settings
    REDIS_URL: str = "redis://localhost"
    REDIS_HOST: str = "localhost"
    REDIS_PORT: int = 6379
    REDIS_DB: int = 0

    # JWT settings
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 30
    REFRESH_TOKEN_EXPIRE_DAYS: int = 7
    SECRET_KEY: str = "your-secret-key-here"
    ALGORITHM: str = "HS256"


    # Mail settings
    MAIL_USERNAME: str = "example@ukr.net"
    MAIL_PASSWORD: str = "secretPassword"
    MAIL_FROM: EmailStr = "example@ukr.net"
    MAIL_PORT: int = 465
    MAIL_SERVER: str = "smtp.ukr.net"
    MAIL_FROM_NAME: str = "Contact- app"
    MAIL_STARTTLS: bool = False
    MAIL_SSL_TLS: bool = True
    USE_CREDENTIALS: bool = True
    VALIDATE_CERTS: bool = True
    TEMPLATE_FOLDER: Path = Path(__file__).parent / "templates"

    # Cloudinary settings
    CLD_NAME: str
    # CLD_API_KEY: int = 123456789
    CLD_API_KEY: int = 191275896727463
    CLD_API_SECRET: str = "secret"

    class Config:
        env_file = ".env"
        case_sensitive = True
        extra = "allow"


settings = Settings()
