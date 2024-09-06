# config.py
from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    DATABASE_URL: str = "postgresql://neondb_owner:CY62wPRHcvqe@ep-noisy-cake-a5fr8att.us-east-2.aws.neon.tech/neondb?sslmode=require&options=project%3Dep-noisy-cake-a5fr8att"
    SECRET_KEY: str = "your-secret-key"
    ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 30

settings = Settings()