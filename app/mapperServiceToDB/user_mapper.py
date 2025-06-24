from app.schemas.user import UserCreate
from app.models.user import User

def user_service_to_db(user:UserCreate) -> User:
    return User(
        username=user.username,
        first_name=user.first_name,
        last_name=user.last_name,
        email=user.email,
        password=user.password,
        profile_pic=user.profile_pic,
        phone_number=user.phone_number,
        dob=user.dob
    )
