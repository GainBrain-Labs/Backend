from app.graphql.types.stock import StockTickerInput
from app.schemas.stock import StockTicker
def stock_tiker_input(ticker:StockTickerInput) -> StockTicker:
    return StockTicker(
        ticker = ticker.ticker
    )