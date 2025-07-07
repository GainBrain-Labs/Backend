import strawberry
import datetime

@strawberry.type
class StockData:
    ticker: str
    date: datetime.date
    open_price: float
    close_price: float
    high_price: float
    low_price: float
    volume: float

@strawberry.type
class Stock:
    name: str
    ticker: str


@strawberry.input
class StockTickerInput:
    ticker: str

@strawberry.input
class CreateStockInput:
    name: str
    ticker: str

@strawberry.type
class StockGroup:
    name: str
    ticker: str
    type: str

@strawberry.input
class StockGroupInput:
    name: str
    ticker: str

@strawberry.type
class DefaultStockGroup(StockGroup):
    stock_group_type: str

@strawberry.input
class CreateDefaultStockGroupInput(StockGroupInput):
    stock_group_type: str

@strawberry.type
class CustomStockGroup(StockGroup):
    user_id: int

@strawberry.input
class CreateCustomStockGroupInput(StockGroupInput):
    user_id: int

@strawberry.type
class StockGroupComposition:
    stock_group_id: int
    stock_id: int

@strawberry.input
class CreateStockGroupCompositionInput:
    stock_group_id: int
    stock_id: int
