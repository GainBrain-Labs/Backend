from sqlalchemy.ext.asyncio import AsyncSession
from typing import TypeVar, Generic, Type, Optional
from sqlalchemy.future import select
from sqlalchemy.exc import SQLAlchemyError
from app.exceptions.repository_errors import RepositoryError, NotFoundError, CreationError, DeletionError

ModelType = TypeVar("ModelType")

class BaseRepository(Generic[ModelType]):
    def __init__(self, model: Type[ModelType], db: AsyncSession):
        self.model = model
        self.db = db
    
    async def create(self, instance: ModelType) -> ModelType:
        """
        Add a new row based on the provided instance.
        """
        try:
            self.db.add(instance)
            await self.db.commit()
            await self.db.refresh(instance)
            return instance
        except SQLAlchemyError as e:
            await self.db.rollback()
            raise CreationError(f"Failed to create {self.model.__name__}: {e}")
        
    async def get_by_id(self, id_: int) -> Optional[ModelType]:
        try:
            stmt = select(self.model).where(self.model.id == id_)
            result = await self.db.execute(stmt)
            item = result.scalar_one_or_none()
            if not item:
                raise NotFoundError(f"{self.model.__name__} with ID {id_} not found")
            return item
        except SQLAlchemyError as e:
            raise RepositoryError(f"Database error on get_by_id: {e}")
        
    async def get_all(self) -> list[ModelType]:
        try:
            stmt = select(self.model)
            result = await self.db.execute(stmt)
            return list(result.scalars().all())  # https://chatgpt.com/share/684ffd96-3470-800c-9b3c-76cc21744212
        except SQLAlchemyError as e:
            raise RepositoryError(f"Database error on get_all: {e}")
        
    async def delete(self, instance: ModelType) -> None:
        try:
            await self.db.delete(instance)
            await self.db.commit()
        except SQLAlchemyError as e:
            await self.db.rollback()
            raise DeletionError(f"Failed to delete {self.model.__name__}: {e}")
