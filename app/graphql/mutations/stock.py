import strawberry
from app.graphql.types.stock import CreateStockInput, Stock, CreateDefaultStockGroupInput, DefaultStockGroup, CreateCustomStockGroupInput, CustomStockGroup, CreateStockGroupCompositionInput, StockGroupComposition
from typing import Optional
from app.graphql.resolvers.stock_resolver import add_stock, add_default_stock_group, add_custom_stock_group, add_stock_group_composition

@strawberry.type
class StockMutations:
    @strawberry.mutation
    def add_stock(self,stock:CreateStockInput) -> Optional[Stock]:
        return add_stock(stock)

    
    @strawberry.mutation
    def add_default_stock_group(self,default_stock_group:CreateDefaultStockGroupInput) -> Optional[DefaultStockGroup]:
        return add_default_stock_group(default_stock_group)

    
    @strawberry.mutation
    def add_custom_stock_group(self,custom_stock_group:CreateCustomStockGroupInput) -> Optional[CustomStockGroup]:
        return add_custom_stock_group(custom_stock_group)

    @strawberry.mutation
    def add_stock_group_composition(self,stock_group_composition:CreateStockGroupCompositionInput) -> Optional[StockGroupComposition]:
        return add_stock_group_composition(stock_group_composition)

    