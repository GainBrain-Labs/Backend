import strawberry
from app.graphql.queries.user import UserQueries
from app.graphql.mutations.user import UserMutations
from app.graphql.mutations.data import DataMutations

@strawberry.type
class Query(UserQueries):
    pass

@strawberry.type
class Mutation(UserMutations,DataMutations):
    pass

schema = strawberry.Schema(query=Query, mutation=Mutation)