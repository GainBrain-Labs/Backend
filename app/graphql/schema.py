import strawberry
from app.graphql.queries.user import Query
from app.graphql.mutations.user import Mutation

schema = strawberry.Schema(query=Query, mutation=Mutation)