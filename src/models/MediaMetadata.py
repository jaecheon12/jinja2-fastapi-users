from sqlalchemy import Row
from sqlalchemy.ext.declarative import declarative_base
from pydantic import BaseModel
from typing import Optional

Base = declarative_base()

class ILang(BaseModel):
    id: int     # 4
    name: str   # 영어
    code: str   # kr


class ICountry(BaseModel):
    id: int 
    name: str           # 대한민국
    code: str           # kr
    nationUnion: int    # 1
    lang: int           # 4
    oldFlag: int        # AFlag or BFlag


class INochulMeche(BaseModel):
    id: int             # 4
    name: str           # 극장
    oldFlag: int        # AFlag or BFlag
    nochul: int         # nochul flag = 1:광고, 2:비디오....        
    

class IGenreTopic(BaseModel):
    id: int
    name: str
    gname: str


class IItem(BaseModel):
    id: Optional[int] = None
    name: str


class Item:
    def __init__(self, id, name):
        self.id: int = id
        self.name: str = name
        
    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name
        }


class IStaff(BaseModel):
    MakerId: str
    MakerName: str
    Cut: str
    Etc: str


class IAwardItem(BaseModel):
    id: int
    name: str


class IAward(BaseModel):
    year: IAwardItem
    sisang: IAwardItem
    part: IAwardItem
    prize: IAwardItem

class AwardItem:
    def __init__(self, id, name):
        self.id: int = id
        self.name: str = name

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name
        }

class Award:
    def __init__(self, year, sisang, part, prize):
        self.year   : IAwardItem = year
        self.sisang : IAwardItem = sisang
        self.part   : IAwardItem = part
        self.prize  : IAwardItem = prize
    
    def to_dict(self):
        return {
            "year": self.year,
            "sisang": self.sisang,
            "part": self.part,
            "prize": self.prize
        }


class ISelectUser(BaseModel):
    userId: str


class IUserEmail(BaseModel):
    userId: str
    email: str


class IMediaMetadata(BaseModel):
    userId: str
    country: ICountry
    lang: Optional[ILang]
    nochulMeches: list[INochulMeche]
    genreTopics: Optional[list[IGenreTopic]] = None
    mIdx: int
    onair: int
    year: IItem
    month: IItem
    day: IItem
    pumOne: Optional[IItem] = None
    pumTwo: Optional[IItem] = None
    pumThree: Optional[IItem] = None
    title: Optional[IItem] = None
    chapter: Optional[IItem] = None
    campaign: Optional[IItem] = None
    staffs: Optional[Optional[list[Optional[list[Optional[IStaff]]]]]] = None
    awards: Optional[list[IAward]] = None
    etcinfo: str
    tag: str
    copyText: str
    fromMsg: str
    useReaction: int
    mediaType: int
    urf: str
    urfType: int
    fileSize: int
    flag3: float
    flag5: float
    code: str
    folder: str
    hash: str
    duration: float
    videoBrand: str
    videoLang: str
    channelId: str
    channelCountry: str
    channelUrl: str
    channelLogo: str
    channelTitle: str
    width: int
    height: int
    qt: int
    isAdmin: bool
    mocr: str
    
    
class MediaMetadata:
    userId: str = ""
    uIdx: int = 0
    country: Optional[dict] = None
    lang: Optional[dict] = None # Assuming Lang is a class you have defined
    nochulMeches: list = []  # Assuming INochulMeche is a class you have defined
    genreTopics: list = []  # Assuming IGenreTopic is a class you have defined
    mIdx: int = 0
    onair: int = 0
    year: Optional[dict] = None
    month: Optional[dict] = None
    day: Optional[dict] = None
    year2: str = ""
    month2: str = ""
    day2: str = ""
    pumOne: Optional[dict] = None
    pumTwo: Optional[dict] = None
    pumThree: Optional[dict] = None
    title: Optional[dict] = None
    chapter: Optional[dict] = None
    campaign: Optional[dict] = None
    thumbnail: str = ""
    staffs: list = []  # Assuming IStaff is a class you have defined
    awards: list = []  # Assuming IAward is a class you have defined
    etcinfo: str = ""
    tag: str = ""
    copyText: str = ""
    fromMsg: str = ""
    useReaction: int = 0
    mediaType: int = 0
    urf: str = ""
    urfType: int = 0
    flag3: float = 0.0
    flag5: float = 0.0
    code: str = ""
    folder: str = ""
    hash: str = ""
    duration: float = 0.0
    durationStr: str = ""
    uFileName: str = ""
    videoBrand: str = ""
    videoLang: str = ""
    channelId: str = ""
    channelCountry: str = ""
    channelUrl: str = ""
    channelLogo: str = ""
    channelTitle: str = ""
    width: int = 0
    height: int = 0
    qt: int = 0
    isAdmin: bool = False
    mocr: str = ""
    
    def to_dict(self):
        try:
            serializable_dict = {}
            for attr, value in self.__dict__.items():
                if isinstance(value, Row):  # If value is a Row object, convert it to a dict
                    print("row", attr, value)
                    serializable_dict[attr] = dict(value)
                elif hasattr(value, 'to_dict'):  
                    print("to_dict",attr, value)
                    serializable_dict[attr] = value.to_dict()
                else:
                    serializable_dict[attr] = value
            return serializable_dict
        except Exception as e:
            print("err metadata to_dict: ", str(e))
            return None
        
class IOthers(BaseModel):
    mediaIndex: int
    relayIndex: int
    msg: str
    userId: str
