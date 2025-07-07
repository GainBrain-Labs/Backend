import strawberry
from app.graphql.queries.user import UserQueries
from app.graphql.queries.stock import StockQueries
from app.graphql.mutations.user import UserMutations
from app.graphql.mutations.data import DataMutations
from app.graphql.mutations.stock import StockMutations
from app.graphql.mutations.portfolio import PortfolioMutation

@strawberry.type
class Query(UserQueries, StockQueries):
    pass

@strawberry.type
class Mutation(UserMutations, DataMutations, StockMutations, PortfolioMutation):
    pass

schema = strawberry.Schema(query=Query, mutation=Mutation)