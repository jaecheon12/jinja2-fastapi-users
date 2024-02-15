
from sqlalchemy.future import select
from sqlalchemy.orm import Session
from src.models.Maker_TM import Maker_TM as Maker
from icecream import ic
import logging

class CtrlMaker:
    def __init__(self, db: Session):
        self.db = db
        
    async def select(self, code: str) -> Maker|None:
        try:
            stmt = select(Maker).filter(Maker.Code == code)
            result = await self.db.execute(stmt)

            return result.scalars().one_or_none()
        except BaseException as e:
            ic(f"ERR CtrlMaker select: {str(e)}")
            return None
        
    async def select_all(self, code: str) -> list[Maker]|None:
        try:
            stmt = select(Maker).filter(Maker.Code == code, Maker.State == 1)
            result = await self.db.execute(stmt)
            
            return result.scalars().all()
        except BaseException as e:
            ic(f"ERR CtrlMaker select_all: {str(e)}")
            return None
