"""API v1 Router"""
from fastapi import APIRouter

from app.api.v1.endpoints import users, auth

router = APIRouter()

# Include endpoint routers
router.include_router(auth.router, prefix="/auth", tags=["auth"])
router.include_router(users.router, prefix="/users", tags=["users"])
