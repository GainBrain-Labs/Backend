from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from app.models.user import User
from app.schemas.user import UserCreate

async def get_user_by_email(email: str, db: AsyncSession):
    result = await db.execute(select(User).where(User.email == email))
    return result.scalars().first()

async def get_user_by_username(username: str, db: AsyncSession):
    result = await db.execute(select(User).where(User.username == username))
    return result.scalars().first()

async def create_user(user_data: UserCreate, hashed_password: str, db: AsyncSession):
    new_user = User(
        username=user_data.username,
        first_name=user_data.first_name,
        last_name=user_data.last_name,
        password=hashed_password,
        email=user_data.email,
        profile_pic=user_data.profile_pic,
        phone_number=user_data.phone_number,
        dob=user_data.dob,
    )
    db.add(new_user)
    await db.commit()
    await db.refresh(new_user)
    return new_user
