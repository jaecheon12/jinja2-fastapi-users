from pydantic import BaseModel
from pytz import timezone


CONST_TIMEZONE_UTC = timezone('UTC')
CONST_TIMEZONE_KST = timezone('Asia/Seoul')


class Iselect_media(BaseModel):
    code: str
