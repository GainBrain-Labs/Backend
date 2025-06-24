import strawberry
import datetime
from typing import Optional

@strawberry.type
class User:
    id: int
    first_name: str
    last_name: str
    username: str
    email: str
    profile_pic: str
    phone_no: str
    dob: datetime.datetime
    isActive: bool

@strawberry.type
class UserToken:
    token: str

@strawberry.input
class UserByTokenInput:
    token: str

@strawberry.input
class CreateUserInput:
    username: str
    email: str
    password: str
    first_name: str
    last_name: Optional[str] =  None
    profile_pic: Optional[str] =  None
    phone_number: Optional[str] =  None
    dob: Optional[datetime.date] = None


@strawberry.input
class GetUserInput:
    email: str

@strawberry.input
class LoginUserInput:
    email: str
    password: str

