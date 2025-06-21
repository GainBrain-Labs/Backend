from typing import AsyncGenerator
from app.db.session import session_manager
from sqlalchemy.ext.asyncio import AsyncSession
from app.repositories.user_repository import UserRepository
from app.services.user_service import UserService
from app.services.auth_service import AuthService
from contextlib import asynccontextmanager

async def get_db() -> AsyncGenerator[AsyncSession, None]:
    async with session_manager.session() as session:
        yield session

@asynccontextmanager
async def get_user_context():
    async with session_manager.session() as session:
        user_repo = UserRepository(session)
        yield {
            "user_service": UserService(user_repo),
            "auth_service": AuthService(user_repo)
        }
