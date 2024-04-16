

from fastapi import Depends
from sqlalchemy import Integer, Column
from sqlalchemy.orm import DeclarativeBase, Mapped
from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker, create_async_engine
from typing import Optional, AsyncGenerator
from datetime import datetime


DATABASE_URL = "sqlite+aiosqlite:///./test1.db"


class Base(DeclarativeBase):
    pass

class keyword_logs(Base):
    __tablename__ = 'keyword_logs'
    
    id: Mapped[Optional[int]] = Column(Integer, primary_key=True)
    cdate: Mapped[datetime]
    udate: Mapped[datetime]
    
    src_code: Mapped[str]
    src_contents: Mapped[str]
    src_keycode: Mapped[str]
    src_keycontents: Mapped[str]
    src_kw_feeling: Mapped[str]
    src_kw_things: Mapped[str]
    src_kw_theme: Mapped[str]
    src_kw_etc: Mapped[str]
    src_udate: Mapped[str]
    
    dest_code: Mapped[str]
    dest_contents: Mapped[str]
    dest_keycode: Mapped[str]
    dest_keycontents: Mapped[str]
    dest_kw_feeling: Mapped[str]
    dest_kw_things: Mapped[str]
    dest_kw_theme: Mapped[str]
    dest_kw_etc: Mapped[str]
    dest_udate: Mapped[str]
    
    
engine = create_async_engine(DATABASE_URL)
async_session_maker = async_sessionmaker(engine, expire_on_commit=False)


async def create_db_and_tables():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)


async def get_async_session() -> AsyncGenerator[AsyncSession, None]:
    async with async_session_maker() as session:
        yield session


async def get_lite_db(session: AsyncSession = Depends(get_async_session)):
    yield session
