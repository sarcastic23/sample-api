from app.route import users
from jose import JWTError,jwt
from datetime import datetime,timedelta
from fastapi import HTTPException,status,Depends
from app.database import Token_data,get_db
from fastapi.security import OAuth2PasswordBearer
from sqlalchemy.orm import Session
from app import models
from app.config import settings

oauth2_scheme=OAuth2PasswordBearer(tokenUrl="login")



secret_key=f"{settings.secret_key}"
ALGORITHM=f"{settings.algorithm}"
ACCESS_TOKEN_time=settings.access_token

def create_token(data: dict):
    encode=data.copy()
    expire=datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_time)
    encode.update({"exp":expire})
    jwt_encoded= jwt.encode(encode,secret_key,algorithm=ALGORITHM)#this requirea a data of exp time as well as userdata i.e(id or name), secret key and algo.
    
    return jwt_encoded

def verify_access_token(token: str,error):
    try:
        payload=jwt.decode(token,secret_key,algorithms=[ALGORITHM])
        user_id=payload.get("user_id")
        if user_id==None:
            raise error
        token_data=Token_data(id=int(user_id))
    except JWTError:
        raise error
    return token_data
    
def current_users(token:str=Depends(oauth2_scheme),db:Session=Depends(get_db)):
    error=HTTPException(status_code=status.HTTP_403_FORBIDDEN,detail=f"invalid",headers={"www-Authenticate":"Bearer"})
    user_token=verify_access_token(token,error)
    user=db.query(models.Users).filter(models.Users.id==user_token.id).first()
    if user==None:
        raise error
    return user