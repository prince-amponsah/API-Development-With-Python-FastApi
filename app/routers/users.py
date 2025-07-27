from fastapi import FastAPI, Response, status, HTTPException, Depends, APIRouter
from datetime import datetime
from fastapi.params import Body
from pydantic import BaseModel
from typing import Optional, List
from random import randrange
import psycopg2
from psycopg2.extras import RealDictCursor
import time
from .. import models
from ..database import SessionLocal, get_db
from sqlalchemy.orm import session
from .. import schemas
from .. import utils


router = APIRouter(
    prefix="/users",
    tags=['Users']
)

    # User Scripts Below:


@router.post('/', status_code=status.HTTP_201_CREATED,response_model=schemas.UserResponse)
def create_user(user: schemas.UserCreate, db: session = Depends(get_db)):

    hassed_pwd = utils.hashed_pwd(user.password)
    user.password = hassed_pwd
    new_user = models.User(**user.dict())
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user


#Get User By Id:
@router.get("/{id}", response_model=schemas.UserResponse)
def get_user(id: int,  db: session = Depends(get_db)):
    get_user = db.query(models.User).filter(models.User.id == id).first()
    if not get_user:
         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"user Id:{id} Not Found!")
    return get_user