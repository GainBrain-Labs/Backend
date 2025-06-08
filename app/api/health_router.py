from fastapi import APIRouter

router = APIRouter(
    prefix="/health"
)

@router.get("/")
async def health_check():
    """
    Health check endpoint to verify the service is running.
    """
    return {"status": "healthy"}