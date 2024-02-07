from sqlalchemy.orm import Session
from src.models.Keyword_TM import Keyword_TM
from icecream import ic
import logging


class CKeyword:
    def __init__(self, db: Session):
        self.db = db
        
    def selectKeyword(self, mediaCode: str):
        try:
            result = self.db.query(Keyword_TM).filter(Keyword_TM.Code == mediaCode).first()
            return result
        except BaseException as e:
            ic(f"ERR selectKeyword: {str(e)}")
            logging.error(f"ERR selectKeyword: {e}")
            return None
        

    def select_bycode(self, code: str) -> Keyword_TM|None:
        try:
            result = self.db.query(Keyword_TM).filter(Keyword_TM.Code == code).first()
            return result
        except BaseException as e:
            ic(f"ERR select_bycode: {str(e)}")
            logging.error(f"ERR select_bycode: {e}")
            return None
        