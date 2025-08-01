from sqlalchemy import Column, Integer, String, Boolean, ForeignKey
from .database import Base
from pydantic import BaseModel
from sqlalchemy.sql.sqltypes import TIMESTAMP
from sqlalchemy.orm import relationship



class Post(Base):
    __tablename__ = "posts"

    id = Column(Integer, primary_key=True, nullable=False)
    title = Column(String, nullable=False)
    content = Column(String, nullable=False)
    published = Column(Boolean, server_default='True')
    created_at = Column(TIMESTAMP(timezone=True),
                         nullable=False, server_default=('now()'))
    owner_id = Column(Integer, ForeignKey("users.id",ondelete="CASCADE"))

    owner = relationship("User")


class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, nullable=False)
    email = Column(String, nullable=False, unique=True)
    password = Column(String, nullable=False)
    created_at = Column(TIMESTAMP(timezone=True), 
                        nullable=False, server_default=('now()'))





