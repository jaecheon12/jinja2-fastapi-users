from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from src.models.Media_TM import Media_TM, Media_TM_NoFolder
from src.controllers.const import CConst
from src.static.utils import str_to_onair
from src.static.post_Interfaces import IVideoFile
from src.static.const import CONST_TIMEZONE_KST
from datetime import datetime
from icecream import ic
import re

class CtrlMedia:
    def __init__(self, db: AsyncSession):
        self.db = db
        
    async def getMediaCode(self, mediaType: int) -> str:
        try:
            whenLike = 'A%' if mediaType == 1 else 'B%'
            result = await self.db.execute(select(Media_TM.Code).order_by(Media_TM.Idx.desc()).filter(Media_TM.Code.like(whenLike)).limit(1))
            result = result.scalars().first()
            numbers = int(re.sub(r'[^0-9]', "", result)) + 1
            
            return ('A' if mediaType == 1 else 'B') + str(numbers).zfill(9)
        except BaseException as e:
            ic(f"ERR getMediaCode: {str(e)}")
            return ""
        
    async def insertMedia(self, video: IVideoFile, code: str):
        try:
            ic("insertMedia", video, code)
            qCountry = await CConst(self.db).selectCountryChannel(video.channelCountry)

            media = Media_TM_NoFolder(Code=code, 
                                      State=2,
                                      Flag3=4 + 8388608 + 134217728 if video.urfType > 1 else 4, 
                                      Country=0 if not qCountry else qCountry.CValue,
                                      ChannelCountry="" if not qCountry else qCountry.CName,
                                      OnAir=str_to_onair(video.videoPublishedAt),
                                      Urf=video.urf, 
                                      MediaType=video.mediaType, 
                                      VideoId=video.videoId,
                                      ChannelId=video.channelId,
                                      VideoBrand=video.videoBrand,
                                      VideoLang=video.videoLang,
                                      Duration=video.videoDuration, 
                                      VideoDuration=video.videoDuration, 
                                      VideoViewCount=video.videoViewCount,
                                      VideoLikeCount=video.videoLikeCount,
                                      VideoCommentCount=video.videoCommentCount)
            self.db.add(media)
            await self.db.commit()
            return media
        except BaseException as e:
            ic("err insertMedia: ", str(e))
            await self.db.rollback()
            return None

    async def selectIdx(self, mediaIdx: int) -> Media_TM|None:
        try:
            result = await self.db.execute(select(Media_TM).filter(Media_TM.Idx == mediaIdx))
            return result.scalars().first()
        except BaseException as e:
            ic("err selectIdx: ", str(e))
            return None

    async def selectCode(self, mediaCode: str) -> Media_TM|None:
        try:
            result = await self.db.execute(select(Media_TM).filter(Media_TM.Code == mediaCode))
            return result.scalars().first()
        except BaseException as e:
            ic("err selectCode: ", str(e))
            return None

    async def selectAllVideoId(self, videoId: str) -> list[Media_TM]:
        try:
            result = await self.db.execute(select(Media_TM.Idx).filter(Media_TM.State == 1, Media_TM.VideoId == videoId))
            return result.scalars().all()
        except BaseException as e:
            ic("err selectAllVideoId: ", str(e))
            return []

    async def countChannelId(self, ChannelId: str) -> int:
        try:
            result = await self.db.execute(select(Media_TM).filter(Media_TM.ChannelId == ChannelId, Media_TM.State == 1))
            return result.scalars().count()
        except BaseException as e:
            ic("err countChannelId: ", str(e))
            return 0

    async def setMediaState(self, mediaIdx: int, type: int, state: int, reason: int, user_id: str) -> bool:
        try:
            result = await self.db.execute(select(Media_TM).filter(Media_TM.Idx == mediaIdx))
            resMedia = result.scalars().first()
            if resMedia:  
                resMedia.State = state
                resMedia.HiddenReason = reason if state == 2 else 0
                resMedia.UDate = datetime.now(CONST_TIMEZONE_KST)
                
            if type > 1:
                resMedia.Urf = ""
            
            if state == 0:
                resMedia.VideoId = ""
            
            await self.db.commit()
            return True
        except BaseException as e:
            ic("err setMediaState: ", str(e))
            await self.db.rollback()
            return False