from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    DATA_DIR: str = "data/uploads"

    class Config:
        env_file = ".env"

settings = Settings()