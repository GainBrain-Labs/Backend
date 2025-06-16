from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from app.services.auth_service import verify_access_token
from app.repositories.user_repository import get_user_by_username
from app.db.session import get_db  
from sqlalchemy.ext.asyncio import AsyncSession

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/login")

async def get_current_user(token: str = Depends(oauth2_scheme), db: AsyncSession = Depends(get_db)):
    payload = verify_access_token(token)
    username = payload.get("sub") if payload else None
    if username is None:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid token")

    user = await get_user_by_username(username, db)
    if user is None:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="User not found")
    return user
