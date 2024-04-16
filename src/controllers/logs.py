from src.models.lite_db import keyword_logs
from datetime import datetime
from src.static.const import CONST_TIMEZONE_KST
from sqlalchemy import select, insert
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.ext.asyncio import AsyncSession
from icecream import ic

class Clogs:
    def __init__(self, db: AsyncSession):
        self.db = db
    
    async def insert(self, src: dict, dest: dict) -> bool:
        try:
            await self.db.execute(insert(keyword_logs)
                                  .values(  cdate=datetime.now().astimezone(CONST_TIMEZONE_KST),
                                            udate=datetime.now().astimezone(CONST_TIMEZONE_KST),

                                            src_code=src["Code"],
                                            src_contents=src["Contents"],
                                            src_keycode=src.get("keycode", ""),  # .get을 사용하여 키가 없는 경우를 처리
                                            src_keycontents=src.get("keycontents", ""),
                                            src_kw_feeling=src.get("kw_feeling", ""),
                                            src_kw_things=src.get("kw_things", ""),
                                            src_kw_theme=src.get("kw_theme", ""),
                                            src_kw_etc=src.get("kw_etc", ""),
                                            src_udate=src.get("udate", datetime.now().astimezone(CONST_TIMEZONE_KST)),
                                            
                                            dest_code=dest["Code"],
                                            dest_contents=dest["Contents"],
                                            dest_keycode=dest.get("keycode", ""),
                                            dest_keycontents=dest.get("keycontents", ""),
                                            dest_kw_feeling=dest.get("kw_feeling", ""),
                                            dest_kw_things=dest.get("kw_things", ""),
                                            dest_kw_theme=dest.get("kw_theme", ""),
                                            dest_kw_etc=dest.get("kw_etc", ""),
                                            dest_udate=dest.get("udate", datetime.now().astimezone(CONST_TIMEZONE_KST)),))
            return True
        except SQLAlchemyError as e:  # SQLAlchemy 관련 예외 처리
            ic(f"ERR Clogs insert: {str(e)}")
            return False
    
    async def select(self, date: datetime, inf: int = 0) -> list[dict]|None:
        try:
            stmt = select(keyword_logs).order_by(keyword_logs.id.desc())
            # stmt = select(keyword_logs).filter(func.date(keyword_logs.cdate) == date.date()).order_by(keyword_logs.id.desc())
            if inf > 0:
                stmt = stmt.limit(inf)
            
            result = await self.db.execute(stmt)
            
            if result is None:
                return []
            
            rows = result.scalars().all()
            ic (rows)
            return rows
        except SQLAlchemyError as e:
            ic(f"ERR Clogs select: {str(e)}")
            return None