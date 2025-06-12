from app.graphql.types.user import User, createUserInput, getUserInput, loginUserInput
from typing  import List, Optional

def get_users() -> List[User]:
        #db call for get all users
    return [
        User(
            id = 1,
            first_name="Nityanand",
            last_name="Kumar",
            user_name="nitya_dev",
            email="nitya@example.com",
            profile_pic="https://example.com/images/nitya.jpg",
            phone_no="9876543210",
            dob="1999-01-15"
        ),
        User(
            id = 2,
            first_name="Ananya",
            last_name="Singh",
            user_name="ananya123",
            email="ananya@example.com",
            profile_pic="https://example.com/images/ananya.jpg",
            phone_no="9123456780",
            dob="2000-05-30"
        ),
        User(
            id = 3,
            first_name="Ravi",
            last_name="Verma",
            user_name="ravi_v",
            email="ravi@example.com",
            profile_pic="https://example.com/images/ravi.jpg",
            phone_no="9988776655",
            dob="1998-11-22"
        ),
    ]

def get_user(user:getUserInput) -> Optional[User]:
    #db call for one user using id
    return User(
        id = 1,
        first_name="Nityanand",
        last_name="Kumar",
        user_name="nitya_dev",
        email="nitya@example.com",
        profile_pic="https://example.com/images/nitya.jpg",
        phone_no="9876543210",
        dob="1999-01-15"
    )

def create_user(user:createUserInput) -> Optional[User]:
    #db call to add user to database
    return User(
        id = 4,
        first_name="nitya",
        last_name="noi hai",
        user_name=user.username,
        email=user.email,
        profile_pic="https://example.com/images/nitya.jpg",
        phone_no="7004813144",
        dob="15-03-2004"
    )

def login_user(user: loginUserInput) -> Optional[User]:
    #db call to check ans return if user exists with given parameters
    return User(
        id = 4,
        first_name="nitya",
        last_name="noi hai",
        user_name=user.username,
        email=user.email,
        profile_pic="https://example.com/images/nitya.jpg",
        phone_no="7004813144",
        dob="15-03-2004"
    )