from app.repositories.base_repository import BaseRepository
from app.models.portfolio import Portfolio, PortfolioComposition
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.future import select
from app.exceptions.repository_errors import NotFoundError, RepositoryError

class PortfolioRepository(BaseRepository[Portfolio]):
    def __init__(self, db: AsyncSession):
        super().__init__(Portfolio, db)
    
    async def get_portfolio(self,name:str, user_id:int):
        try:
            stmt = select(Portfolio).where(Portfolio.name == name and Portfolio.user_id == user_id)
            result = await self.db.execute(stmt)
            postfolio = result.scalar_one_or_none()
            if not postfolio:
                raise NotFoundError(f"portfolio with name {name} and user id {user_id} not found")
            return Portfolio
        except SQLAlchemyError as e:
            raise RepositoryError(f"Database error on get_portfolio: {e}")
    
    async def get_portfolio_composition(self,portfolio_id: int, stock_group_id: int):
        try:
            stmt = select(PortfolioComposition).where(PortfolioComposition.stock_group_id == stock_group_id and PortfolioComposition.portfolio_id == portfolio_id)
            result = await self.db.execute(stmt)
            portfolio_composition = result.scalar_one_or_none()
            if not portfolio_composition:
                raise NotFoundError(f"portfolio composition with portfolio id {portfolio_id} and stock group id {stock_group_id} not found")
            return portfolio_composition
        except SQLAlchemyError as e:
            raise RepositoryError(f"Database error on get_portfolio_composition: {e}")
