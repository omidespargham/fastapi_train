from db.database import Base
from sqlalchemy import Column, String, Integer, ForeignKey
from sqlalchemy.orm import relationship


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True, unique=True)
    email = Column(String, unique=True)
    username = Column(String)
    password = Column(String)

    # posts = relationship("Post",back_populates="user")


class Post(Base):
    __tablename__ = "posts"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String)
    description = Column(String)
    # user_id =  Column(Integer,ForeignKey("users.id"))
    # user = relationship("User",back_populates="posts")


class Person(Base):
    __tablename__ = "persons"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True)

    items = relationship("Item", back_populates="person")


class Item(Base):
    __tablename__ = "items"
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String)
    person_id = Column(Integer, ForeignKey("persons.id"))

    person = relationship("Person", back_populates="items")
    