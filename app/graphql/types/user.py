import strawberry

@strawberry.type
class User:
    id: int
    first_name: str
    last_name: str
    user_name: str
    email: str
    profile_pic: str
    phone_no: str
    dob: str
    isActive: bool

@strawberry.input
class CreateUserInput:
    username: str
    email: str
    password: str

@strawberry.input
class GetUserInput:
    email: str

@strawberry.input
class LoginUserInput:
    email: str
    password: str