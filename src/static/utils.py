from datetime import datetime
from src.models.MediaMetadata import Item
from sqlalchemy.engine.row import Row
from icecream import ic

def str_to_onair(date_str: str) -> int:
    if not date_str:
        return 0
    return int(datetime.strptime(date_str, "%Y-%m-%d").strftime("%Y%m%d"))

def to_dict(obj):
    try:
        if isinstance(obj, dict):
            return {k: to_dict(v) for k, v in obj.items()}
        elif isinstance(obj, list):
            return [to_dict(v) for v in obj]
        elif isinstance(obj, Row):
            obj = dict(obj)
            return obj
        elif isinstance(obj, datetime):
            return obj.isoformat()
        elif hasattr(obj, "__dict__"):
            return {k: to_dict(v) for k, v in obj.__dict__.items() if not k.startswith('_')}
        else:
            return obj
    except BaseException as e:
        print("err to_dict: ", str(e))     

def class_to_resdict(obj):
    try:
        print("class_to_resdict: ", obj)

        # SQLAlchemy Row 객체를 처리
        if isinstance(obj, Row):
            obj = dict(obj)

        result = vars(obj)  # Convert the object to a dictionary

        if '_sa_instance_state' in result:
            result.pop('_sa_instance_state')

        for key, value in result.items():
            # datetime 객체를 처리
            
            if isinstance(value, datetime):
                result[key] = value.isoformat()
            # 다른 복잡한 타입들을 처리할 수 있는 코드를 여기에 추가

        return result
    
    except BaseException as e:
        print("err class_to_resdict: ", str(e))     

def onair_year(onair: int) -> str:
    date = datetime.strptime(str(onair), "%Y%m%d")
    return str(date.year)

def onair_month(onair: int) -> str:
    date = datetime.strptime(str(onair), "%Y%m%d")
    return date.strftime("%m")

def onair_day(onair: int) -> str:
    date = datetime.strptime(str(onair), "%Y%m%d")
    return date.strftime("%d")

def onairYear_toItem(onair: int) -> Item:
    return Item(int(onair_year(onair)), (onair_year(onair) + "년"))

def onairMonth_toItem(onair: int) -> Item:
    return Item(int(onair_month(onair)), (onair_month(onair) + "월"))

def onairDay_toItem(onair: int) -> Item:
    return Item(int(onair_day(onair)), (onair_day(onair) + "일"))

def duration_string(sec: float) -> str:
    hours, remainder = divmod(sec, 3600)
    minutes, seconds = divmod(remainder, 60)

    s = ""
    s += f"{int(hours)}시 " if hours > 0 else ""
    s += f"{int(minutes)}분 " if minutes > 0 else ""
    s += f"{int(seconds)}초 " if seconds > 0 else ""

    if not s:
        s = "0초"

    return s

def string_to_list(s: str) -> list:
    return s.split(",") if s else []


def string_to_list(input_string:str, space:bool = False) -> list:
    if not input_string:
        return []
    
    cleaned_text = input_string.replace(",,", ",").replace("\n", "")    
    
    if space:
        cleaned_text = cleaned_text.replace(" ", "")
    
    return cleaned_text.split(",")

def flag_to_name_one(flag: int, media_type: int) -> str:
    if media_type == 1:
        return a_flag_to_name_one(flag)
    else:
        return b_flag_to_name_one(flag)


def a_flag_to_name_one(flag: int) -> str:
    if flag & 4 == 4:
        return "공중파"
    elif flag & 8 == 8:
        return "케이블"
    elif flag & 65536 == 65536:
        return "극장"
    elif flag & 16 == 16:
        return "인터넷"
    elif flag & 32768 == 32768:
        return "바이럴"
    elif flag & 4194304 == 4194304:
        return "인터렉티브"
    elif flag & 268435456 == 268435456:
        return "앰비언트"
    elif flag & 16384 == 16384:
        return "OOH"
    elif flag & 8388608 == 8388608:
        return "홍보"
    elif flag & 16777216 == 16777216:
        return "이벤트"
    elif flag & 32 == 32:
        return "메이킹"
    elif flag & 131072 == 131072:
        return "NG"
    elif flag & 64 == 64:
        return "노컷"
    elif flag & 262144 == 262144:
        return "가상광고"
    elif flag & 256 == 256:
        return "시보광고"
    else:
        return "기타"


def b_flag_to_name_one(flag: int) -> str:
    if flag & 4 == 4:
        return "신문"
    elif flag & 8 == 8:
        return "잡지"
    elif flag & 4194304 == 4194304:
        return "인터렉티브"
    elif flag & 262144 == 262144:
        return "엠비언트"
    elif flag & 131072 == 131072:
        return "Outdoor"
    elif flag & 524288 == 524288:
        return "Design"
    elif flag & 1048576 == 1048576:
        return "Branding"
    elif flag & 33554432 == 33554432:
        return "다이렉트마케팅"
    elif flag & 16777216 == 16777216:
        return "대학생작품"
    else:
        return "기타"
    