import asyncio
from sqlalchemy import text
from app.db.session import session_manager
from app.core.dependencies import get_user_context, get_db
from sqlalchemy.inspection import inspect

def model_to_dict(obj):
    return {c.key: getattr(obj, c.key) for c in inspect(obj).mapper.column_attrs}

async def test_db():
    try:
        # async with session_manager.session() as session:
        #     result = await session.execute(text("SELECT 1"))
        #     print("✅ Database connected!")
        #     print(f"Result: {result.fetchone()[0]}")
            
        # async for session in get_db():
        #     result = await session.execute(text("SELECT 1"))
        #     print("✅ Database connected!")
        #     print(f"Result: {result.fetchone()[0]}")
        
        async with get_user_context() as user_repo:
            users = await user_repo.get_all()
            for user in users:
                print(model_to_dict(user))

    except Exception as e:
        print(f"❌ Connection failed: {e}")

if __name__ == "__main__":
    asyncio.run(test_db())


# python -m tests.test_db (run this from backend folder)
