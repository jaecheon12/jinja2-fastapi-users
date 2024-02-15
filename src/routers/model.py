
from fastapi import APIRouter, Depends, Request, Form
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from sqlalchemy.orm import Session
from sqlalchemy.exc import SQLAlchemyError
from src.models.sql_db import get_db
from src.controllers.maker import CtrlMaker
from src.controllers.model import CtrlModel
from src.controllers.media import CtrlMedia
from icecream import ic
from datetime import datetime

model_router = APIRouter()
templates = Jinja2Templates(directory="templates")

@model_router.post("/", response_class=HTMLResponse)
async def select_model(request: Request, code: str = Form(...), sqldb: Session = Depends(get_db)):
    try:
        
        res_makers = await CtrlMaker(sqldb).select_all(code)
        res_media = await CtrlMedia(sqldb).selectCode(code)
        ctrl_model = CtrlModel(sqldb)
        
        if not res_makers:
            raise Exception("No maker found")
        
        if not res_media:
            raise Exception("No media found")
        
        media = res_media.to_dict()
        
        models = []
        for maker in res_makers:
            if maker.MakerId:
                if maker.MakerId[0:4] == 'M000':
                    res_model = await ctrl_model.get_bycode(maker.MakerId)
                    if res_model:
                        model = res_model.to_dict()
                        if model.get("Birth"):
                            if len(model.get("Birth")) == 10:
                                birth_date = datetime.strptime(model.get("Birth"), '%Y-%m-%d').date()
                                today = datetime.today().date()
                                model["Age"] = today.year - birth_date.year - ((today.month, today.day) < (birth_date.month, birth_date.day))
                            
                        models.append(model)
        
        context = {"request": request}
        context["models"] = models
        context["media"] = media
        
        return templates.TemplateResponse("model.html", context)
    
    except SQLAlchemyError as e:
        ic(f"select_model{e}")
        sqldb.rollback()
        context = {"request": request}
        context["ERR"] = str(e)
        return templates.TemplateResponse("model.html", context)
    
    except Exception as e:
        ic(f"select_model{e}")
        context = {"request": request}
        context["ERR"] = str(e)
        return templates.TemplateResponse("model.html", context)


@model_router.get("/", response_class=HTMLResponse)
async def read_root(request: Request):
    return templates.TemplateResponse("model.html", {"request": request})
