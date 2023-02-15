from fastapi import FastAPI
from typing import Optional
from pydantic import BaseModel


app = FastAPI()

class Person(BaseModel):
    name: str
    password: str
    email: Optional[str]
    # three: str

class PersonOut(BaseModel):
    name: str
    email: Optional[str]

@app.get("/")
def root():
    return {"hello":"world"}

@app.get("/the_name/{name}")
def the_name(name: str,num:int=None): # Optional is query params
    return {"hello":name,"number":num}

# @app.post("/person/")
# def person(two,three,one):
#     return {"one":one,"two":two,"three":three}

@app.get("/person/",response_model=PersonOut)
def person(person:Person):
    return person


