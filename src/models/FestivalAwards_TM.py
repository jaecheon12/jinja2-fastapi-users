from sqlalchemy import Column, Integer, String, DateTime, BigInteger
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime
from src.static.const import CONST_TIMEZONE_KST

Base = declarative_base()

class FestivalAwards_TM(Base):
    __tablename__ = 'FestivalAwards_TM'
    __table_args__ = {'extend_existing': True}

    Idx = Column(Integer, primary_key=True, autoincrement=True)
    AwardGroup = Column(BigInteger, default=0)
    AwardLogo = Column(String, default="")
    AwardName = Column(String, nullable=False)
    AwardEngName = Column(String, default="")
    AwardDescription = Column(String, default="")
    AwardNationCode = Column(Integer, nullable=False)
    AwardCity = Column(String, nullable=False)
    AwardAddr = Column(String, default="")
    AwardAreaCode = Column(Integer)
    AwardContactNumber = Column(String, default="")
    AwardEmail = Column(String, default="")
    AwardSite = Column(String, default="")
    State = Column(Integer, default=1)
    CUserId = Column(String, nullable=False)
    UDate = Column(DateTime, default=datetime.now(CONST_TIMEZONE_KST))
    UUserId = Column(String, nullable=False)
    Ordering = Column(Integer, default=2147483647)
    AwardStart = Column(String, default="")
    AwardEnd = Column(String, default="")


class FestivalAwards_TM_insert(Base):
    __tablename__ = 'FestivalAwards_TM'
    __table_args__ = {'extend_existing': True}

    AwardGroup = Column(BigInteger, default=0)
    AwardLogo = Column(String, default="")
    AwardName = Column(String, nullable=False)
    AwardEngName = Column(String, default="")
    AwardDescription = Column(String, default="")
    AwardNationCode = Column(Integer, nullable=False)
    AwardCity = Column(String, nullable=False)
    AwardAddr = Column(String, default="")
    AwardAreaCode = Column(Integer)
    AwardContactNumber = Column(String, default="")
    AwardEmail = Column(String, default="")
    AwardSite = Column(String, default="")
    State = Column(Integer, default=1)
    CUserId = Column(String, nullable=False)
    CDate = Column(DateTime, nullable=False, default=datetime.now(CONST_TIMEZONE_KST))
    UDate = Column(DateTime, default=datetime.now(CONST_TIMEZONE_KST), onupdate=datetime.now(CONST_TIMEZONE_KST))
    UUserId = Column(String, nullable=False)
    Ordering = Column(Integer, default=2147483647)
    AwardStart = Column(String, default="")
    AwardEnd = Column(String, default="")
