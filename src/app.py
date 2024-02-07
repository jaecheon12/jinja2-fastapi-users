
from typing import Union

from fastapi import FastAPI , APIRouter, Request, Form
from fastapi.responses import HTMLResponse
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles 
from src.routers.user import user_router  # Updated import
from src.routers.keyword import keyword_router  # Updated import
# from src.routers.auth import auth_router  # Updated import
# from src.routers.auth import bearer_transport

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allows all origins
    # allow_origins=allowed_origins,
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

# app.include_router(
#     auth_router,
#     prefix="/auth",
#     tags=["auth"],
# )


# @app.get("/", response_class=HTMLResponse)
# async def read_root(request: Request):
#     return templates.TemplateResponse("main.html", {"request": request})

# @app.get("/signin", response_class=HTMLResponse)
# async def read_signin(request: Request):
#     return templates.TemplateResponse("signin.html", {"request": request})

# @app.get("/signup", response_class=HTMLResponse)
# async def read_signup(request: Request):
#     return templates.TemplateResponse("signup.html", {"request": request})


# @app.get("/")
# def read_root():
#     return {"Hello": "World"}

