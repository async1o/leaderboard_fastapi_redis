
from fastapi import APIRouter


from src.schemas.users import UserAddSchema
from src.services.users import UserServices
from src.repositories.users import UserRepositories, UsersLeaderBoardRepository
from src.services.user_leaderboard import UsersLeaderBoardService

router = APIRouter(
    prefix='/users',
    tags=['users']
)

@router.get('')
async def get_all_users():
    res = await UserServices(UserRepositories).get_all_users()
    return res

@router.post('')
async def add_user(data: UserAddSchema):
    user_id = await UserServices(UserRepositories).add_user(data)
    return user_id

@router.put('')
async def update_user(user_id: int, data: UserAddSchema):
    model = await UserServices(UserRepositories).update_user(user_id, data)
    return model

@router.delete('')
async def delete_user(user_id: int):
    res = await UserServices(UserRepositories).delete_user(user_id)
    return res

@router.put('/points')
async def update_points(user_id: int, points: int):
    res = await UsersLeaderBoardService(UsersLeaderBoardRepository).update_points(user_id, points)
    return res