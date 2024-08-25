from sqlalchemy.sql.sqltypes import Integer, String, Float
from sqlalchemy import Column
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class Laptop(Base):
    __tablename__= "laptops"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    description = Column(String, nullable=False)
    image = Column(String, nullable=False)
    price = Column(Float, nullable=False)


class Chat(Base):
    __tablename__= "chats"
    id = Column(Integer, primary_key=True, index=True)
    date = Column(String, nullable=False)
    conversation = Column(String, nullable=False)