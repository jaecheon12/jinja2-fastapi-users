from sqlalchemy.ext.declarative import declarative_base
from typing import Optional, List
from pydantic import BaseModel
from datetime import datetime

Base = declarative_base()

class Country:
    def __init__(self, id, name, code, nationUnion, lang, oldFlag):
        self.id     : int = id
        self.name   : str = name
        self.code   : str = code
        self.nationUnion: int = nationUnion
        self.lang   : int = lang
        self.oldFlag: int = oldFlag

    def to_dict(self):
        return {
            "id": self.id,  
            "name": self.name,
            "code": self.code,
            "nationUnion": self.nationUnion,
            "lang": self.lang,
            "oldFlag": self.oldFlag
        }

class Language:
    def __init__(self, id, name, code):
        self.id: int = id
        self.name: str = name
        self.code: str = code
    
    def to_dict(self):
        return {
            "id": self.id,  
            "name": self.name,
            "code": self.code,
        }

class NochulMeche:
    def __init__(self, id, name, oldFlag, nochul):
        self.id: int = id
        self.name: str = name
        self.oldFlag: int = oldFlag
        self.nochul: int = nochul

    def to_dict(self):
        return {
            "id": self.id,  
            "name": self.name,
            "oldFlag": self.oldFlag,
            "nochul": self.nochul
        }

class GenreTopic:
    def __init__(self, id, name, gname):
        self.id: int = id
        self.name: str = name
        self.gname: str = gname

    def to_dict(self):
        return {
            "id": self.id,  
            "name": self.name,
            "gname": self.gname,
        }

class Staff:
    def __init__(self, makerId, makerName, cut, etc):
        self.MakerId: str = makerId
        self.MakerName: str = makerName
        self.Cut: str = cut
        self.Etc: str = etc
    
    def to_dict(self):
        return {
            "MakerId": self.MakerId,  
            "MakerName": self.MakerName,
            "Cut": self.Cut,
            "Etc": self.Etc
        }
        

class YoutubeVideo(BaseModel):
    id: str
    title: str
    description: str
    tags: List[str]
    logo: str
    publishedAt: datetime|str
    url: str
    duration: float
    lang: str
    videoViewCount: int
    videoLikeCount: int
    videoCommentCount: int

class YoutubeChannel(BaseModel):
    id: str
    title: str
    description: str
    logo: str
    country: str
    publishedAt: datetime|str
    url: str
    viewCount: int
    videoCount: int
    hiddenSubscriberCount: bool
    subscriberCount: Optional[int]
    TvcfFirstAdder: str

class YoutubeInfo(BaseModel):
    twice: Optional[int]
    twices: Optional[List[int]]
    videoId: str
    video: YoutubeVideo
    channel: YoutubeChannel
    err: str = ""
    
class VimeoInfo(BaseModel):
    id: str
    title: str
    description: str
    cut: str
    durationStr: str
    tag: str
    