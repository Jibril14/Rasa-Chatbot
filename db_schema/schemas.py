from pydantic import BaseModel
import datetime

class LaptopBase(BaseModel):
    name: str
    description: str
    image: str
    price: float


class LaptopDisplay(BaseModel):
    name: str
    description: str
    image: str
    price: float
    class Config():
        orm_mode = True


class ChatBase(BaseModel):
    # chatId : int
    date: str # datetime.datetime
    conversation: str

class ChatDisplay(BaseModel):
    # chatId : int
    date: str
    conversation: str
    class Config():
        orm_mode = True