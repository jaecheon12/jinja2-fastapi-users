from sqlalchemy import Column, Integer, String, Boolean, DateTime, SmallInteger
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime
from src.static.const import CONST_TIMEZONE_KST

Base = declarative_base()

class Keyword_TM(Base):
    __tablename__ = 'Keyword_TM'

    Idx = Column(Integer, primary_key=True, autoincrement=True)
    UserId = Column(String)
    Code = Column(String)
    Gubun = Column(String, default="")
    Contents = Column(String, default="")
    keycode = Column(String, default="")
    keycontents = Column(String, default="")
    kw_feeling = Column(String, default="")
    kw_things = Column(String, default="")
    kw_theme = Column(String, default="")
    kw_etc = Column(String, default="")
    isflag = Column(Boolean, default=True)
    adm_check = Column(Boolean, default=False)
    adm_naegong = Column(SmallInteger, default=0)
    createDate = Column(DateTime, default=datetime.now(CONST_TIMEZONE_KST))
    keycodeChkBox = Column(String, default="")
    UDate = Column(DateTime, default=datetime.now(CONST_TIMEZONE_KST))
    videlGubunCheck = Column(Integer, default=0)
    
    def to_dict(self):
        return {
            "Code": self.Code,
            "Contents": self.Contents,
            "keycode": self.keycode,
            "keycontents": self.keycontents,
            "kw_feeling": self.kw_feeling,
            "kw_things": self.kw_things,
            "kw_theme": self.kw_theme,
            "kw_etc": self.kw_etc,
            "udate": (self.UDate).isoformat()
        }
        