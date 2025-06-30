import strawberry
from app.graphql.types.stock import StockData, StockTickerInput
from app.graphql.resolvers.data_resolver import fetch_add_data
from typing import List

@strawberry.type
class DataMutations:
    @strawberry.mutation
    def fetch_add_data(self,ticker: StockTickerInput) -> List[StockData]:
        return fetch_add_data(ticker)
