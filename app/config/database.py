from sqlalchemy.ext.asyncio import create_async_engine
from sqlalchemy.pool import NullPool
from settings import DatabaseSettings

settings = DatabaseSettings()

USERNAME = settings.db_username
PASSWORD = settings.db_password
HOST_ADDRESS = settings.db_host_address
PORT = settings.db_port
DATABASE_NAME = settings.db_database_name

# Building Database URL
DATABASE_URL = f"postgres://{USERNAME}:{PASSWORD}@{HOST_ADDRESS}:{PORT}/{DATABASE_NAME}"

# Creating Async Engine
engine = create_async_engine(
    DATABASE_URL,
    poolclass = NullPool,   # Because our database(aiven)'s free plan doesn't support pooling
    echo = True
)
