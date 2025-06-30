from app.graphql.types.stock import StockTickerInput, StockData
from typing import List, Optional
from app.core.dependencies import get_user_context
from app.mappers import stock_mappers

async def fetch_add_data(ticker:StockTickerInput) -> List[StockData]:
    ctx = await get_user_context()
    data_service = ctx["data_service"]
    ticker_input = stock_mappers.stock_tiker_input(ticker)
    return await data_service.fetch_add_data(ticker_input)
    
