import logging
import sys
import os
from contextlib import asynccontextmanager
sys.path.insert(1, os.path.join(sys.path[0], '..'))

from fastapi import FastAPI
import uvicorn

from src.db.db import reset_tables
from src.api.main_router import router

@asynccontextmanager
async def lifespan(app: FastAPI):
    logging.basicConfig(level=logging.INFO)
    await reset_tables()
    logging.info(f'Tables reset')
    yield


app = FastAPI(lifespan=lifespan)


app.include_router(router)


if __name__ == '__main__':
    uvicorn.run('main:app', host='0.0.0.0', port=8000, reload=True)


