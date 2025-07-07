from app.repositories.base_repository import BaseRepository
from app.schemas.portfolio import CreatePortfolio, CreatePortfolioComposition
from app.exceptions.repository_errors import FoundError, NotFoundError
from app.config.logger import logger
from app.mapperServiceToDB import portfolio_mapper

class PortfolioService():
    def __init__(self, portfolio_repository:BaseRepository):
        self.portfolio_repository = portfolio_repository

    async def add_portfolio(self,portfolio_data: CreatePortfolio):
        try:
            try:
                portfolio = await self.portfolio_repository.get_portfolio(portfolio_data.name, portfolio_data.user_id)
                if portfolio:
                    raise FoundError(f"portfolio with name {portfolio_data.name} and user id {portfolio_data.user_id} already exists")
            except NotFoundError as e:
                logger.info("portfolio not found")
            except Exception:
                raise
        except Exception:
            raise
        else:
            add_portfolio_input = portfolio_mapper.add_portfolio_to_db(portfolio_data)
            return await self.portfolio_repository.create(add_portfolio_input)
        
    async def add_portfolio_composition(self,portfolio_composition_data: CreatePortfolioComposition):
        try:
            try:
                portfolio_composition = await self.portfolio_repository.get_portfolio_composition(portfolio_composition_data.portfolio_id, portfolio_composition_data.stock_group_id)
                if portfolio_composition:
                    raise FoundError(f"portfolio composition with portfolio id {portfolio_composition_data.portfolio_id} and stock group id {portfolio_composition_data.stock_group_id} already exists")
            except NotFoundError as e:
                logger.info("portfolio composition not found")
            except Exception:
                raise
        except Exception:
            raise
        else:
            add_portfolio_composition_input = portfolio_mapper.add_portfolio_composition_to_db(portfolio_composition_data)
            return await self.portfolio_repository.create(add_portfolio_composition_input)
