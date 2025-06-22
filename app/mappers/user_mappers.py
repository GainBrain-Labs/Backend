from app.graphql.types.user import GetUserInput, LoginUserInput, CreateUserInput
from app.schemas.user import UserCreate, GetUser, ValidateUser

def create_user_input(user:CreateUserInput) -> UserCreate :
    print(user)
    return UserCreate(
        username=user.username,
        first_name=user.first_name,
        last_name=user.last_name,
        email=user.email,
        password=user.password,
        profile_pic=user.profile_pic,
        phone_number=user.phone_number,
        dob=user.dob
    )

def get_user_input(user: GetUserInput) -> GetUser:
    return GetUser(
        email=user.email
    )

def validate_user_input(user: LoginUserInput) -> ValidateUser:
    return ValidateUser(
        email=user.email,
        password=user.password
    )