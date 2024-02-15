
from sqlalchemy import select
from sqlalchemy.orm import Session
from sqlalchemy.exc import SQLAlchemyError 
from src.models.Model_tm import ModelTM
from icecream import ic


class CtrlModel:
    def __init__(self, asyncdb: Session):
        self.db = asyncdb

    async def get_bycode(self, code: str) -> ModelTM|None:
        try:
            stmt = select(ModelTM).filter(ModelTM.Code == code)
            result = await self.db.execute(stmt)

            return result.scalars().one_or_none()
        except SQLAlchemyError as e:
            ic(f"ERR select_bycode: {str(e)}")
            return None
        
    async def gall_bycode(self, code: str) -> ModelTM|None:
        try:
            stmt = select(ModelTM).filter(ModelTM.Code == code)
            result = await self.db.execute(stmt)
            
            return result.scalars().all()
        except SQLAlchemyError as e:
            ic(f"ERR select_bycode: {str(e)}")
            return None