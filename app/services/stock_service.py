from app.repositories.base_repository import BaseRepository
from app.schemas.stock import CreateStock, CreateDefaultStockGroup, CreateCustomStockGroup, CreateStockGroupComposition
from typing import Optional, List
from app.exceptions.repository_errors import FoundError, NotFoundError
from app.config.logger import logger
from app.mapperServiceToDB import stock_mappers

class StockService():
    def __init__(self, stock_repository:BaseRepository):
        self.stock_repository = stock_repository

    async def get_stocks(self):
        return await self.stock_repository.get_all()

    async def add_stock(self,stock: CreateStock):
        try:
            try:
                stock = await self.stock_repository.get_stock_by_ticker(stock.ticker)
                if stock:
                    raise FoundError(f"stock with ticker {stock.ticker} already exists")
            except NotFoundError as e:
                logger.info("stock not found")
            except Exception:
                raise
        except Exception:
            raise
        else:
            create_stock_input = stock_mappers.stock_service_to_db(stock)
            return await self.stock_repository.create(create_stock_input)
        
    async def create_default_stock_group(self,stock_group_data:CreateDefaultStockGroup):
        try:
            try:
                stock_group = await self.stock_repository.get_stock_group_by_ticker(stock_group_data.ticker)
                if stock_group:
                    raise FoundError(f"stock group with ticker {stock_group_data.ticker} already exists")
            except NotFoundError as e:
                logger.info("stock group not found")
            except Exception:
                raise
        except Exception:
            raise
        else:
            create_stock_group_input = stock_mappers.default_stock_group_service_to_db(stock_group_data)
            return await self.stock_repository.create(create_stock_group_input)
        
    async def create_custom_stock_group(self,stock_group_data:CreateCustomStockGroup):
        try:
            try:
                stock_group = await self.stock_repository.get_stock_group_by_ticker(stock_group_data.ticker)
                if stock_group:
                    raise FoundError(f"stock group with ticker {stock_group_data.ticker} already exists")
            except NotFoundError as e:
                logger.info("stock group not found")
            except Exception:
                raise
        except Exception:
            raise
        else:
            create_stock_group_input = stock_mappers.custom_stock_group_service_to_db(stock_group_data)
            return await self.stock_repository.create(create_stock_group_input)
        
    async def create_stock_group_composition(self,stock_group_composition:CreateStockGroupComposition):
        try:
            try:
                stock_group_composition = await self.stock_repository.get_stock_group_composition(stock_group_composition.stock_group_id, stock_group_composition.stock_id)
                if stock_group_composition:
                    raise FoundError(f"stock group composition with stock group id {stock_group_composition.stock_group_id} and stock id {stock_group_composition.stock_id} already exists")
            except NotFoundError as e:
                logger.info("stock group composition not found")
            except Exception:
                raise
        except Exception:
            raise
        else:
            create_stock_group_composition_input = stock_mappers.stock_group_composition_service_to_db(stock_group_composition)
            return await self.stock_repository.create(create_stock_group_composition_input)
  


        
