from app.repositories.base_repository import BaseRepository
from app.models.user import User
from sqlalchemy.ext.asyncio import AsyncSession
from typing import Optional
from sqlalchemy.future import select
from app.exceptions.repository_errors import RepositoryError, NotFoundError
from sqlalchemy.exc import SQLAlchemyError

class UserRepository(BaseRepository[User]):
    def __init__(self, db: AsyncSession):
        super().__init__(User, db)
    
    async def get_by_email(self, email: str) -> Optional[User]:
        try:
            stmt = select(User).where(User.email == email)
            result = await self.db.execute(stmt)
            user = result.scalar_one_or_none()
            if not user:
                raise NotFoundError(f"User with email {email} not found")
            return user
        except SQLAlchemyError as e:
            raise RepositoryError(f"Database error on get_by_email: {e}")

    async def get_by_username(self, username: str) -> Optional[User]:
        try:
            stmt = select(User).where(User.username == username)
            result = await self.db.execute(stmt)
            user = result.scalar_one_or_none()
            if not user:
                raise NotFoundError(f"User with email {username} not found")
            return user
        except SQLAlchemyError as e:
            raise RepositoryError(f"Database error on get_by_email: {e}")
            