from pydantic import BaseModel
import datetime

class StockTicker(BaseModel):
    ticker: str

class StockData(BaseModel):
    ticker: str
    date: datetime.date
    open_price: float
    close_price: float
    high_price: float
    low_price: float
    volume: float