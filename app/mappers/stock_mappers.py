from app.graphql.types.stock import StockTickerInput, CreateStockInput, CreateDefaultStockGroupInput, CreateCustomStockGroupInput, CreateStockGroupCompositionInput
from app.schemas.stock import CreateStock,StockTicker, CreateDefaultStockGroup, CreateCustomStockGroup, CreateStockGroupComposition
def stock_tiker_input(ticker:StockTickerInput) -> StockTicker:
    return StockTicker(
        ticker = ticker.ticker
    )

def add_stock_input(stock:CreateStockInput) -> CreateStock:
    return CreateStock(
        name=stock.name,
        ticker = stock.ticker
    )

def add_default_stock_group_input(default_stock_group:CreateDefaultStockGroupInput) -> CreateDefaultStockGroup:
    return CreateDefaultStockGroup(
        name = default_stock_group.name,
        ticker = default_stock_group.ticker,
        type = "default",
        stock_group_type = default_stock_group.stock_group_type
    )

def add_custom_stock_group_input(custom_stock_group:CreateCustomStockGroupInput) -> CreateCustomStockGroup:
    return CreateCustomStockGroup(
        name = custom_stock_group.name,
        ticker = custom_stock_group.ticker,
        type = "custom",
        user_id = custom_stock_group.user_id
    )

def add_stock_group_composition_input(stock_group_composition:CreateStockGroupCompositionInput) -> CreateStockGroupComposition:
    return CreateStockGroupComposition(
        stock_group_id = stock_group_composition.stock_group_id,
        stock_id = stock_group_composition.stock_id
    )