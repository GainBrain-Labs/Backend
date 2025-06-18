import strawberry
from app.graphql.types.user import User, CreateUserInput
from app.graphql.resolvers.user_resolver import create_user

@strawberry.type
class UserMutations:
    @strawberry.mutation
    def create_user(self,user:CreateUserInput) -> User:
        return create_user(user)
