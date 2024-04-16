from fastapi import APIRouter, Depends, Request
from fastapi.templating import Jinja2Templates
from sqlalchemy.orm import Session
from src.core.sql_db import get_db
from src.controllers.festivalAwardTH import CtrlFestivalAwards_TH as ctrl_awards_th

awards1_router = APIRouter()
templates = Jinja2Templates(directory="templates")

@awards1_router.get("/")
def index(request: Request, db: Session = Depends(get_db)):

    awards_th = ctrl_awards_th(db)
    res_list = awards_th.selectAwardsTHList_top30()

    context = {"request": request, "awards": res_list}

    return templates.TemplateResponse("awards1.html", context)

