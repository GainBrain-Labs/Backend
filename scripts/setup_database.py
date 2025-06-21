from app.config.database import engine
from app.db.base import Base
import asyncio
from sqlalchemy import inspect
from app.models.user import User
from app.models.base import BasicModel

async def create_tables():
    print("[INFO] Starting table creation...")

    try:
        async with engine.begin() as conn:
            print("[INFO] Connected to the database.")
            print("[DEBUG] Current tables in metadata:", Base.metadata.tables.keys())
            await conn.run_sync(Base.metadata.create_all)
            print("[SUCCESS] Tables created via metadata.\n")

            def inspect_db(connection):
                inspector = inspect(connection)
                tables = inspector.get_table_names()
                print("[INFO] Tables present in database:")
                for table_name in tables:
                    print(f"  📄 {table_name}")
                    columns = inspector.get_columns(table_name)
                    for col in columns:
                        print(f"     - {col['name']} ({col['type']})")

            await conn.run_sync(inspect_db)

        await engine.dispose()
        print("\n[INFO] Engine disposed. Setup complete.")

    except Exception as e:
        print(f"[ERROR] Failed to create or inspect tables: {e}")

if __name__ == "__main__":
    asyncio.run(create_tables())
