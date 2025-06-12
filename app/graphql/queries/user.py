import strawberry
from typing import List, Optional
from app.graphql.resolvers.user_resolver import get_users, get_user, login_user
from app.graphql.types.user import  User, getUserInput, loginUserInput

@strawberry.type
class Query:
    users: List[User] = strawberry.field(resolver=get_users)

    @strawberry.field
    def user(self,user:getUserInput) -> User:
        return get_user(user)
    
    @strawberry.field
    def loginUser(self,user:loginUserInput) -> Optional[User]:
        return login_user(user)