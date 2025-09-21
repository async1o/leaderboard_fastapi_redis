from typing import Dict

from src.utils.repositories import AbstractRepositories, LeaderBoardRepositories
from src.schemas.users import UserAddSchema, UserSchema


class UserServices():
    def __init__(self, users_repo: type(AbstractRepositories)):  # type: ignore
        self.users_repo: type(AbstractRepositories) = users_repo() # type: ignore


    async def get_all_users(self) -> UserSchema:
        res = await self.users_repo.find_all()
        return res

    async def add_user(self, data: UserAddSchema) -> UserSchema:
        data_dict = data.model_dump()
        res = await self.users_repo.add_one(data_dict)
        return res

    async def update_user(self, user_id: int, data: UserAddSchema) -> UserSchema:
        data_dict = data.model_dump()
        res = await self.users_repo.update_one(user_id, data_dict)
        return res

    async def delete_user(self, user_id: int) -> Dict:
        await self.users_repo.delete_one(user_id)
        return {'message': 'User deleted'}


