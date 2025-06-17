from fastapi import FastAPI
from app.api import health_router
from app.core.middleware import add_cors_middleware

app = FastAPI()

add_cors_middleware(app)

app.include_router(health_router.router)

@app.get("/")
async def health_check():
        return {"status": "it is live"}