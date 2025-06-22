import contextlib
from typing import AsyncIterator
from sqlalchemy.ext.asyncio import (
    AsyncConnection,
    AsyncSession,
    async_sessionmaker,
)
from app.config.database import engine
from app.config.logger import logger

class DatabaseSessionManager:
    def __init__ (self, engine):
        
        logger.info("Creating database session")
        
        self._engine = engine
        self._sessionmaker = async_sessionmaker(
            bind=engine, 
            autoflush=False,
            autocommit=False,
            expire_on_commit=False,
            class_=AsyncSession
        )
    
    async def close(self):
        
        logger.info("Closing database session")
        
        if self._engine:
            await self._engine.dispose()
            
        self._engine = None
        self._sessionmaker = None
        
    @contextlib.asynccontextmanager
    async def connect(self) -> AsyncIterator[AsyncConnection]:
        
        logger.info("Connecting to Database")
        
        if self._engine is None:
            logger.error("DatabaseSessionManager is not initialized")
            return

        async with self._engine.begin() as connection:
            try:
                yield connection
            except Exception:
                await connection.rollback()
                logger.error("Connection to Database failed")
            
    @contextlib.asynccontextmanager
    async def session(self) -> AsyncIterator[AsyncSession]:
        if self._sessionmaker is None:
            logger.error("DatabaseSessionManager is not initialized")
            return

        session = self._sessionmaker()
        try:
            yield session
        except Exception as e:
            await session.rollback()
            logger.error(f"Database session error: {e!r}")
        finally:
            await session.close()
            
session_manager = DatabaseSessionManager(engine=engine)
