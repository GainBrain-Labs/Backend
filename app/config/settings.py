from pydantic import SecretStr
from pydantic_settings import BaseSettings

class DatabaseSettings(BaseSettings):
  db_username: str
  db_password: SecretStr
  db_host_address: str
  db_database_name: str
  class Config:
    env_file = ".env"
    env_file_encoding = "utf-8"
