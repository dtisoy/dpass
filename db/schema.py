from sqlalchemy import Column, Integer, String, ForeignKey
from base import Base

class Website(Base):
    __tablename__ = "website"
    id = Column(Integer, primary_key=True)
    name = Column(String)

class Account(Base):
    __tablename__ = "account"
    id = Column(Integer, primary_key=True)
    username = Column(String)
    website = Column(Integer, ForeignKey("website.id"))

