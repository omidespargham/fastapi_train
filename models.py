from database import Base
from sqlalchemy import Column,String,Integer

class User(Base):
    __tablename__ = "users"

    id = Column(Integer,primary_key=True,index=True)
    email = Column(String,unique=True)
    username = Column(String)
    password = Column(String)


class Post(Base):
    __tablename__ = "posts"

    id = Column(Integer,primary_key=True,index=True)
    title = Column(String)
    description = Column(String)
    
