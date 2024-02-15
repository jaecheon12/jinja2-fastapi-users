from sqlalchemy import Column, Integer, String, DateTime, BigInteger
from sqlalchemy.ext.declarative import declarative_base
from typing import Optional
from datetime import datetime
from src.static.const import CONST_TIMEZONE_KST

Base = declarative_base()

class Maker_TM(Base):
    __tablename__ = 'Maker_TM'
    __table_args__ = {'extend_existing': True}

    Idx = Column(Integer, primary_key=True, autoincrement=True)
    Code = Column(String)
    MakerPart = Column(BigInteger, default=2)
    MakerId = Column(String, default="")
    MakerName = Column(String)
    CUserId = Column(String)
    UUserId = Column(String)
    CDate = Column(DateTime)
    UDate = Column(DateTime)
    Flag = Column(BigInteger, default=1)
    State = Column(Integer, default=1)
    Sunse = Column(Integer, default=0)
    
    def to_dict(self):
        return {
            "Idx": self.Idx,
            "Code": self.Code,
            "MakerPart": self.MakerPart,
            "MakerId": self.MakerId,
            "MakerName": self.MakerName,
            "Flag": self.Flag,
            "State": self.State,
        }  
    