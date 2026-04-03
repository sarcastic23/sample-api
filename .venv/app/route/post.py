from fastapi import Depends,APIRouter,HTTPException,status
from app import models,jwttoken
from app.database import Item
from sqlalchemy.orm import Session
from app.database import get_db



import psycopg2 #when using raw sql
from psycopg2.extras import RealDictCursor#raw sql
 
router=APIRouter()
error=HTTPException(status_code=status.HTTP_401_UNAUTHORIZED)

@router.get("/sql",response_model=list[Item])
async def sql(db:Session=Depends(get_db),user_data=Depends(jwttoken.current_users)):
    
    row=db.query(models.post).filter(models.post.owner_id == user_data.id).all()
    
    return row

@router.get("/name/{id}")
async def pay(id:int,db:Session=Depends(get_db),user_data=Depends(jwttoken.current_users)):
    row=db.query(models.post).filter(models.post.id==id).first()
    if row==None:
        return{"no such id"}
    else:
        if row.owner_id==user_data.id:
         return row
        else:
            return error
    

 
@router.post("/post")
async def posts(item:Item,db:Session=Depends(get_db),user_data=Depends(jwttoken.current_users)):
   
        new_post=models.post(owner_id=user_data.id,**item.dict()  )
        db.add(new_post)
        db.commit()
        db.refresh(new_post)
        return new_post   

        
        
@router.delete("/posts/{id}")
async def delete_post(id:int,db:Session=Depends(get_db),user_data:int=Depends(jwttoken.current_users)):
 row=db.query(models.post).filter(models.post.id==id)
 rox:models.post=row.first()
 if rox==None:
     return{"no such posts to delete"}
 else:
     if rox.owner_id==user_data.id :
        row.delete(synchronize_session=False)
        db.commit()
        return {f"ok, post deleted by :{user_data.id}"}
     else:
         error
 
@router.put("/post/{id}")
async def update_post(id:int,item: Item,db:Session=Depends(get_db),user_id:int=Depends(jwttoken.current_users)):
    
    row=db.query(models.post).filter(models.post.id==id)
    rox=row.first()
    if rox==None:
        return{"id doesnt exist"}
    else:
        if rox.owner_id==user_id.id:
            row.update(item.dict(),synchronize_session=False)   
            db.commit()
       
            return rox
        else:
            return error
