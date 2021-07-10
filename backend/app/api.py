from fastapi import APIRouter

from .auth.views import auth_router, user_router

api_router = APIRouter()

# include all routers
api_router.include_router(auth_router, prefix="/auth", tags=["auth"])
api_router.include_router(user_router, prefix="/users", tags=["users"])

