from sqlalchemy import Column, Integer, String, BigInteger, DateTime, SmallInteger
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime
from src.static.const import CONST_TIMEZONE_KST

Base = declarative_base()

class Const_TM(Base):
    __tablename__ = 'Const_TM'
    __table_args__ = {'extend_existing': True}

    Idx = Column(Integer, primary_key=True, autoincrement=True)
    GName = Column(String)
    CName = Column(String)
    CNameASP = Column(String)
    CValue = Column(BigInteger)
    Sunse = Column(SmallInteger)  # Assuming Byte in C# is equivalent to SmallInteger in SQLAlchemy
    Flag = Column(BigInteger)
    Flag2 = Column(BigInteger)
    GeekJong = Column(BigInteger)
    UpJong = Column(BigInteger)
    Target = Column(String)
    Descript = Column(String)
    CDate = Column(DateTime)
    UDate = Column(DateTime)
    State = Column(Integer)
    
    def to_dict(self):
        return {
            "Idx": self.Idx,
            "GName": self.GName,
            "CName": self.CName,
            "CNameASP": self.CNameASP,
            "CValue": self.CValue,
            "Sunse": self.Sunse,
            "Flag": self.Flag,
            "Flag2": self.Flag2,
            "GeekJong": self.GeekJong,
            "UpJong": self.UpJong,
            "Target": self.Target,
            "Descript": self.Descript,
            "CDate": (self.CDate).isoformat(),
            "UDate": (self.UDate).isoformat(),
            "State": self.State
        }
    
    def toPumsDict(self):
        return {
            "gname": self.GName,
            "id": self.CValue,
            "name": self.CName,
            "pumOne": self.Flag,
            "pumTwo": self.Flag2
        }
    

class Const_TM_insert(Base):
    __tablename__ = 'Const_TM'
    __table_args__ = {'extend_existing': True}

    GName = Column(String)
    CName = Column(String)
    CNameASP = Column(String)
    CValue = Column(BigInteger)
    Sunse = Column(SmallInteger)
    Flag = Column(BigInteger, default = 0)
    Flag2 = Column(BigInteger, default = 0)
    GeekJong = Column(BigInteger, default = 0)
    UpJong = Column(BigInteger, default = 0)    
    Target = Column(String)
    Descript = Column(String, default = "")
    CDate = Column(DateTime, default = datetime.now(CONST_TIMEZONE_KST))
    UDate = Column(DateTime, default = datetime.now(CONST_TIMEZONE_KST))
    State = Column(Integer, default = 1)    
