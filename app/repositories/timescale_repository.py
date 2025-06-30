from app.repositories.base_repository import BaseRepository
from app.models.timescale import StockTimescale
from sqlalchemy.ext.asyncio import AsyncSession


class TimescaleRepository(BaseRepository[StockTimescale]):
    def __init__(self, db: AsyncSession):
        super().__init__(StockTimescale, db)
