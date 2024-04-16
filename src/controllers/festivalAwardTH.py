from sqlalchemy.orm import Session
from sqlalchemy.exc import SQLAlchemyError
from src.models.FestivalAwards_TH import FestivalAwards_TH as AwardTH
from sqlalchemy import or_
from icecream import ic
import logging

class CtrlFestivalAwards_TH:
    def __init__(self, db: Session):
        self.db = db

    def selectAwardsTHList(self, mediaIdx: int) -> list[AwardTH]|None:
        try:
            result = self.db.query(AwardTH).filter(AwardTH.MediaIdx == mediaIdx
                                            ).filter(or_(AwardTH.State == 1, AwardTH.State == 2)
                                            ).all()
            return result
        except SQLAlchemyError as e:
            ic(f"ERR CFestivalAwards_TH selectAwardsTHList: {str(e)}")
            logging.error(f"ERR CFestivalAwards_TH selectAwardsTHList: {e}")
            return None


    def selectAwardsTHList_top30(self) -> list[AwardTH]|None:
        try:
            result = self.db.query(AwardTH).filter(or_(AwardTH.State == 1, AwardTH.State == 2)
                                            ).order_by(AwardTH.Idx.desc()).limit(10).all()
            return result
        except SQLAlchemyError as e:
            ic(f"ERR CFestivalAwards_TH selectAwardsTHList: {str(e)}")
            logging.error(f"ERR CFestivalAwards_TH selectAwardsTHList: {e}")
            return None


    def insert(self, award: AwardTH) -> bool:
        try:
            self.db.add(award)
            return True
        except SQLAlchemyError as e:
            ic(f"ERR CFestivalAwards_TH insert: {str(e)}")
            logging.error(f"ERR CFestivalAwards_TH insert: {e}")
            return False


    def updateCancel(self, mediaIdx: int) -> list[AwardTH]|None:
        try:
            awardList = self.db.query(AwardTH).filter(AwardTH.MediaIdx == mediaIdx).all()
            if awardList :
                for award in awardList:
                    award.State = -1
            return awardList
        except SQLAlchemyError as e:
            ic(f"ERR CFestivalAwards_TH updateCancel: {str(e)}")
            logging.error(f"ERR CFestivalAwards_TH updateCancel: {e}")
            return None
