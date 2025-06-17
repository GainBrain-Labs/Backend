import strawberry
from app.graphql.queries.user import UserQueries
from app.graphql.mutations.user import UserMutations

@strawberry.type
class Query(UserQueries):
    pass

@strawberry.type
class Mutation(UserMutations):
    pass

schema = strawberry.Schema(query=Query, mutation=Mutation)