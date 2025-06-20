from app.graphql.types.user import User, CreateUserInput, LoginUserInput, GetUserInput
from typing  import List, Optional
from app.mappers import user_mappers
from app.services import user_service
from app.core import dependencies

async def get_users() -> List[User]:
    return await user_service.get_all_user(dependencies.get_db())
    return [
        User(
            id = 1,
            first_name="Nityanand",
            last_name="Kumar",
            user_name="nitya_dev",
            email="nitya@example.com",
            profile_pic="https://example.com/images/nitya.jpg",
            phone_no="9876543210",
            dob="1999-01-15",
            isActive=True
        ),
        User(
            id = 2,
            first_name="Ananya",
            last_name="Singh",
            user_name="ananya123",
            email="ananya@example.com",
            profile_pic="https://example.com/images/ananya.jpg",
            phone_no="9123456780",
            dob="2000-05-30",
            isActive=True
        ),
        User(
            id = 3,
            first_name="Ravi",
            last_name="Verma",
            user_name="ravi_v",
            email="ravi@example.com",
            profile_pic="https://example.com/images/ravi.jpg",
            phone_no="9988776655",
            dob="1998-11-22",
            isActive=True
        ),
    ]

async def get_user(user:GetUserInput) -> Optional[User]:
    get_user_input = user_mappers.get_user_input(user)
    return await user_service.get_user(get_user_input,dependencies.get_db())
    return User(
        id = 1,
        first_name="Nityanand",
        last_name="Kumar",
        user_name="nitya_dev",
        email="nitya@example.com",
        profile_pic="https://example.com/images/nitya.jpg",
        phone_no="9876543210",
        dob="1999-01-15",
        isActive=True
    )

async def create_user(user:CreateUserInput) -> Optional[User]:
    user_input = user_mappers.create_user_input(user)
    return await user_service.create_user(user_input,dependencies.get_db())
    return User(
        id = 4,
        first_name="nitya",
        last_name="noi hai",
        user_name=user.username,
        email=user.email,
        profile_pic="https://example.com/images/nitya.jpg",
        phone_no="7004813144",
        dob="15-03-2004",
        isActive=True
    )

async def login_user(user: LoginUserInput) -> Optional[User]:
    login_user_input = user_mappers.validate_user_input(user)
    return await user_service.validate_user(login_user_input,dependencies.get_db())
    #service call to check ans return if user exists with given parameters
    return User(
        id = 4,
        first_name="nitya",
        last_name="noi hai",
        user_name="dsfdsf",
        email=user.email,
        profile_pic="https://example.com/images/nitya.jpg",
        phone_no="7004813144",
        dob="15-03-2004",
        isActive=True
    )