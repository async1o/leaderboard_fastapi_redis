from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker
from sqlalchemy.orm import DeclarativeBase
from redis import Redis

from src.config_db import settings

engine = create_async_engine(
    url=settings.get_url_db,
)
async_session_maker = async_sessionmaker(engine, expire_on_commit=False)


class Base(DeclarativeBase):
    pass

def get_redis() -> Redis:
    redis = Redis(host='localhost', port=6379, db=0)
    return redis

async def reset_tables():
    redis = get_redis()
    await redis.flushall()
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)
        await conn.run_sync(Base.metadata.create_all)
