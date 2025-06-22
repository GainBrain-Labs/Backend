import strawberry
import datetime

@strawberry.type
class User:
    id: int
    first_name: str
    last_name: str
    user_name: str
    email: str
    profile_pic: str
    phone_no: str
    dob: datetime.datetime
    isActive: bool

@strawberry.input
class CreateUserInput:
    username: str
    email: str
    password: str
    first_name: str
    last_name: str | None
    profile_pic: str | None
    phone_number: str | None
    dob: datetime.date | None


@strawberry.input
class GetUserInput:
    email: str

@strawberry.input
class LoginUserInput:
    email: str
    password: str

