from fastapi import APIRouter, Depends, Request, HTTPException, Form
from fastapi.responses import JSONResponse
from fastapi.templating import Jinja2Templates
from sqlalchemy.orm import Session
from src.static.const import Iselect_media
from src.models.db import get_db
from src.controllers.media import CMedia
from src.controllers.keyword import CKeyword
from src.static.utils import string_to_list
from src.classes.keyword import Keywords
from icecream import ic
from dotenv import dotenv_values
from sqlalchemy.exc import SQLAlchemyError
from datetime import datetime
from src.static.const import CONST_TIMEZONE_KST

config = dotenv_values(".env") 

keyword_router = APIRouter()
templates = Jinja2Templates(directory="templates")
ckeywords = Keywords()


@keyword_router.post("/media1")
async def select_media(request: Request, search_type: str = Form(...), code: str = Form(...), db: Session = Depends(get_db)):
    
    resKeyword = CKeyword(db).select_bycode(code)
    resMedia = CMedia(db).selectCode(code)
    
    image_path = (config["G_PATH_SBIMG"] + 
                  resMedia.Folder + "/" + 
                  resMedia.Code + resMedia.Hash + "_y1.jpg") if resMedia else ""
    
    ic(image_path)
    
    if resKeyword:
        ckeywords.set_keyword("keywords1", code, 
                              string_to_list(resKeyword.Contents, True),
                              string_to_list(resKeyword.keycode, True),
                              string_to_list(resKeyword.kw_etc, True),
                              image_path)
        
    context = {"request": request}
    context["keywords1"] = ckeywords.get_keywords()["keywords1"]
    context["keywords2"] = ckeywords.get_keywords()["keywords2"]
        
    return templates.TemplateResponse("keyword.html", context)
    

@keyword_router.post("/media2")
async def select_media(request: Request, search_type: str = Form(...), code: str = Form(...), db: Session = Depends(get_db)):
    try:
        
        resKeyword = CKeyword(db).select_bycode(code)
        resMedia = CMedia(db).selectCode(code)
        
        image_path = (config["G_PATH_SBIMG"] + 
                    resMedia.Folder + "/" + 
                    resMedia.Code + resMedia.Hash + "_y1.jpg") if resMedia else ""
                
        if resKeyword and resMedia:
            ckeywords.set_keyword("keywords2", code, 
                                  string_to_list(resKeyword.Contents, True),
                                  string_to_list(resKeyword.keycode, True),
                                  string_to_list(resKeyword.kw_etc, True),
                                  image_path)
            
            context = {"request": request}
            context["keywords1"] = ckeywords.get_keywords()["keywords1"]
            context["keywords2"] = ckeywords.get_keywords()["keywords2"]
                
            return templates.TemplateResponse("keyword.html", context)
        else:
            context = {"request": request}
            context["ERR"] = "Failed to find keyword content"
            context["keywords1"] = ckeywords.get_keywords()["keywords1"]
            context["keywords2"] = ckeywords.init_keyword("keywords2")
            return templates.TemplateResponse("keyword.html", context)
    
    except SQLAlchemyError as e:
        ic(e)
        db.rollback()
        context = {"request": request}
        context["ERR"] = str(e)
        context["keywords1"] = ckeywords.get_keywords()["keywords1"]
        context["keywords2"] = ckeywords.get_keywords()["keywords2"]
        return templates.TemplateResponse("keyword.html", context)    
    
    except Exception as e:
        ic(e)
        context = {"request": request}
        context["ERR"] = str(e)
        context["keywords1"] = ckeywords.get_keywords()["keywords1"]
        context["keywords2"] = ckeywords.get_keywords()["keywords2"]
        return templates.TemplateResponse("keyword.html", context)


@keyword_router.post("/copy")
async def copy_keyword(request: Request, code1: str = Form(...), code2: str = Form(...), db: Session = Depends(get_db)):
    try:
        ic(code1, code2)
        keyword = CKeyword(db)
        
        src = keyword.select_bycode(code1)
        dst = keyword.select_bycode(code2)
        
        if src and dst:
            dst.Contents = src.Contents
            dst.keycode = src.keycode
            dst.keycontents = src.keycontents
            dst.kw_feeling = src.kw_feeling
            dst.kw_things = src.kw_things
            dst.kw_theme = src.kw_theme
            dst.kw_etc = src.kw_etc
            dst.UDate = datetime.now(CONST_TIMEZONE_KST)
            
            db.commit()
            
            resMedia = CMedia(db).selectCode(code2)
            
            image_path = (config["G_PATH_SBIMG"] + 
                          resMedia.Folder + "/" + 
                          resMedia.Code + resMedia.Hash + "_y1.jpg") if resMedia else ""
            
            ckeywords.set_keyword("keywords2", code2, 
                                    string_to_list(dst.Contents, True),
                                    string_to_list(dst.keycode, True),
                                    string_to_list(dst.kw_etc, True),
                                    image_path)
            
            context = {"request": request}
            context["keywords1"] = ckeywords.get_keywords()["keywords1"]
            context["keywords2"] = ckeywords.get_keywords()["keywords2"]
            
            return templates.TemplateResponse("keyword.html", context)
        else:
            db.rollback()
            context = {"request": request}
            context["ERR"] = "Failed to find keyword content"
            context["keywords1"] = ckeywords.get_keywords()["keywords1"]
            context["keywords2"] = ckeywords.get_keywords()["keywords2"]
            return templates.TemplateResponse("keyword.html", context)
    
    except SQLAlchemyError as e:
        ic(e)
        db.rollback()
        context = {"request": request}
        context["ERR"] = str(e)
        context["keywords1"] = ckeywords.get_keywords()["keywords1"]
        context["keywords2"] = ckeywords.get_keywords()["keywords2"]
        return templates.TemplateResponse("keyword.html", context)    
    
    except Exception as e:
        ic(e)
        context = {"request": request}
        context["ERR"] = str(e)
        context["keywords1"] = ckeywords.get_keywords()["keywords1"]
        context["keywords2"] = ckeywords.get_keywords()["keywords2"]
        return templates.TemplateResponse("keyword.html", context)
    
    

@keyword_router.get("/")
async def index(request: Request):
    
    ckeywords.init_keywords()
    context = {"request": request}
        
    return templates.TemplateResponse("keyword.html", context)
