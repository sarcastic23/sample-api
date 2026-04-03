
from sqlalchemy.orm import relationship
from sqlalchemy import  ForeignKey, Integer,Column,String
from .database import Base

class post(Base):
    __tablename__="posts"
    id=Column(Integer,primary_key=True,nullable=True)
    name=Column(String,nullable=False)
    age=Column(Integer,nullable=False)
    tax=Column(Integer,server_default=None)
    owner_id=Column(Integer,ForeignKey("users.id",ondelete="CASCADE"),nullable=False)
   

    
class Users(Base):
    __tablename__="users"
    
    id=Column(Integer,primary_key=True,nullable=True)
    username=Column(String,nullable=False)
    password=Column(String,nullable=False)