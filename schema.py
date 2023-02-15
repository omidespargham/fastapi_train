from pydantic import BaseModel


class UserBase(BaseModel):
    email: str
    username: str


class UserCreate(UserBase):
    password: str


class UserShow(UserBase):
    id: int

    class Config:
        orm_mode = True # if i send you obj of my db you tern if to json data
