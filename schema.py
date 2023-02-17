from pydantic import BaseModel
from models import Post
from typing import Optional
from fastapi import Body

# User schema

class UserBase(BaseModel):
    email: str
    username: str


class UserCreate(UserBase):
    password: str = Body(Ellipsis,
                         min_length=8)


class UserShow(UserBase):
    id: Optional[int]
    # posts: list[Post] = []

    class Config:
        orm_mode = True # if i send you obj of my db, schema can tern it to json data
                          # if it is True. without schema db obj will return auto to json.
                          # be carefull schema objects can return to json automatically
                          # this orm_mode just use when we want to give db obj to schema class
                          # for make it as json

################################

# Post schema

class PostCreate(BaseModel):
    title:str
    description:str

class PostShow(PostCreate):
    id:int

    class Config:
        orm_mode = True



