from database.config_db import Base
from pydantic import BaseModel
from pydantic import EmailStr

class UserBase(BaseModel):
    email:EmailStr

class UserCreate(UserBase):
    fname : str
    lname : str
    password : str
    

