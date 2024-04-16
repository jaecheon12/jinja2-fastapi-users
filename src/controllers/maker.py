
from sqlalchemy.orm import Session
from src.models.Maker_TM import Maker_TM as Maker
from icecream import ic

class CtrlMaker:
    def __init__(self, db: Session):
        self.db = db

    def select(self, code: str) -> Maker|None:
        try:
            result = self.db.query(Maker).filter(Maker.Code == code).first()
            return result
        except BaseException as e:
            ic(f"ERR CtrlMaker select: {str(e)}")
            return None

    def select_all(self, code: str) -> list[Maker]|None:
        try:
            result = self.db.query(Maker).filter(Maker.Code == code).all()
            return result
        except BaseException as e:
            ic(f"ERR CtrlMaker select_all: {str(e)}")
            return None
