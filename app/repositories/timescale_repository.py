from app.repositories.base_repository import BaseRepository
from app.models.timescale import StockTimescale
from sqlalchemy.ext.asyncio import AsyncSession
from typing import Optional, List
from sqlalchemy.future import select
from app.exceptions.repository_errors import NotFoundError, RepositoryError
from sqlalchemy.exc import SQLAlchemyError


class TimescaleRepository(BaseRepository[StockTimescale]):
    def __init__(self, db: AsyncSession):
        super().__init__(StockTimescale, db)

    async def get_stockdata_by_ticker(self, ticker: str) -> Optional[List[StockTimescale]]:
        try:
            stmt = select(StockTimescale).where(StockTimescale.ticker == ticker)
            result = await self.db.execute(stmt)
            data = result.scalars().all()
            if not data:
                raise NotFoundError(f"stock data with ticker {ticker} not found")
            return data
        except SQLAlchemyError as e:
            raise RepositoryError(f"Database error on get_stockdata_by_ticker: {e}")
