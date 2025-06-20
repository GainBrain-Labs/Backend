from fastapi import HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession
from app.repositories.user_repository import UserRepository
from app.core.security import hash_password, verify_password
from app.schemas.user import UserCreate, GetUser, ValidateUser

async def create_user(user_data: UserCreate, db: AsyncSession):
    print("in user service")
    print(user_data)
    user_repository = UserRepository(db)
    if await user_repository.get_by_email(user_data.email):
        raise HTTPException(status_code=400, detail="Email already exists")
    if await user_repository.get_user_by_username(user_data.username):
        raise HTTPException(status_code=400, detail="Username already taken")

    hashed = hash_password(user_data.password)
    return await user_repository.create(user_data, hashed)

async def validate_user(user : ValidateUser, db: AsyncSession):
    print(user)
    user_repository = UserRepository(db)
    user = await user_repository.get_by_email(user.email)
    if not user or not verify_password(user.password, user.password):
        raise HTTPException(status_code=401, detail="Invalid credentials")
    return user

async def get_all_user(db:AsyncSession):
    user_repository = UserRepository(db)
    return await user_repository.get_all()

async def get_user(user: GetUser, db: AsyncSession):
    print(user)
    user_repository = UserRepository(db)
    return await user_repository.get_by_email(user.email)

