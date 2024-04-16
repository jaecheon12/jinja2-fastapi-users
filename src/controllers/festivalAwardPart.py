from sqlalchemy.orm import Session
from sqlalchemy.exc import SQLAlchemyError
from src.models.FestivalAwards_Part import FestivalAwardsPart as Awards
from sqlalchemy import or_
from icecream import ic
import logging


class CtrlFestivalAwardPart:
    def __init__(self, db: Session):
        self.db = db

    def selectPart(self, id: int, name: str) -> Awards|None:
        try:
            result = self.db.query(Awards).filter(  Awards.FestivalAwardIdx == id,
                                                    Awards.CName == name,
                                                    Awards.GName == "AwardParts",
                                                    Awards.State != -1
                                                    ).first()
            return result
        except SQLAlchemyError as e:
            ic(f"ERR CFestivalAwardPart selectPart: {str(e)}")
            logging.error(f"ERR CFestivalAwardPart selectPart: {e}")
            return None


    def selectPartId(self, id: int, partIdx: int) -> Awards|None:
        try:
            result = self.db.query(Awards).filter(  Awards.FestivalAwardIdx == id,
                                                    or_(Awards.State == 1, Awards.State == 2),
                                                    Awards.GName == "AwardParts",
                                                    Awards.CValue == partIdx
                                                    ).first()
            return result
        except SQLAlchemyError as e:
            ic(f"ERR CFestivalAwardPart selectPartId: {str(e)}")
            logging.error(f"ERR CFestivalAwardPart selectPartId: {e}")
            return None


    def getPartId(self) -> int:
        try:
            result = self.db.query(Awards).filter(Awards.GName == "AwardParts").order_by((Awards.CValue).desc()).first()
            return result.CValue + 1
        except SQLAlchemyError as e:
            ic(f"ERR CFestivalAwardPart getPartId: {str(e)}")
            logging.error(f"ERR CFestivalAwardPart getPartId: {e}")
            return -1


    def selectPrize(self, id: int, name: str):
        try:
            result = self.db.query(Awards).filter(  Awards.FestivalAwardIdx == id,
                                                    Awards.CName == name,
                                                    Awards.GName == "AwardPrizes",
                                                    Awards.State != -1
                                                    ).first()
            return result
        except SQLAlchemyError as e:
            ic(f"ERR CFestivalAwardPart selectPrize: {str(e)}")
            logging.error(f"ERR CFestivalAwardPart selectPrize: {e}")
            return None


    def selectPrizeId(self, id: int, prizeIdx: int):
        try:
            result = self.db.query(Awards).filter(  Awards.FestivalAwardIdx == id,
                                                    Awards.GName == "AwardPrizes",
                                                    Awards.CValue == prizeIdx
                                                    ).filter(or_(Awards.State == 1, Awards.State == 2)
                                                    ).first()
            return result
        except SQLAlchemyError as e:
            ic(f"ERR CFestivalAwardPart selectPrizeId: {str(e)}")
            logging.error(f"ERR CFestivalAwardPart selectPrizeId: {e}")
            return None


    def insert(self, award: Awards) -> bool:
        try:
            self.db.add(award)
            return True
        except SQLAlchemyError as e:
            ic(f"ERR CFestivalAwardPart insert: {str(e)}")
            logging.error(f"ERR CFestivalAwardPart insert: {e}")
            return False


    def getPrizes_id(self) -> int:
        try:
            result = self.db.query(Awards).filter(Awards.GName == "AwardPrizes").order_by((Awards.CValue).desc()).first()
            return result.CValue + 1
        except SQLAlchemyError as e:
            ic(f"ERR CFestivalAwardPart getPrizes_id: {str(e)}")
            logging.error(f"ERR CFestivalAwardPart getPrizes_id: {e}")
            return -1
