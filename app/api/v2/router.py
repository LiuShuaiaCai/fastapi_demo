"""API v2 Router"""
from fastapi import APIRouter

from app.api.v2.endpoints import users

router = APIRouter()

# Include endpoint routers
router.include_router(users.router, prefix="/users", tags=["users"])
