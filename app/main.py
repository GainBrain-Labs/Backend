from fastapi import FastAPI
from api import health_router


app = FastAPI()

app.include_router(health_router.router)

@app.get("/")
async def health_check():
        return {"status": "it is live"}