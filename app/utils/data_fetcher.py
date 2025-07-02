import yfinance as yf
from app.schemas.stock import StockTicker, StockData
from typing import List

def get_stock_data_default(ticker:StockTicker) -> List[StockData]:
    stock_data = yf.download(ticker.ticker, start='2015-04-01', end='2025-04-01')
    data = []
    for row in stock_data.itertuples(index = True):
        data.append(
            StockData(
                ticker=ticker.ticker,
                date=row[0].date(),
                open_price=row[4],
                close_price=row[1],
                high_price=row[2],
                low_price=row[3],
                volume=row[5]
            )
        )
    return data
