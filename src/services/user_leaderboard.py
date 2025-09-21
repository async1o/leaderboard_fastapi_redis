from typing import Dict, List

from src.schemas.users import UserSchema
from src.utils.repositories import LeaderBoardRepositories


class UsersLeaderBoardService:
    def __init__(self, leaderboard_repo: type(LeaderBoardRepositories)): # type: ignore
        self.leaderboard_repo: type(LeaderBoardRepositories) = leaderboard_repo() # type: ignore



    async def update_points(self, user_id: int, points: int) -> Dict:
        await self.leaderboard_repo.update_points(user_id, points)
        return {'message': 'Points added'}

    async def get_leaderboard(self) -> List[UserSchema]:
        return await self.leaderboard_repo.get_leaderboard()