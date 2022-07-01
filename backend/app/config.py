
from contextlib import asynccontextmanager
from asyncio import current_task
from typing import AsyncGenerator

from sqlalchemy.ext.asyncio import (
    AsyncSession,
    create_async_engine,
    async_scoped_session,
)
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlmodel import SQLModel

from .utils import db_set_up

db_config = db_set_up()

Base = declarative_base()
SQLModel.metadata = Base.metadata

engine_uri = 'mysql+aiomysql://%s:%s@%s/%s?charset=utf8' % (
    db_config["DB_USER_NAME"],
    db_config["DB_USER_PASSWD"],
    db_config["DB_HOST"],
    db_config["DB_NAME"],
)

engine = create_async_engine(
    engine_uri,
    pool_recycle=3600,
)

async_session_factory = sessionmaker(bind=engine, class_=AsyncSession)

session = async_scoped_session(
    session_factory=async_session_factory,
    scopefunc=current_task,
)

async_session = sessionmaker(
    bind=engine,
    class_=AsyncSession,
    expire_on_commit=False,
    autocommit=False,
    autoflush=False,
)


@asynccontextmanager
async def get_session() -> AsyncGenerator[AsyncSession, None]:
    async with async_session() as session:
        async with session.begin():
            try:
                yield session
            finally:
                await session.close()


# async def _async_main():
#     async with engine.begin() as conn:
#         await conn.run_sync(Base.metadata.drop_all)
#         await conn.run_sync(Base.metadata.create_all)
#     await engine.dispose()
