from sqlalchemy.orm.session import Session 
from  db_schema.schemas import LaptopBase, ChatBase
from db.models import Laptop, Chat


def create_laptop(db: Session, request: LaptopBase):
    new_laptop = Laptop(
        name = request.name,
        price = request.price,
        description = request.description,
        image = request.image
    )
    db.add(new_laptop)
    db.commit()
    db.refresh(new_laptop)
    return new_laptop


def get_all_laptops(db: Session):
    return db.query(Laptop).all()

def get_one_laptop(db: Session, search: int):
    return db.query(Laptop).filter(Laptop.id == search).first()


def get_match_laptops(db: Session, search: str):
    # return all laptop object that contains the search string
    return db.query(Laptop).filter(Laptop.description.ilike(f'%{search}%')).all()


def update_laptop(db: Session, id: int, request: LaptopBase):
    laptop = db.query(Laptop).filter(Laptop.id == id)
    laptop.update({
        Laptop.name: request.name,
        Laptop.description: request.description,
        Laptop.price: request.price
    })
    db.commit()
    return "ok"


def delete_laptop(db: Session, id: int):
    laptop = db.query(Laptop).filter(Laptop.id == id).first()
    db.delete(laptop)
    db.commit()
    return "ok"

def create_chat(db: Session, request: ChatBase):
    new_chat = Chat(
        date = request.date,
        conversation = request.conversation
    )
    db.add(new_chat)
    db.commit()
    db.refresh(new_chat)
    return new_chat

def get_all_chat(db: Session):
    return db.query(Chat).all()