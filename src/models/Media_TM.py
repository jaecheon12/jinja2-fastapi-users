
from sqlalchemy import Column, Integer, String, Float, DateTime, BigInteger
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime
from src.static.const import CONST_TIMEZONE_KST
import uuid

Base = declarative_base()

class Media_TM(Base):
    __tablename__ = 'Media_TM'
    __table_args__ = {'extend_existing': True}

    Idx = Column(Integer, primary_key=True, autoincrement=True)
    Old_code = Column(String, default="")
    Code = Column(String, default="")
    MediaType = Column(Integer)
    ProductName = Column(String, default="")
    TitleFishing = Column(String, default="")
    Hash    = Column(String, default=str(uuid.uuid4())[:4])
    Folder  = Column(String, default="")
    OnAir   = Column(Integer, default=0)
    Title   = Column(String, default="")
    Brand   = Column(String, default="")
    Chapter = Column(String, default="")
    Campaign = Column(String, default="")
    Genre   = Column(BigInteger, default=0)
    PumOne  = Column(Integer, default=0)
    PumTwo  = Column(Integer, default=0)
    PumThree = Column(Integer, default=0)
    NationUnion = Column(BigInteger, default=0)
    Nation = Column(BigInteger, default=0)
    Lang    = Column(BigInteger, default=0)
    Flag    = Column(BigInteger, default=0)
    Flag2 = Column(BigInteger, default=0)
    Flag3 = Column(BigInteger, default=0)
    Flag4 = Column(BigInteger, default=0)
    Flag5 = Column(BigInteger, default=1)
    Hit   = Column(Integer, default=0)
    Width = Column(Integer, default=0)
    Height = Column(Integer, default=0)
    AspectRatio = Column(Float, default=0)
    Duration = Column(Float, default=0)
    Total = Column(Float, default=0)
    CDate = Column(DateTime, default="")
    UDate = Column(DateTime, default="")
    UseReaction = Column(Integer, default=1)
    Quality = Column(Integer, default=-999)
    Urf = Column(String, default="")
    State = Column(Integer, default=-1)
    FDate = Column(DateTime)
    CutTime = Column(Float, default=0)
    TotalNew = Column(Float, default=0)
    ExAvg1 = Column(Float, default=0)
    ExAvg2 = Column(Float, default=0)
    ExAvg3 = Column(Float, default=0)
    Qt = Column(Integer, default=4)
    Nochul = Column(BigInteger, default=0)
    Meche = Column(BigInteger, default=0)
    Country = Column(BigInteger, default=0)
    HiddenReason = Column(Integer, default=0)
    Topic = Column(BigInteger, default=0)
    VideoId = Column(String, default="")
    ChannelId = Column(String, default="")
    UrfType = Column(Integer, default=0)
    VideoBrand = Column(String, default="")
    ChannelCountry = Column(String, default="")
    VideoLang = Column(String, default="")
    VideoDuration = Column(Float, default=0)
    VideoLikeCount = Column(BigInteger, default=0)
    VideoCommentCount = Column(BigInteger, default=0)
    VideoViewCount = Column(BigInteger, default=0)
    VDate = Column(DateTime)
    TotalNewP = Column(Integer, default=0)

    
    def to_dict(self):
        return {
            "Code": self.Code,
            "Nation": self.Nation,
            "Country": self.Country,
            "Lang": self.Lang  ,
            "State": self.State,
            "OnAir": self.OnAir   ,
            "Title": self.Title   ,
            "Brand": self.Brand   ,
            "Chapter ": self.Chapter ,
            "Campaign": self.Campaign,
        }
    
class Media_TM_NoFolder(Base):
    __tablename__ = 'Media_TM'
    __table_args__ = {'extend_existing': True}

    Idx = Column(Integer, primary_key=True, autoincrement=True)
    Old_code = Column(String, default="")
    Code = Column(String, default="")
    MediaType = Column(Integer)
    Hash = Column(String, default=str(uuid.uuid4())[:4])
    OnAir = Column(Integer, default=0)
    Title = Column(String, default="")
    Brand = Column(String, default="")
    ProductName = Column(String, default="")
    Chapter = Column(String, default="")
    Campaign = Column(String, default="")
    TitleFishing = Column(String, default="")
    Genre = Column(BigInteger, default=0)
    PumOne = Column(Integer, default=0)
    PumTwo = Column(Integer, default=0)
    PumThree = Column(Integer, default=0)
    NationUnion = Column(BigInteger, default=0)
    Nation = Column(BigInteger, default=0)
    Lang = Column(BigInteger, default=0)
    Flag = Column(BigInteger, default=0)
    Flag2 = Column(BigInteger, default=0)
    Flag3 = Column(BigInteger, default=0)
    Flag4 = Column(BigInteger, default=0)
    Flag5 = Column(BigInteger, default=1)
    Hit = Column(Integer, default=0)
    Width = Column(Integer, default=0)
    Height = Column(Integer, default=0)
    AspectRatio = Column(Float, default=0)
    Duration = Column(Float, default=0)
    Total = Column(Float, default=0)
    CDate = Column(DateTime, default=datetime.now(CONST_TIMEZONE_KST))
    UDate = Column(DateTime, default=datetime.now(CONST_TIMEZONE_KST))
    UseReaction = Column(Integer, default=1)
    Quality = Column(Integer, default=-999)
    Urf = Column(String, default="")
    State = Column(Integer, default=-1)
    FDate = Column(DateTime)
    CutTime = Column(Float, default=0)
    TotalNew = Column(Float, default=0)
    ExAvg1 = Column(Float, default=0)
    ExAvg2 = Column(Float, default=0)
    ExAvg3 = Column(Float, default=0)
    Qt = Column(Integer, default=4)
    Nochul = Column(BigInteger, default=0)
    Meche = Column(BigInteger, default=0)
    Country = Column(BigInteger, default=0)
    HiddenReason = Column(Integer, default=0)
    Topic = Column(BigInteger, default=0)
    VideoId = Column(String, default="")
    ChannelId = Column(String, default="")
    UrfType = Column(Integer, default=0)
    VideoBrand = Column(String, default="")
    ChannelCountry = Column(String, default="")
    VideoLang = Column(String, default="")
    VideoDuration = Column(Float, default=0)
    VideoLikeCount = Column(BigInteger, default=0)
    VideoCommentCount = Column(BigInteger, default=0)
    VideoViewCount = Column(BigInteger, default=0)
    VDate = Column(DateTime)
    TotalNewP = Column(Integer, default=0)