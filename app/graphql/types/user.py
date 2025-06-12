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

@strawberry.input
class createUserInput:
    username: str
    email: str
    password: str

@strawberry.input
class getUserInput:
    id: int

@strawberry.input
class loginUserInput:
    email: str
    password: str