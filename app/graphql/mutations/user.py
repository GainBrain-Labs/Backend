import strawberry
from app.graphql.types.user import User, createUserInput
from app.graphql.resolvers.user_resolver import create_user
# from strawberry.field_extensions import InputMutationExtension

@strawberry.type
class Mutation:
    @strawberry.mutation
    def create_user(self,user:createUserInput) -> User:
        return create_user(user)
