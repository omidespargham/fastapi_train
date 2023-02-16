from database import Base
from sqlalchemy import Column,String,Integer,ForeignKey
from sqlalchemy.orm import relationship

class User(Base):
    __tablename__ = "users"

    id = Column(Integer,primary_key=True,index=True,unique=True)
    email = Column(String,unique=True)
    username = Column(String)
    password = Column(String)

    # posts = relationship("Post",back_populates="user")

class Post(Base):
    __tablename__ = "posts"

    id = Column(Integer,primary_key=True,index=True)
    title = Column(String)
    description = Column(String)
    # user_id =  Column(Integer,ForeignKey("users.id"))
    # user = relationship("User",back_populates="posts")
