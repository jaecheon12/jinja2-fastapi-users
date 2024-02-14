from pydantic import BaseModel

class IMakerWait_insert(BaseModel):
    userId: str
    makerName: str

class IVideoFile(BaseModel):
    urfType: int  
    urf: str
    mediaType: int
    fileSize: int
    email: str
    mobile: str
    userId: str

    videoId: str 
    channelId: str 

    channelCountry: str 
    channelAdman: str 

    videoPublishedAt: str 
    videoBrand: str 
    videoDescription: str 
    videoTag: str 
    videoLang: str
    videoDuration: str 
    videoViewCount: int 
    videoLikeCount: int 
    videoCommentCount: int 

class IVideoInfo(BaseModel):
    videoId: str

class IComplete(BaseModel):
    userId: str
    updateMediaId: int
    