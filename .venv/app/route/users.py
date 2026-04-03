
from fastapi import Depends,APIRouter
from app import models
from app.database import Item_S
from sqlalchemy.orm import Session
from app.database import get_db
from app.database import user_out
from argon2 import PasswordHasher




router=APIRouter()
ph = PasswordHasher()

def verify(p1:str,p2:str):
    hashed=ph.verify(p1,p2)
    return hashed

def hasher(password: str):
    hashed=ph.hash(password)
    return hashed
 




@router.get("/users")
async def get_users(db:Session=Depends(get_db)):
    row=db.query(models.Users).all()
    return row

@router.get("/users/{id}",response_model=user_out)
async def get_users(id: int,db:Session=Depends(get_db)):
    row=db.query(models.Users).filter(models.Users.id==id).first()
    if row== None:
        return {"nth to say"}
    else:
        return row
    
    

    
@router.post("/users",response_model=user_out)
async def post_user( item:Item_S,db:Session=Depends(get_db)):
    
    item.password=hasher(item.password)
    
    row=models.Users(**item.dict())
    
    db.add(row)
    db.commit()
    db.refresh(row)
    return row
    

        
    
    
       






















