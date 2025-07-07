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

class CreateStock(BaseModel):
    name: str
    ticker: str

class CreateStockGroup(BaseModel):
    name: str
    ticker: str
    type: str

class CreateDefaultStockGroup(CreateStockGroup):
    stock_group_type:  str

class CreateCustomStockGroup(CreateStockGroup):
    user_id: int

class CreateStockGroupComposition(BaseModel):
    stock_group_id: int
    stock_id: int