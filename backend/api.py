from fastapi import APIRouter

from app.auth.views import auth_router

api_router = APIRouter()

# include all routers
api_router.include_router(auth_router, prefix="/auth", tags=["auth"])
