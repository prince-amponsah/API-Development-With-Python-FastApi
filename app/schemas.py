from sqlalchemy import Column, Integer, String, Boolean
from pydantic import BaseModel, EmailStr
from .database import Base
from sqlalchemy.sql.sqltypes import TIMESTAMP
from datetime import datetime
from typing import Optional


class PostBase(BaseModel):
    title: str
    content: str
    published: bool = True

class PostCreate(PostBase):
    pass

class Post(BaseModel):
    title : str
    content: str
    published: bool = True



class UserCreate(BaseModel):
    email: EmailStr
    password: str

class UserResponse(BaseModel): #UserOut
    id: int
    email: EmailStr
    created_at: datetime
    class config:
        orm_mode = True

class PostResponse(PostBase):
    id: int 
    created_at: datetime
    owner_id: int
    owner: UserResponse
    class config:
        orm_mode = True


        
class UserLogin(BaseModel):
    email: EmailStr
    password: str


class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    id: Optional[int] = None