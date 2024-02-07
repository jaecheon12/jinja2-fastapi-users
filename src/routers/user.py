from fastapi import APIRouter, Depends, Request, HTTPException
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates


user_router = APIRouter()

templates = Jinja2Templates(directory="templates")

# print("templates", templates, templates.__dict__, templates.env.__dict__)

@user_router.get("/", response_class=HTMLResponse)
async def read_root(request: Request):
    return templates.TemplateResponse("main.html", {"request": request})

@user_router.get("/signin", response_class=HTMLResponse)
async def read_signin(request: Request):
    return templates.TemplateResponse("signin.html", {"request": request})

@user_router.get("/signup", response_class=HTMLResponse)
async def read_signup(request: Request):
    return templates.TemplateResponse("signup.html", {"request": request})

@user_router.get("/keyword", response_class=HTMLResponse)
async def read_keyword(request: Request):
    return templates.TemplateResponse("keyword.html", {"request": request})
