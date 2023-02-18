from pydantic import BaseModel
from db.models import Post
from typing import Optional,List
from fastapi import Body

# User schema

class UserBase(BaseModel):
    email: str
    username: str


class UserCreate(UserBase):
    password: str = Body(Ellipsis,min_length=8)
    t: List[str]


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

##################################

# item schema
class ItemBase(BaseModel):
    title: str
    person_id:int
class ItemCreate(ItemBase):
    pass

class ItemShow(ItemBase):
    id:int
    # person: 

    class Config:
        orm_mode = True

#############################

# person schema

class PersonBase(BaseModel):
    name:str

class PersonCreate(PersonBase):
    pass

class PersonShow(PersonBase):
    id:int
    items: List[ItemShow] = []

    class Config:
        orm_mode = True