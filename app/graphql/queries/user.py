import strawberry
from typing import List, Optional
from app.graphql.resolvers.user_resolver import get_users, get_user, login_user, get_user_by_token
from app.graphql.types.user import  User, GetUserInput, LoginUserInput,UserToken, UserByTokenInput

@strawberry.type
class UserQueries:
    users: List[User] = strawberry.field(resolver=get_users)

    @strawberry.field
    def user(self,user:GetUserInput) -> User:
        return get_user(user)
    
    @strawberry.field
    def login_user(self,user:LoginUserInput) -> UserToken:
        return login_user(user)
    
    @strawberry.field
    def get_user_by_token(self,tokenInput: UserByTokenInput) -> Optional[User]:
        return get_user_by_token(tokenInput)