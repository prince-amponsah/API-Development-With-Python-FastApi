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
from ..database import engine, SessionLocal, get_db
from sqlalchemy.orm import session
from .. import schemas, oauth2, utils
from .. import utils
from . import users



router = APIRouter(
    prefix="/posts",
    tags=['Post']
)
#List all posts
@router.get('/', response_model=List[schemas.PostResponse])
def get_posts(db: session = Depends(get_db), current_user: int =  Depends(oauth2.get_current_user), 
              limit: int = 10, skip: int = 0, search: Optional[str] = ""):
    print(limit)
    post = db.query(models.Post).filter(models.Post.title.contains(search)).limit(limit).offset(2).all()
    return post


#Create new posts
@router.post('/', status_code=status.HTTP_201_CREATED, response_model=schemas.PostResponse)
def create_post(post: schemas.PostCreate, db: session = Depends(get_db),current_user: int =  Depends(oauth2.get_current_user)):
    # print(current_user)
    new_post = models.Post(owner_id=current_user.id,**post.dict())
    db.add(new_post)
    db.commit()
    db.refresh(new_post)
    return new_post


#Get Post By id Implementation
@router.get('/{id}', response_model=schemas.PostResponse)
def get_posts(id: int, db: session = (Depends(get_db)), current_user: int =  Depends(oauth2.get_current_user)):

    post = db.query(models.Post).filter(models.Post.id == id).first()
    # print(post)
    # if post:
    #     return {"Data": post}
    # else:
    #     return {"Message": f"Your id: {id} NOT in our database!"}
    return post

#Implementation For Deleting Posts.
@router.delete('/{id}', response_model=schemas.PostResponse)
def delete_post(id: int, db: session = Depends(get_db)):
    post = db.query(models.Post).filter(models.Post.id == id)
    post_query = post.first()
    if post.first() ==  None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)

    if post.owner_id != oauth2.get_current_user.id:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, 
                            detail=f"Not authorised to delete from another user!")
    post_query.delete(synchronize_session=False)
    db.commit()
    return {"Message": f"Post with Id:{id} Deleted Successfully!"}


@router.put('/{id}', response_model=schemas.PostResponse)
def update_post(id: int, updated_post: schemas.PostBase, db: session = Depends(get_db)):      
    post_query = db.query(models.Post).filter(models.Post.id == id)
    post = post_query.first()
    if post_query == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                             details=f"Your id:{post_query} Doesn't Exist!")
    else:
        post_query.update(updated_post.dict(), synchronize_session=False)
        db.commit()
        return post_query.first()
    
