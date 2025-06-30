from app.schemas.stock import StockData, StockTicker
from app.repositories.base_repository import BaseRepository
import datetime
from app.utils.data_fetcher import get_stock_data_default
from app.mapperServiceToDB import stock_mappers

class DataService():
    def __init__(self, timescale_repository:BaseRepository):
        self.timescale_repository = timescale_repository
    async def fetch_add_data(self,ticker:StockTicker):
        data = get_stock_data_default(ticker)
        for stock_data in data:
            stock_data_db = stock_mappers.stock_data_service_to_db(stock_data)
            await self.timescale_repository.create(stock_data_db)
        return data
