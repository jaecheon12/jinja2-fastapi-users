from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime
from src.static.const import CONST_TIMEZONE_KST

Base = declarative_base()

class FestivalAwardsPart(Base):
    __tablename__ = 'FestivalAwardsPart_TM'
    __table_args__ = {'extend_existing': True}

    Idx = Column(Integer, primary_key=True, autoincrement=True)
    FestivalAwardIdx = Column(Integer, nullable=False)
    GName = Column(String, nullable=False)
    CName = Column(String, nullable=False)
    CNameASP = Column(String, default="")
    CValue = Column(Integer, nullable=False)
    Ordering = Column(Integer, default=999)
    State = Column(Integer, default=0)
    CUserId = Column(String, nullable=False)
    UDate = Column(DateTime, default=datetime.now(CONST_TIMEZONE_KST))
    UUserId = Column(String, nullable=False)


class FestivalAwardsPart_insert(Base):
    __tablename__ = 'FestivalAwardsPart_TM'
    __table_args__ = {'extend_existing': True}

    FestivalAwardIdx = Column(Integer, nullable=False)
    GName = Column(String, nullable=False)
    CName = Column(String, nullable=False)
    CNameASP = Column(String, default="")
    CValue = Column(Integer, nullable=False)
    Ordering = Column(Integer, default=999)
    State = Column(Integer, default=0)
    CUserId = Column(String, nullable=False)
    CDate = Column(DateTime, nullable=False, default=datetime.now(CONST_TIMEZONE_KST))
    UDate = Column(DateTime, default=datetime.now(CONST_TIMEZONE_KST), onupdate=datetime.now(CONST_TIMEZONE_KST))
    UUserId = Column(String, nullable=False)

