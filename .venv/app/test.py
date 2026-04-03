from app import jwttoken
from fastapi import Depends
from sqlalchemy.orm import Session
from app.database import Item,get_db

    
def posts(user_data=Depends(jwttoken.current_users)):
    print(user_data)


    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
# @app.get("/post/{id}")
# async def get_post(id: int,db:Session=Depends(get_db)):
#     row=db.query(models.post).filter(models.post.id==id)
#     if row.first()==None:
#         return{"no id"}
#     else:
#         return row.first()
        


# while True:
#     try:
#         conn=psycopg2.connect(host='localhost',database='fastapi',user='postgres',password='1593',cursor_factory=RealDictCursor)
#         cursor=conn.cursor()
#         print("database connection sucessfull")
#         break
#     except Exception as error:
#         print("conn failed",error)    
#         time.sleep(2)
        
#   cursor.execute("SELECT *FROM description WHERE name = %s", (id,))
#    row = cursor.fetchone()
#    if row==None:
#        return{"given name is not listed"}
#    else:
#       return row

# cursor.execute("""INSERT INTO description(name,age,tax) VALUES(%s,%s,%s) RETURNING 
    #                * """,(item.name,item.age,item.tax))
    # new_post=cursor.fetchone()
    # conn.commit()
    


