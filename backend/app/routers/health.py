from fastapi import APIRouter

router = APIRouter()

@router.get("/health")
async def health_check():
    """
    Health check endpoint.
    Returns a simple JSON payload to confirm the service is running.
    """
    return {"status": "ok"}


