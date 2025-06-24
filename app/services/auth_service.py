from datetime import datetime, timedelta
from jose import JWTError, jwt
from app.schemas.user import ValidateUser
from app.utils.jwt_helper import to_dict

class AuthService() :
    def __init__(self):
        self.SECRET_KEY = "your-secret"
        self.ALGORITHM = "HS256"
        self.ACCESS_TOKEN_EXPIRE_MINUTES = 30

    def create_access_token(self,user:ValidateUser):
        to_encode = to_dict(user)
        expire = datetime.utcnow() + timedelta(minutes=self.ACCESS_TOKEN_EXPIRE_MINUTES)
        to_encode.update({"exp": expire})
        return jwt.encode(to_encode, self.SECRET_KEY, algorithm=self.ALGORITHM)

    def verify_access_token(self,token: str):
        try:
            return jwt.decode(token, self.SECRET_KEY, algorithms=[self.ALGORITHM])
        except JWTError:
            return None
    