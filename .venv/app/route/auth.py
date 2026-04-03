from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database import get_db
from app import models, jwttoken
from app.route.users import verify
from fastapi.security.oauth2 import OAuth2PasswordRequestForm


router=APIRouter()

@router.post("/login")
def login_check(item:OAuth2PasswordRequestForm=Depends(),db:Session=Depends(get_db)):
    checked_row = db.query(models.Users).filter(
    models.Users.id == item.username).first()
   
    

    if checked_row ==None or  verify(checked_row.password,item.password)==False :
        return{"there is no user ,, sing up first"}
    else:
        
        access_token=jwttoken.create_token({"user_id":checked_row.id})
        

        return {
            "access_token": access_token,
            "token_type": "bearer"
        }
        
    
    
    

