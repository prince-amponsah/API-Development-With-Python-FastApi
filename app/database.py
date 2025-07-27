from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import os
import psycopg2
from datetime import datetime
import time
from psycopg2.extras import RealDictCursor
from .config import settings

SQLALCHEMY_DATABASE_URL = f'postgresql://{settings.database_username}:{settings.database_password}@{settings.database_hostname}:{settings.database_port}/{settings.database_name}'

#SQLALCHEMY_DATABASE_URL = 'postgresql://{settings.database_username}:{settings.database_password}@{settings.database_hostnam}:{settings.database_port}/{settings.database_name}'


engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()




def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()



try:
        connection = psycopg2.connect(host='localhost', database='fastapi', 
                                      user='postgres', password='admin',cursor_factory=RealDictCursor)
        cursor = connection.cursor()
        print("Database Succeccfully Connected!")
        time.sleep(10)

except Exception as error:
        print("Connection Error With Database!")
        print("Error Was:", error)


#my_post = [{"title": "Learn Coding", "content": "Api Development With Python", "id":1},{ "Title": "AI Development", "Content": "Programming AI Models With Python", "id": 4}]


