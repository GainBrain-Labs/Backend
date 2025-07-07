from app.graphql.types.stock import Stock, CreateStockInput, CreateDefaultStockGroupInput, DefaultStockGroup, CreateCustomStockGroupInput, CustomStockGroup, CreateStockGroupCompositionInput, StockGroupComposition
from app.core.dependencies import get_user_context
from app.mappers import stock_mappers
from typing import Optional, List


async def get_stocks() -> Optional[List[Stock]]:
    ctx = await get_user_context()
    stock_service = ctx["stock_service"]
    return await stock_service.get_stocks()

async def add_stock(stock: CreateStockInput) -> Optional[Stock]:
    ctx = await get_user_context()
    stock_service = ctx["stock_service"]
    add_stock_input = stock_mappers.add_stock_input(stock)
    return await stock_service.add_stock(add_stock_input)

async def add_default_stock_group(default_stock_group:CreateDefaultStockGroupInput) -> Optional[DefaultStockGroup]:
    ctx = await get_user_context()
    stock_service = ctx["stock_service"]
    default_stock_group_input = stock_mappers.add_default_stock_group_input(default_stock_group)
    return await stock_service.create_default_stock_group(default_stock_group_input)

async def add_custom_stock_group(custom_stock_group:CreateCustomStockGroupInput) -> Optional[CustomStockGroup]:
    ctx = await get_user_context()
    stock_service = ctx["stock_service"]
    custom_stock_group_input = stock_mappers.add_custom_stock_group_input(custom_stock_group)
    return await stock_service.create_custom_stock_group(custom_stock_group_input)

async def add_stock_group_composition(stock_group_composition:CreateStockGroupCompositionInput ) -> Optional[StockGroupComposition]:
    ctx = await get_user_context()
    stock_service = ctx["stock_service"]
    stock_group_composition_input = stock_mappers.add_stock_group_composition_input(stock_group_composition)
    return await stock_service.create_stock_group_composition(stock_group_composition_input)


