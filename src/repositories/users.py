from src.utils.repositories import SQLAlchemyRepositories, LeaderBoardRepositories
from src.models.users import UsersModel

class UserRepositories(SQLAlchemyRepositories):
    model = UsersModel


class UsersLeaderBoardRepository(LeaderBoardRepositories):
    model = UsersModel