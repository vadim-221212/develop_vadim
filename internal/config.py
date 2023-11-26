from pydantic import BaseSettings

class Settings(BaseSettings):
   SECRET_KEY: str
   ALGORITHM: str
   ACCESS_TOKEN_EXPIRE_MINUTES: int

settings = Settings()