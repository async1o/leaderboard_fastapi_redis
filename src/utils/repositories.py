from typing import List

from abc import ABC, abstractmethod
from sqlalchemy import select, insert, delete, update, desc

from src.db.db import async_session_maker
from src.schemas.users import UserSchema


class AbstractRepositories(ABC):
    @abstractmethod
    async def find_all(self):
        raise NotImplementedError

    @abstractmethod
    async def add_one(self, data: dict):
        raise NotImplementedError

    @abstractmethod
    async def update_one(self, entity_id: int, data: dict):
        raise NotImplementedError

    @abstractmethod
    async def delete_one(self, entity_id: int):
        raise NotImplementedError


class SQLAlchemyRepositories(AbstractRepositories):
    model = None

    async def find_all(self) -> List[UserSchema]:
        async with async_session_maker() as session:
            stmt = select(self.model)  # type: ignore
            models = await session.execute(stmt)
            models = [row[0].to_read_model() for row in models.all()]
            return models

    async def add_one(self, data: dict):
        async with async_session_maker() as session:
            stmt = insert(self.model).values(**data).returning(self.model.id)  # type: ignore
            entity_id = await session.execute(stmt)
            entity_id = entity_id.scalar_one()
            await session.commit()
            return entity_id

    async def update_one(self, entity_id: int, data: dict):
        async with async_session_maker() as session:
            stmt = update(self.model).where(self.model.id == entity_id).values(**data).returning(
                self.model)  # type: ignore
            model = await session.execute(stmt)
            model = model.scalar_one().to_read_model()
            await session.commit()
            return model

    async def delete_one(self, entity_id: int):
        async with async_session_maker() as session:
            stmt = delete(self.model).where(self.model.id == entity_id)  # type: ignore
            await session.execute(stmt)
            await session.commit()



class LeaderBoardRepositories:
    model = None

    async def update_points(self, entity_id: int, points: int):
        async with async_session_maker() as session:
            stmt = update(self.model).where(self.model.id == entity_id).values({'points': self.model.points + points})
            await session.execute(stmt)
            await session.commit()

    async def get_leaderboard(self):
        async with async_session_maker() as session:
            stmt = select(self.model).order_by(desc(self.model.points))
            result = await session.execute(stmt)
            return [row[0].to_read_model() for row in result.all()]