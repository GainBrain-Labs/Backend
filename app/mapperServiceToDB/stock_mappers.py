from app.models.timescale import StockTimescale
from app.models.stock import Stock, DefaultStockGroup, CustomStockGroup, StockGroupComposition
from app.schemas.stock import StockData, CreateStock, CreateDefaultStockGroup, CreateCustomStockGroup, CreateStockGroupComposition

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

def stock_service_to_db(stock:CreateStock) -> Stock:
    return Stock(
        name = stock.name,
        ticker = stock.ticker
    )

def default_stock_group_service_to_db(stock_group: CreateDefaultStockGroup) -> DefaultStockGroup:
    return DefaultStockGroup(
        name = stock_group.name,
        ticker = stock_group.ticker,
        type = stock_group.type,
        stock_group_type = stock_group.stock_group_type
    )

def custom_stock_group_service_to_db(stock_group: CreateCustomStockGroup) -> CustomStockGroup:
    return CustomStockGroup(
        name = stock_group.name,
        ticker = stock_group.ticker,
        type = stock_group.type,
        user_id = stock_group.user_id
    )

def stock_group_composition_service_to_db(stock_group_composition:CreateStockGroupComposition) -> StockGroupComposition:
    return StockGroupComposition(
        stock_group_id = stock_group_composition.stock_group_id,
        stock_id = stock_group_composition.stock_id
    )