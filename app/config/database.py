from sqlalchemy.ext.asyncio import create_async_engine
from sqlalchemy.pool import NullPool
from app.config.settings import DatabaseSettings

settings = DatabaseSettings()

USERNAME = settings.db_username
PASSWORD = settings.db_password.get_secret_value()
HOST_ADDRESS = settings.db_host_address
PORT = settings.db_port
DATABASE_NAME = settings.db_database_name

# Building Database URL
DATABASE_URL = f"postgresql+asyncpg://{USERNAME}:{PASSWORD}@{HOST_ADDRESS}:{PORT}/{DATABASE_NAME}"

# Creating Async Engine
engine = create_async_engine(
    DATABASE_URL,
    poolclass = NullPool,   # Because our database(aiven)'s free plan doesn't support pooling
    echo = True
)
