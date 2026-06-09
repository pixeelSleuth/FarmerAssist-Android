from pydantic_settings import BaseSettings
from pydantic import ConfigDict, Field
from typing import Optional


class Settings(BaseSettings):

    MYSQL_HOST: str
    MYSQL_PORT: int
    MYSQL_USER: str
    MYSQL_PASSWORD: str
    MYSQL_DB: str

    MONGO_URI: str = ""

    REDIS_HOST: str
    REDIS_PORT: int

    FIREBASE_CREDENTIALS: str
    FIREBASE_API_KEY: str
    JWT_SECRET:str
    OPENWEATHER_API_KEY: str
    SARVAM_API_KEY: str
    BASE_URL:str
    GEMINI_API_KEY: Optional[str] = Field(None, alias="gemini_api_key")
    MONGODB_URI: Optional[str] = Field(None, alias="mongodb_uri")
    MONGODB_DB: Optional[str] = Field(None, alias="mongodb_db")
    SARVAM_STT_URL: Optional[str] = Field(None, alias="sarvam_stt_url")
    SARVAM_TTS_URL: Optional[str] = Field(None, alias="sarvam_tts_url")

    model_config = ConfigDict(
        env_file=".env",
        extra="ignore",
        populate_by_name=True
    )


settings = Settings()