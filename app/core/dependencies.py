from typing import AsyncGenerator, Dict
from app.db.session import session_manager
from sqlalchemy.ext.asyncio import AsyncSession
from app.repositories.user_repository import UserRepository
from contextlib import asynccontextmanager
from app.services.user_service import UserService

async def get_db() -> AsyncGenerator[AsyncSession, None]:
    async with session_manager.session() as session:
        yield session

async def get_user_context() -> dict[str, UserService]:
    async with session_manager.session() as session:
        user_repo = UserRepository(session)
        user_service = UserService(user_repo)
        return {
            "user_service": user_service,
        }
