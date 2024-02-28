import os
import fastapi
from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates


router = fastapi.APIRouter()
template = Jinja2Templates(directory="app/templates")


@router.get("/", response_class=HTMLResponse)
async def index(request: Request):
    return template.TemplateResponse("pages/base.html", {"request": request})


@router.get("/test", response_class=HTMLResponse)
async def index(request: Request):
    return template.TemplateResponse("pages/test.html", {"request": request})


@router.get("/about", response_class=HTMLResponse)
async def index(request: Request):
    return template.TemplateResponse("pages/about.html", {"request": request})
