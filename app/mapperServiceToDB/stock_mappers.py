from app.models.timescale import StockTimescale
from app.schemas.stock import StockData

def stock_data_service_to_db(data:StockData) -> StockTimescale:
    return StockTimescale(
        ticker = data.ticker,
        date = data.date,
        open_price = data.open_price,
        close_price = data.close_price,
        high_price = data.high_price,
        low_price = data.low_price,
        volume = data.volume
    )