import strawberry
from typing import List
from app.graphql.types.stock import  Stock
from app.graphql.resolvers.stock_resolver import get_stocks

@strawberry.type
class StockQueries:
    stocks: List[Stock] = strawberry.field(resolver=get_stocks)
