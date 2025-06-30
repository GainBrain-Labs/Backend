from app.schemas.user import ValidateUser

def to_dict(user:ValidateUser):
    return {
        "email": user.email
    }