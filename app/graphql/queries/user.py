import strawberry
from typing import List, Optional
from app.graphql.resolvers.user_resolver import get_users, get_user, login_user
from app.graphql.types.user import  User, GetUserInput, LoginUserInput

@strawberry.type
class UserQueries:
    users: List[User] = strawberry.field(resolver=get_users)

    @strawberry.field
    def user(self,user:GetUserInput) -> User:
        return get_user(user)
    
    @strawberry.field
    def loginUser(self,user:LoginUserInput) -> Optional[User]:
        return login_user(user)