from datetime import datetime
from icecream import ic

def str_to_onair(date_str: str) -> int:
    try:
        if not date_str:
            return 0
        return int(datetime.strptime(date_str, "%Y-%m-%d").strftime("%Y%m%d"))
    except BaseException as e:
        ic("ERR str_to_onair: ", str(e))
        return 0

def string_to_list(s: str) -> list:
    return s.split(",") if s else []

def string_to_list(input_string:str, space:bool = False) -> list:
    try:
        if not input_string:
            return []
        
        cleaned_text = input_string.replace(",,", ",").replace("\n", "")    
        
        if space:
            cleaned_text = cleaned_text.replace(" ", "")
        
        return cleaned_text.split(",")
    except BaseException as e:
        ic("ERR string_to_list: ", str(e))
        return []
