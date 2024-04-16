from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime
from src.static.const import CONST_TIMEZONE_KST

Base = declarative_base()

class FestivalAwards_TH(Base):
    __tablename__ = 'FestivalAwards_TH'
    __table_args__ = {'extend_existing': True}

    Idx = Column(Integer, primary_key=True, autoincrement=True)
    MediaIdx = Column(Integer, nullable=False)
    FestivalAwardIdx = Column(Integer, nullable=False)
    FestivalAwardYear = Column(String, default="")
    FestivalAwardPartIdx = Column(Integer, nullable=True)
    FestivalAwardPrizeIdx = Column(Integer, nullable=True)
    State = Column(Integer, default=1)
    CUserId = Column(String, nullable=False)
    UDate = Column(DateTime, default=datetime.now(CONST_TIMEZONE_KST))
    UUserId = Column(String, nullable=False)

    def to_dict(self):
        return {
            "Idx": self.Idx,
            "MediaIdx": self.MediaIdx,
            "FestivalAwardIdx": self.FestivalAwardIdx,
            "FestivalAwardYear": self.FestivalAwardYear,
            "FestivalAwardPartIdx": self.FestivalAwardPartIdx,
            "FestivalAwardPrizeIdx": self.FestivalAwardPrizeIdx,
            "State": self.State,
            "CDate": (self.CDate).isoformat(),
            "CUserId": self.CUserId,
            "UDate": (self.UDate).isoformat(),
            "UUserId": self.UUserId
        }


class FestivalAwards_TH_insert(Base):
    __tablename__ = 'FestivalAwards_TH'
    __table_args__ = {'extend_existing': True}

    MediaIdx = Column(Integer, nullable=False)
    FestivalAwardIdx = Column(Integer, nullable=False)
    FestivalAwardYear = Column(String, default="")
    FestivalAwardPartIdx = Column(Integer, nullable=True)
    FestivalAwardPrizeIdx = Column(Integer, nullable=True)
    State = Column(Integer, default=1)
    CUserId = Column(String, nullable=False)
    CDate = Column(DateTime, nullable=False, default=datetime.now(CONST_TIMEZONE_KST))
    UDate = Column(DateTime, default=datetime.now(CONST_TIMEZONE_KST), onupdate=datetime.now(CONST_TIMEZONE_KST))
    UUserId = Column(String, nullable=False)
