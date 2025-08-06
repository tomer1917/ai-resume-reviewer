from fastapi import FastAPI
from .routers.health import router as health_router
from .routers.review import router as review_router

app = FastAPI(title="AI Resume Reviewer")

app.include_router(health_router)
app.include_router(review_router)
