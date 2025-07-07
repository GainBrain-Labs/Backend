from app.repositories.base_repository import BaseRepository
from app.models.stock import Stock, StockGroup, StockGroupComposition
from sqlalchemy.ext.asyncio import AsyncSession
from typing import Optional
from sqlalchemy.future import select
from app.exceptions.repository_errors import NotFoundError, RepositoryError
from sqlalchemy.exc import SQLAlchemyError

class StockRepository(BaseRepository[Stock]):
    def __init__(self, db: AsyncSession):
        super().__init__(Stock, db)

    async def get_stock_by_ticker(self,ticker:str) -> Optional[Stock]:
        try:
            stmt = select(Stock).where(Stock.ticker == ticker)
            result = await self.db.execute(stmt)
            stock = result.scalar_one_or_none()
            if not stock:
                raise NotFoundError(f"stock with ticker {ticker} not found")
            return stock
        except SQLAlchemyError as e:
            raise RepositoryError(f"Database error on get_stock_by_ticker: {e}")
        
    async def get_stock_group_by_ticker(self,ticker:str) -> Optional[StockGroup]:
        try:
            stmt = select(StockGroup).where(StockGroup.ticker == ticker)
            result = await self.db.execute(stmt)
            stock = result.scalar_one_or_none()
            if not stock:
                raise NotFoundError(f"stock group with ticker {ticker} not found")
            return stock
        except SQLAlchemyError as e:
            raise RepositoryError(f"Database error on get_stock_group_by_ticker: {e}")
        
    async def get_stock_group_composition(self,stock_group_id:int, stock_id:int) -> Optional[StockGroupComposition]:
        try:
            stmt = select(StockGroupComposition).where(StockGroupComposition.stock_group_id == stock_group_id and StockGroupComposition.stock_id == stock_id)
            result = await self.db.execute(stmt)
            stock = result.scalar_one_or_none()
            if not stock:
                raise NotFoundError(f"stock group composition with stock group id {stock_group_id} and stock id {stock_id} not found")
            return stock
        except SQLAlchemyError as e:
            raise RepositoryError(f"Database error on get_stock_group_composition: {e}")
    

            