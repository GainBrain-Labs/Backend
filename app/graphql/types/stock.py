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


@strawberry.input
class StockTickerInput:
    ticker: str