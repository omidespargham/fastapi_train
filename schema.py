from pydantic import BaseModel
from models import Post

# User schema

class UserBase(BaseModel):
    email: str
    username: str


class UserCreate(UserBase):
    password: str


class UserShow(UserBase):
    id: int
    # posts: list[Post] = []

    class Config:
        orm_mode = True # if i send you obj of my db you tern if to json data

################################

# Post schema

class PostCreate(BaseModel):
    title:str
    description:str

class PostShow(PostCreate):
    id:int

    class Config:
        orm_mode = True



