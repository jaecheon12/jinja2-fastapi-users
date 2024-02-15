
from typing import Union

from fastapi import FastAPI , APIRouter, Request, Form
from fastapi.responses import HTMLResponse
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles 
from fastapi.templating import Jinja2Templates
from src.routers.user import user_router  # Updated import
from src.routers.keyword import keyword_router  # Updated import
from src.routers.model import model_router  # Updated import
from src.static.config import config

from src.models.lite_db import create_db_and_tables

app = FastAPI()

templates = Jinja2Templates(directory="templates")
app.mount("/static", StaticFiles(directory="static"), name="static")

app.add_middleware(
    CORSMiddleware,
    allow_origins=config["FASTAPI_ALLOW_ORIGINS"], 
    allow_credentials=True,
    allow_methods=["*"],  # Allows all methods
    allow_headers=["*"],  # Allows all headers
)

app.include_router(
    user_router,
    prefix="/user",
    tags=["user"],
)

app.include_router(
    keyword_router,
    prefix="/keyword",
    tags=["keyword"],
)

app.include_router(
    model_router,
    prefix="/model",
    tags=["model"],
)

@app.get("/", response_class=HTMLResponse)
async def read_root(request: Request):
    return templates.TemplateResponse("main.html", {"request": request})

@app.on_event("startup")
async def on_startup():
    await create_db_and_tables()
