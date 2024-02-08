
from sqlalchemy import select, update
from sqlalchemy.orm import Session
from sqlalchemy.exc import SQLAlchemyError 
from src.models.Keyword_TM import Keyword_TM
from icecream import ic


class CKeyword:
    def __init__(self, asyncdb: Session):
        self.db = asyncdb

    async def select_bycode(self, code: str) -> Keyword_TM|None:
        try:
            stmt = select(Keyword_TM).filter(Keyword_TM.Code == code)
            result = await self.db.execute(stmt)

            return result.scalars().one_or_none()
        except SQLAlchemyError as e:
            ic(f"ERR select_bycode: {str(e)}")
            return None
        
    async def update(self, code: str, src: Keyword_TM) -> bool:
        try:
            src_dict = src.to_dict().pop("udate")
            # stmt = update(Keyword_TM).where(Keyword_TM.Code == code).values(src_dict)
            # await self.db.execute(stmt)
            
            stmt = update(Keyword_TM).where(Keyword_TM.Code == code).values(Contents=src.Contents,
                                                                           keycode=src.keycode,
                                                                           keycontents=src.keycontents,
                                                                           kw_feeling=src.kw_feeling,
                                                                           kw_things=src.kw_things,
                                                                           kw_theme=src.kw_theme,
                                                                           kw_etc=src.kw_etc)
                
            await self.db.execute(stmt)
            
            return True
        except SQLAlchemyError as e:
            ic(f"ERR update: {str(e)}")
            return False
        
        