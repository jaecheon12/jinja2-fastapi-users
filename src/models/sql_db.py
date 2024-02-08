from fastapi import Depends

from sqlalchemy.engine import URL

from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker, create_async_engine

from typing import AsyncGenerator, List, Optional 
from dotenv import dotenv_values

config = dotenv_values(".env") 

connection_url = URL.create(
    config["MSSQL_LIB"],
    username=config["MSSQL_USER"],
    password=config["MSSQL_PASS"],
    host=config["MSSQL_HOST"],
    port=config["MSSQL_PORT"],
    database=config["MSSQL_DB"],
    query={
        "driver": config["MSSQL_DIRVER"],
    },
)       

engine = create_async_engine(connection_url)
async_session_maker = async_sessionmaker(engine, expire_on_commit=False)

async def get_async_session() -> AsyncGenerator[AsyncSession, None]:
    async with async_session_maker() as session:
        yield session



async def get_db() -> AsyncGenerator[AsyncSession, None]:
    async with async_session_maker() as session:
        yield session
        

# async def get_db(session: AsyncSession = Depends(get_async_session)):
#     yield SQLAlchemyUserDatabase(session, User, OAuth)
