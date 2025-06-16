from sqlalchemy.ext.asyncio import create_async_engine
from sqlalchemy.pool import AsyncAdaptedQueuePool
from app.config.settings import DatabaseSettings
import ssl

settings = DatabaseSettings()

USERNAME = settings.db_username
PASSWORD = settings.db_password.get_secret_value()
HOST_ADDRESS = settings.db_host_address
DATABASE_NAME = settings.db_database_name

# Building Database URL
DATABASE_URL = f"postgresql+asyncpg://{USERNAME}:{PASSWORD}@{HOST_ADDRESS}/{DATABASE_NAME}"

ssl_context = ssl.create_default_context()

# Creating Async Engine with pooling
engine = create_async_engine(
    DATABASE_URL,
    echo=True,
    poolclass=AsyncAdaptedQueuePool,
    pool_size=10,          # max number of connections to keep in the pool
    max_overflow=20,       # how many overflow connections can be opened beyond pool_size
    pool_timeout=30,       # seconds to wait before giving up on getting a connection
    pool_recycle=1800,     # connections older than this (in seconds) will be recycled
    connect_args={"ssl": ssl_context}
)
