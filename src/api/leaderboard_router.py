from fastapi import APIRouter

from src.services.user_leaderboard import UsersLeaderBoardService
from src.repositories.users import UsersLeaderBoardRepository

router = APIRouter(
    prefix="/leaderboard",
    tags=["leaderboard"]
)

@router.get('')
async def get_users_leaderboard():
    return await UsersLeaderBoardService(UsersLeaderBoardRepository).get_leaderboard()