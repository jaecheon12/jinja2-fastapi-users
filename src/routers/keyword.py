from fastapi import APIRouter, Depends, Request, HTTPException, Form
from fastapi.responses import JSONResponse
from fastapi.templating import Jinja2Templates
from sqlalchemy.orm import Session
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.ext.asyncio import AsyncSession
from src.models.sql_db import get_db
from src.models.lite_db import get_lite_db, get_async_session
from src.classes.keyword import Keywords
from src.controllers.media import CMedia
from src.controllers.keyword import CKeyword
from src.controllers.logs import Clogs
from src.static.utils import string_to_list
from src.static.const import CONST_TIMEZONE_KST
from src.static.config import config
from icecream import ic
from datetime import datetime

keyword_router = APIRouter()
templates = Jinja2Templates(directory="templates")
ckeywords = Keywords()


@keyword_router.post("/media1")
async def select_media(request: Request, code: str = Form(...), db: Session = Depends(get_db)):
    try:
        resKeyword = await CKeyword(db).select_bycode(code)
        resMedia = await CMedia(db).selectCode(code)
        
        image_path = (config["G_PATH_SBIMG"] + 
                    resMedia.Folder + "/" + 
                    resMedia.Code + resMedia.Hash + "_y1.jpg") if resMedia else ""
                
        if resKeyword:
            ckeywords.set_keyword("keywords1", code, 
                                  string_to_list(resKeyword.Contents, True),
                                  string_to_list(resKeyword.keycode, True),
                                  string_to_list(resKeyword.kw_etc, True),
                                  image_path)
            
            context = {"request": request}
            update_context_with_keywords(context)
                
            return templates.TemplateResponse("keyword.html", context)
        else:
            context = {"request": request}
            context["ERR"] = "Failed to find keyword content"
            context["keywords1"] = ckeywords.init_keyword("keywords1")
            context["keywords2"] = ckeywords.get_keywords()["keywords2"]
            return templates.TemplateResponse("keyword.html", context)
    
    except SQLAlchemyError as e:
        ic("select_media", e)
        db.rollback()
        context = {"request": request}
        context["ERR"] = str(e)
        update_context_with_keywords(context)
        return templates.TemplateResponse("keyword.html", context)    
    
    except Exception as e:
        ic("select_media", e)
        context = {"request": request}
        context["ERR"] = str(e)
        update_context_with_keywords(context)
        return templates.TemplateResponse("keyword.html", context)
    
@keyword_router.post("/media2")
async def select_media(request: Request, search_type: str = Form(...), code: str = Form(...), db: Session = Depends(get_db)):
    try:
        resKeyword = await CKeyword(db).select_bycode(code)
        resMedia = await CMedia(db).selectCode(code)
        
        image_path = (config["G_PATH_SBIMG"] + 
                    resMedia.Folder + "/" + 
                    resMedia.Code + resMedia.Hash + "_y1.jpg") if resMedia else ""
                
        if resKeyword:
            ckeywords.set_keyword("keywords2", code, 
                                  string_to_list(resKeyword.Contents, True),
                                  string_to_list(resKeyword.keycode, True),
                                  string_to_list(resKeyword.kw_etc, True),
                                  image_path)
            
            context = {"request": request}
            update_context_with_keywords(context)
                
            return templates.TemplateResponse("keyword.html", context)
        else:
            context = {"request": request}
            context["ERR"] = "Failed to find keyword content"
            context["keywords1"] = ckeywords.get_keywords()["keywords1"]
            context["keywords2"] = ckeywords.init_keyword("keywords2")
            return templates.TemplateResponse("keyword.html", context)
    
    except SQLAlchemyError as e:
        ic(f"select_media{str(e)}")
        db.rollback()
        context = {"request": request}
        context["ERR"] = str(e)
        update_context_with_keywords(context)
        return templates.TemplateResponse("keyword.html", context)    
    
    except Exception as e:
        ic(f"select_media{str(e)}")
        context = {"request": request}
        context["ERR"] = str(e)
        update_context_with_keywords(context)
        return templates.TemplateResponse("keyword.html", context)


@keyword_router.post("/copy")
async def copy_keyword(request: Request, code1: str = Form(...), code2: str = Form(...), sql: Session = Depends(get_db), lite: AsyncSession = Depends(get_async_session)):
    context = {"request": request}
    try:
        if code1 == code2:
            raise ValueError("Source and destination codes must be different.")
        
        keyword = CKeyword(sql)
        src = await keyword.select_bycode(code1)
        dst = await keyword.select_bycode(code2)
        
        if await Clogs(lite).insert(src=src.to_dict(), dest=dst.to_dict()) == True:
            await lite.commit()
        else:
            await lite.rollback()
            raise ValueError("Failed to insert log")
            
        if await CKeyword(sql).update(dst.Code, src) == True:
            await sql.commit()
        else:
            await sql.rollback()
            raise ValueError("Failed to update keyword")
        
        resMedia = await CMedia(sql).selectCode(code2)
        
        image_path = (config["G_PATH_SBIMG"] + 
                        resMedia.Folder + "/" + 
                        resMedia.Code + resMedia.Hash + "_y1.jpg") if resMedia else ""
        
        ckeywords.set_keyword("keywords2", code2, 
                                string_to_list(dst.Contents, True),
                                string_to_list(dst.keycode, True),
                                string_to_list(dst.kw_etc, True),
                                image_path)
                    
        context = {"request": request}
        update_context_with_keywords(context)
        
        return templates.TemplateResponse("keyword.html", context)
    
    except (SQLAlchemyError, ValueError, LookupError) as e:
        ic(f"copy_keyword {str(e)}")
        sql.rollback()
        lite.rollback()
        context = {"request": request}
        context["ERR"] = str(e)
        update_context_with_keywords(context)
        return templates.TemplateResponse("keyword.html", context)    
    
    except Exception as e:
        ic(f"copy_keyword {str(e)}")
        context = {"request": request}
        context["ERR"] = str(e)
        update_context_with_keywords(context)
        return templates.TemplateResponse("keyword.html", context)
    
@keyword_router.post("/logs")
async def get_log1(request: Request, date: str = Form(...), session: AsyncSession = Depends(get_lite_db)):
    try:
        result = await Clogs(session).select(date)
        context = {"request": request}
        context["logs"] = result
        
        return templates.TemplateResponse("logs.html", context)
    
    except Exception as e:
        ic(f"logs1: {str(e)}")
        context = {"request": request}
        context["ERR"] = str(e)
        return templates.TemplateResponse("logs.html", context)
    
@keyword_router.get("/logs")
async def get_log2(request: Request, session: AsyncSession = Depends(get_lite_db)):
    try:
        result = await Clogs(session).select(datetime.now(CONST_TIMEZONE_KST), 5)
        context = {"request": request}
        context["logs"] = result
        
        return templates.TemplateResponse("logs.html", context)
    
    except Exception as e:
        ic(f"logs2: {str(e)}")
        context = {"request": request}
        context["ERR"] = str(e)
        return templates.TemplateResponse("logs.html", context)

@keyword_router.get("/")
async def index(request: Request):
    ckeywords.init_keywords()
    context = {"request": request}
        
    return templates.TemplateResponse("keyword.html", context)

def update_context_with_keywords(context):
    context["keywords1"] = ckeywords.get_keywords()["keywords1"]
    context["keywords2"] = ckeywords.get_keywords()["keywords2"]
    