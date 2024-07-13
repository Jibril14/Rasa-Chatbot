import os
from typing import List
from fastapi import APIRouter, FastAPI, Request, Depends, Form
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from db_schema.schemas import LaptopBase, LaptopDisplay, ChatBase
from db.models import Laptop, Chat
from db.database import get_db, SessionLocal
from sqlalchemy.orm.session import Session 
from db import views
import requests
import datetime

router = APIRouter()
template = Jinja2Templates(directory="app/templates")



chatbot_user_dialog = []

def create_dialog():
    db : Session = SessionLocal()
    now = datetime.datetime.now()
    new_chat = Chat(
        date = str(now),
        conversation = str(chatbot_user_dialog)
    )
    db.add(new_chat)
    db.commit()
    db.refresh(new_chat)


# send chat from app to rasa server and get response
def rasa_response(message):       
    payload = {"message": message} #
    # http://localhost:5050/webhooks/rest/webhook for local dev
    req = requests.post("http://localhost:8000/webhooks/rest/webhook", json=payload)
    texts = [] # Bot may reply with list of strings
    for text in req.json():
      texts.append(text["text"])
    user_msg = message
    chatbot_msg = " ".join(texts)
    chatbot_user_dialog.append((user_msg, chatbot_msg))
    # check for slots in convo text, use this to query db for the laptop that have slot 
    check_slot(" ".join(texts))
    create_dialog()
    return " ".join(texts)


@router.get("/", response_class=HTMLResponse)
async def index(request: Request):
    return template.TemplateResponse("pages/base.html", {"request": request})

extra_list = []
# import json
@router.post("/message")
async def message(chat: ChatBase):
    msg = chat.dict()  # 1st turn request obj to dictionary
    print("MSG:",msg)
    return {
        "message": rasa_response(msg["conversation"]),
        "extra": extra_list 
        }

def check_slot(text):
    extra_list.clear()
    import re
    # Regular expression pattern to match a substring starting with ### and followed by word characters
    pattern = r'(\w+)###'
 
    match = re.search(pattern, text)
    if match:
        print("There is a match")
        db : Session = SessionLocal()
        laptops_slot = db.query(Laptop).filter(Laptop.description.ilike(f'%{match.group(1)}%')).all()
        for laptop in laptops_slot:
            extra_list.append(laptop)
    else:
        print("No match found")


@router.get("/about", response_class=HTMLResponse)
async def index(request: Request):
    return template.TemplateResponse("pages/about.html", {"request": request})


@router.post("/laptop/create", response_model=LaptopDisplay)
async def create_laptop(request: LaptopBase, db: Session = Depends(get_db)):
    return views.create_laptop(db, request)


@router.get("/all/laptops", response_model=List[LaptopDisplay])
async def get_laptops(db: Session = Depends(get_db)):
    return views.get_all_laptops(db)


@router.get("/laptop/{id}", response_model=LaptopDisplay)
async def get_one_laptop(idx: int, db: Session = Depends(get_db)):
    return views.get_one_laptop(db, idx)


@router.get("/all/{search_str}", response_model=List[LaptopDisplay])
async def get_match_laptops(search_str: str, db: Session = Depends(get_db)):
    return views.get_match_laptops(db, search_str)


@router.post("/laptop/update/{id}")
async def update_laptop(id: int, request: LaptopBase, db: Session = Depends(get_db)):
    return views.update_laptop(db, id, request)


@router.get("/laptop/delete/{id}")
async def delete_laptop(id: int, db: Session = Depends(get_db)):
    return views.delete_laptop(db, id)


@router.post("/chat/create")
async def create_chat(request: ChatBase, db: Session = Depends(get_db)):
    return views.create_chat(db, request)


@router.get("/all/chat")
async def get_chats(db: Session = Depends(get_db)):
    return views.get_all_chat(db)
