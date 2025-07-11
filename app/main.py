from fastapi import FastAPI
from app.api import health_router
from app.api import graphql_router
from app.core.middleware import add_cors_middleware

app = FastAPI()
add_cors_middleware(app)

app.include_router(health_router.router,prefix="/health", tags=["Health Check"])
app.include_router(graphql_router.router, prefix="/graphql", tags=["graphql"])

@app.get("/")
async def health_check():
        return {"status": "it is live"}