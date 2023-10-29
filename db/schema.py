from sqlalchemy import Column, Integer, String, ForeignKey
from base import Base

class Website(Base):
    __tablename__ = "website"
    id = Column(Integer, primary_key=True)
    name = Column(String)
    
    def __repr__(self):
        return(self.name)

class Account(Base):
    __tablename__ = "account"
    id = Column(Integer, primary_key=True)
    username = Column(String)
    password = Column(String)
    website = Column(Integer, ForeignKey("website.id"))
    def __repr__(self):
        return(self.username)

