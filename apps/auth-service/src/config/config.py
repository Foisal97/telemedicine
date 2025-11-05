from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    # MongoDB connection (example: mongodb+srv://user:pass@cluster0.mongodb.net/telemedicine)
    MONGO_URI: str
    DB_NAME: str = "telemedicine"

    # JWT
    JWT_SECRET: str = "supersecret123"
    JWT_ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 60
    REFRESH_TOKEN_EXPIRE_DAYS: int = 7

    FRONTEND_URL: str = "http://localhost:5173"

    class Config:
        env_file = ".env"
        case_sensitive = True

settings = Settings()
