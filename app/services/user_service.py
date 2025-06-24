from fastapi import HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from app.core.security import hash_password, verify_password
from app.schemas.user import UserCreate, GetUser, ValidateUser, UserToken
from app.repositories.base_repository import BaseRepository
from app.exceptions.repository_errors import NotFoundError
from app.config.logger import logger
from app.mapperServiceToDB import user_mapper
from app.services.auth_service import AuthService

class UserService() :
    def __init__(self, user_repository:BaseRepository):
        self.user_repository = user_repository

    async def create_user(self,user_data: UserCreate):
        print("in user service")
        print(user_data)
        try:
            await self.user_repository.get_by_email(user_data.email)
        except NotFoundError as e:
            logger.info("email not found")
        except Exception:
            raise
        try:
            await self.user_repository.get_by_username(user_data.username)
        except NotFoundError as e:
            logger.info("username not found")
        except Exception:
            raise

        hashed = hash_password(user_data.password)
        user_data.password = hashed
        create_user_input = user_mapper.user_service_to_db(user_data)
        return await self.user_repository.create(create_user_input)

    async def validate_user(self,user_data : ValidateUser,auth_service: AuthService):
        user = await self.user_repository.get_by_email(user_data.email)
        if not user or not verify_password(user_data.password, user.password):
            raise HTTPException(status_code=401, detail="Invalid credentials")
        return auth_service.create_access_token(user_data)

    async def get_all_user(self):
        return await self.user_repository.get_all()

    async def get_user(self,user: GetUser):
        return await self.user_repository.get_by_email(user.email)
    
    async def get_user_from_token(self,token:UserToken,auth_service: AuthService):
        email = auth_service.verify_access_token(token.token)["email"]
        return await  self.user_repository.get_by_email(email)

