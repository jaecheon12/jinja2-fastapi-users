

from sqlalchemy.orm import Session
from src.models.Media_TM import Media_TM, Media_TM_NoFolder
from src.controllers.const import CConst
from src.static.utils import str_to_onair
from src.static.post_Interfaces import IVideoFile
from src.static.const import CONST_TIMEZONE_KST
from datetime import datetime
from icecream import ic
import logging
import re

class CtrlMedia:
    def __init__(self, db: Session):
        self.db = db

    def getMediaCode(self, mediaType: int) -> str:
        try:
            whenLike = 'A%' if mediaType == 1 else 'B%'
            result = self.db.query(Media_TM.Code).order_by((Media_TM.Idx).desc()).filter(Media_TM.Code.like(whenLike)).first()
            numbers = int(re.sub(r'[^0-9]', "", result[0])) + 1

            return ('A' if mediaType == 1 else 'B') + str(numbers).zfill(9)
        except BaseException as e:
            ic(f"ERR getMediaCode: {str(e)}")
            logging.error(f"ERR getMediaCode: {e}")
            return ""

    def insertMedia(self, video: IVideoFile, code: str):
        try:
            ic("insertMedia", video, code)
            qCountry = CConst(self.db).selectCountryChannel(video.channelCountry)

            media = Media_TM_NoFolder(Code = code,
                                    State = 2,
                                    Flag3 = 4 + 8388608 + 134217728 if video.urfType > 1 else 4,
                                    Country = 0 if not qCountry else qCountry.CValue,
                                    ChannelCountry = "" if not qCountry else qCountry.CName,
                                    OnAir = str_to_onair(video.videoPublishedAt),
                                    Urf=video.urf,
                                    MediaType=video.mediaType,
                                    VideoId = video.videoId,
                                    ChannelId = video.channelId,
                                    VideoBrand = video.videoBrand,
                                    VideoLang = video.videoLang,
                                    Duration = video.videoDuration,
                                    VideoDuration = video.videoDuration,
                                    VideoViewCount = video.videoViewCount,
                                    VideoLikeCount = video.videoLikeCount,
                                    VideoCommentCount = video.videoCommentCount)
            self.db.add(media)
            return media
        except BaseException as e:
            ic("err insertMedia: ", str(e))
            logging.error(f"ERR insertMedia: {e}")
            return None


    def selectIdx(self, mediaIdx: int) -> Media_TM|None:
        try:
            result = self.db.query(Media_TM).filter(Media_TM.Idx == mediaIdx).first()
            return result
        except BaseException as e:
            ic("err selectIdx: ", str(e))
            logging.error(f"ERR selectIdx: {e}")
            return None


    def selectCode(self, mediaCode: str) -> Media_TM|None:
        try:
            result = self.db.query(Media_TM).filter(Media_TM.Code == mediaCode).first()
            return result
        except BaseException as e:
            ic("err selectCode: ", str(e))
            logging.error(f"ERR selectCode: {e}")
            return None


    def selectAllVideoId(self, videoId: str) -> Media_TM|None:
        try:
            result = self.db.query(Media_TM.Idx).filter(Media_TM.State == 1, Media_TM.VideoId == videoId).all()
            return result
        except BaseException as e:
            ic("err selectAllVideoId: ", str(e))
            logging.error(f"ERR selectAllVideoId: {e}")
            return None


    def countChannelId(self, ChannelId: str) -> int:
        try:
            result = self.db.query(Media_TM).filter(Media_TM.ChannelId == ChannelId, Media_TM.State == 1).count()
            return result
        except BaseException as e:
            ic("err countChannelId: ", str(e))
            logging.error(f"ERR countChannelId: {e}")
            return 0


    def setMediaState(self, mediaIdx: int, type: int, state: int, reason: int, user_id: str) -> bool:
        try:
            resMedia = self.db.query(Media_TM).filter(Media_TM.Idx == mediaIdx).first()
            if resMedia:
                resMedia.State = state
                resMedia.HiddenReason = reason if state == 2 else 0
                resMedia.UDate = datetime.now(CONST_TIMEZONE_KST)

                if type > 1:
                    resMedia.Urf = ""

                if state == 0:
                    resMedia.VideoId = ""

            return True
        except BaseException as e:
            ic("err setMediaState: ", str(e))
            logging.error(f"ERR setMediaState: {e}")
            return False
