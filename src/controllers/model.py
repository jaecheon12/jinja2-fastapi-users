
from sqlalchemy.orm import Session
from sqlalchemy.exc import SQLAlchemyError
from src.models.Model_tm import ModelTM
from icecream import ic


class CtrlModel:
    def __init__(self, db: Session):
        self.db = db

    def get_bycode(self, code: str) -> ModelTM|None:
        try:
            result = self.db.query(ModelTM).filter(ModelTM.Code == code).first()
            return result
        except SQLAlchemyError as e:
            ic(f"ERR select_bycode: {str(e)}")
            return None

    def get_bycode_all(self, code: str) -> list[ModelTM]|None:
        try:
            result = self.db.query(ModelTM).filter(ModelTM.Code == code).all()
            return result
        except SQLAlchemyError as e:
            ic(f"ERR select_bycode: {str(e)}")
            return None