from pydantic_settings import BaseSettings
class Settings(BaseSettings):
    db_hostname:str
    db_port:str
    db_password:str
    db_name:str
    db_username:str
    secret_key:str
    algorithm:str
    access_token:int
    

    model_config = {
    "env_file": r"C:\NEPSE.analysis\.venv\app\.env",
    "extra": "ignore"}
    
    
settings=Settings()


