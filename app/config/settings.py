from pydantic import SecretStr
from pydantic_settings import BaseSettings

class DatabaseSettings(BaseSettings):
  db_username: str
  db_password: SecretStr
  ip_address: str
  port: int
  database_name: str
  class Config:
    env_file = ".env"
    env_file_encoding = "utf-8"

# if __name__ == "__main__":
#     settings = DatabaseSettings()

#     settings.model_dump()
    #print(f"postgress://{settings.db_username}:{settings.db_password.get_secret_value()}@{settings.ip_address}:{settings.port}/{settings.database_name}")