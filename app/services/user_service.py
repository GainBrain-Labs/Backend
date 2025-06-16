from fastapi import HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession
from app.repositories import user_repository
from app.core.security import hash_password, verify_password
from app.schemas.user import UserCreate

async def create_user(user_data: UserCreate, db: AsyncSession):
    if await user_repository.get_user_by_email(user_data.email, db):
        raise HTTPException(status_code=400, detail="Email already exists")
    if await user_repository.get_user_by_username(user_data.username, db):
        raise HTTPException(status_code=400, detail="Username already taken")

    hashed = hash_password(user_data.password)
    return await user_repository.create_user(user_data, hashed, db)

async def validate_user(email: str, password: str, db: AsyncSession):
    user = await user_repository.get_user_by_email(email, db)
    if not user or not verify_password(password, user.password):
        raise HTTPException(status_code=401, detail="Invalid credentials")
    return user
