from typing import AsyncGenerator, Dict
from app.db.session import session_manager
from sqlalchemy.ext.asyncio import AsyncSession
from app.repositories.user_repository import UserRepository
from app.repositories.timescale_repository import TimescaleRepository
from app.services.user_service import UserService
from app.services.auth_service import AuthService
from app.services.data_service import DataService
from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from sqlalchemy.ext.asyncio import AsyncSession
from app.schemas.user import GetUser

async def get_db() -> AsyncGenerator[AsyncSession, None]:
    async with session_manager.session() as session:
        yield session

async def get_user_context() -> dict[str, UserService]:
    async with session_manager.session() as session:
        user_repo = UserRepository(session)
        timescale_repo = TimescaleRepository(session)
        
        user_service = UserService(user_repo)
        auth_service = AuthService()
        data_service = DataService(timescale_repo)
        return {
            "user_service": user_service,
            "auth_service": auth_service,
            "data_service": data_service
        }

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/login")

async def get_current_user(token: str = Depends(oauth2_scheme), db: AsyncSession = Depends(get_db)):
    ctx = await get_user_context()
    auth_service = ctx["auth_service"]
    user_service = ctx["user_service"]
    payload = auth_service.verify_access_token(token)
    email = payload.get("sub") if payload else None
    if email is None:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid token")

    user = await user_service.get_user(GetUser(email=email))
    if user is None:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="User not found")
    return user
