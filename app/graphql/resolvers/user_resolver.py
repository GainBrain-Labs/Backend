from app.graphql.types.user import User, CreateUserInput, LoginUserInput, GetUserInput, UserByTokenInput, UserToken
from typing  import List, Optional
from app.mappers import user_mappers
from app.core.dependencies import get_user_context

async def get_users() -> List[User]:
    ctx = await get_user_context()
    user_service = ctx["user_service"]
    return await user_service.get_all_user()

async def get_user(user:GetUserInput) -> Optional[User]:
    ctx = await get_user_context()
    user_service = ctx["user_service"]
    get_user_input = user_mappers.get_user_input(user)
    return await user_service.get_user(get_user_input)

async def create_user(user:CreateUserInput) -> Optional[User]:
    ctx = await get_user_context()
    user_service = ctx["user_service"]
    user_input = user_mappers.create_user_input(user)
    return await user_service.create_user(user_input)

async def login_user(user: LoginUserInput) -> Optional[UserToken]:
    ctx = await get_user_context()
    user_service = ctx["user_service"]
    auth_service = ctx["auth_service"]
    login_user_input = user_mappers.validate_user_input(user)
    token = await user_service.validate_user(login_user_input,auth_service)
    return user_mappers.to_user_token(token)

async def get_user_by_token(token: UserByTokenInput) -> Optional[User]:
    ctx = await get_user_context()
    user_service = ctx["user_service"]
    auth_service = ctx["auth_service"]
    get_user_by_token_input = user_mappers.to_user_token_input(token)
    return await user_service.get_user_from_token(get_user_by_token_input,auth_service)


