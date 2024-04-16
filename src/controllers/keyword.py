
from sqlalchemy.orm import Session
from sqlalchemy.exc import SQLAlchemyError
from src.models.Keyword_TM import Keyword_TM
from icecream import ic


class CtrlKeyword:
    def __init__(self, db: Session):
        self.db = db

    def select_bycode(self, code: str) -> Keyword_TM|None:
        try:
            result = self.db.query(Keyword_TM).filter(Keyword_TM.Code == code).first()
            return result
        except SQLAlchemyError as e:
            ic(f"ERR select_bycode: {str(e)}")
            return None

    def update(self, code: str, src: Keyword_TM) -> bool:
        try:
            resKeyword = self.db.query(Keyword_TM).filter(Keyword_TM.Code == code).first()

            if resKeyword:
                resKeyword.Contents = src.Contents
                resKeyword.keycode = src.keycode
                resKeyword.keycontents = src.keycontents
                resKeyword.kw_feeling = src.kw_feeling
                resKeyword.kw_things = src.kw_things
                resKeyword.kw_theme = src.kw_theme
                resKeyword.kw_etc = src.kw_etc
            return True
        except SQLAlchemyError as e:
            ic(f"ERR update: {str(e)}")
            return False

