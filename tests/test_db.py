import asyncio
from sqlalchemy import text
from app.db.session import session_manager

async def test_db():
    try:
        async with session_manager.session() as session:
            result = await session.execute(text("SELECT 1"))
            print("✅ Database connected!")
            print(f"Result: {result.fetchone()[0]}")
    except Exception as e:
        print(f"❌ Connection failed: {e}")
    finally:
        await session_manager.close()

if __name__ == "__main__":
    asyncio.run(test_db())


# python -m tests.test_db (run this from backend folder)