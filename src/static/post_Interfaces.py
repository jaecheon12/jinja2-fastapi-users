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
    
class IOthers(BaseModel):
    userId: str 
    mediaIndex: int
    relayIndex: int
    msg: str
    

class IOthersUpdate(BaseModel):
    userId: str 
    uIndex: int
    
class IOthersSelect(BaseModel):
    gid: str 
    idx: int
    
class OthersMedia(BaseModel):
    index: int
    type: int
    name: str
    
class iOthersUpload(BaseModel):
    userId: str
    title: str
    mediaList: list[OthersMedia]
    mainIndex: int

class IMaker_insert(BaseModel):
    makerName: str
    userId: str
    
class IMaker_update(BaseModel):
    makerId: int
    state: int
    
class patch_status(BaseModel):
    userId: str
    mediaIndex: int
    urfType: int        # 1: local, 2: youtube, 3: vimeo
    status: int         # 0: 삭제, 1: 승인, 2: 숨김, 3: 대기
    reason: int         # hidden reason: 1(화질), 2(요청), 3(자막), 4(기타)
    
    