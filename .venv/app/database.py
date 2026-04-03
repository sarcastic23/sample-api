from typing import Optional
from pydantic import BaseModel,ConfigDict
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from app.config import settings


sql_database_url=f'postgresql://{settings.db_username}:{settings.db_password}@{settings.db_hostname}:{settings.db_port}/{settings.db_name}'
engine=create_engine(sql_database_url)
SessionLocal=sessionmaker(autocommit=False,autoflush=False,bind=engine)
Base=declarative_base()


class Item(BaseModel):
    id:int
    name:str
    age:int
    tax: Optional[float]=None
    
    
class Item_S(BaseModel):
    id:int
    username:str
    password:str
    
class user_out(BaseModel):
    username:str

    model_config = ConfigDict(from_attributes=True)
    

class Token_data(BaseModel):
    id:int
    
    
    
def get_db():
    db=SessionLocal()
    try:
        yield db
    finally:
        db.close()