from fastapi import APIRouter

from src.api.routers.users import router as users_router
from src.api.leaderboard_router import router as ladderboard_router

router = APIRouter()

router.include_router(users_router)
router.include_router(ladderboard_router)
