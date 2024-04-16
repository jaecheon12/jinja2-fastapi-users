from sqlalchemy.orm import Session
from sqlalchemy.exc import SQLAlchemyError
from src.models.FestivalAwards_TM import FestivalAwards_TM as AwardTM
from icecream import ic
import logging

class CtrlFestivalAwards_TM:
    def __init__(self, db: Session):
        self.db = db

    def selectName(self, sisang: str) -> AwardTM|None:
        try:
            result = self.db.query(AwardTM).filter( AwardTM.AwardName == sisang,
                                                    AwardTM.State != -1
                                                    ).first()
            return result
        except SQLAlchemyError as e:
            ic(f"ERR CFestivalAwards_TM selectAwardsName: {str(e)}")
            logging.error(f"ERR CFestivalAwards_TM selectName: {e}")
            return None


    def selectSisang(self, index: str) -> AwardTM|None:
        try:
            result = self.db.query(AwardTM).filter(AwardTM.Idx == index).first()
            return result
        except SQLAlchemyError as e:
            ic(f"ERR CFestivalAwards_TM selectAwardsName: {str(e)}")
            logging.error(f"ERR CFestivalAwards_TM selectSisang: {e}")
            return None


    def insert(self, award: AwardTM) -> bool:
        try:
            self.db.add(award)
            return True
        except SQLAlchemyError as e:
            ic(f"ERR CFestivalAwards_TM insert: {str(e)}")
            logging.error(f"ERR CFestivalAwards_TM insert: {e}")
            return False


    def updateCancelFestivalAwardsTM(self, mediaIdx: int) -> list[AwardTM]|None:
        try:
            awardList = self.db.query(AwardTM).filter(AwardTM.Idx == mediaIdx).all()
            if awardList :
                for award in awardList:
                    award.State = -1
            return awardList
        except SQLAlchemyError as e:
            ic(f"ERR CFestivalAwards_TM updateCancel: {str(e)}")
            logging.error(f"ERR CFestivalAwards_TM updateCancel: {e}")
            return None
