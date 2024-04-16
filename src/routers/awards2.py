from fastapi import APIRouter, Depends, Request
from fastapi.templating import Jinja2Templates
from sqlalchemy.orm import Session
from src.core.sql_db import get_db
from src.classes.keyword import Keywords
from src.controllers.festivalAwardTH import CtrlFestivalAwards_TH as ctrl_awards_th

awards2_router = APIRouter()
templates = Jinja2Templates(directory="templates")
ckeywords = Keywords()

@awards2_router.get("/")
def index(request: Request, db: Session = Depends(get_db)):
    ckeywords.init_keywords()

    awards_th = ctrl_awards_th(db)
    res_list = awards_th.selectAwardsTHList_top30()

    context = {"request": request, "awards": res_list}

    return templates.TemplateResponse("awards2.html", context)
