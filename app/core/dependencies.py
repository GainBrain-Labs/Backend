from typing import AsyncGenerator
from app.db.session import session_manager
from sqlalchemy.ext.asyncio import AsyncSession
from app.repositories.user_repository import UserRepository
from app.services.user_service import UserService
from app.services.auth_service import AuthService

async def get_db() -> AsyncGenerator[AsyncSession, None]:
    async with session_manager.session() as session:
        yield session

async def get_user_context():
    async for session in get_db():
        user_repo = UserRepository(session)
        return {
            "user_service": UserService(user_repo),
            "auth_service": AuthService(user_repo)
        }
