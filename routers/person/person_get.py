from fastapi import APIRouter, Depends, HTTPException, Query,Body
from sqlalchemy.orm import Session
from db.database import SessionLocal, engine
import schema
import db.models as models
from db.database import get_db


router = APIRouter(prefix="",tags=["person"])



@router.get("/get_person/{person_id}",response_model=schema.PersonShow)
def get_person(person_id:int,db:Session=Depends(get_db)):
    person = db.query(models.Person).filter(models.Person.id==person_id).first()
    if not person:
        raise HTTPException(status_code=404,detail="person not exist with this id")
    return person
    
@router.get("/get_item/{item_id}",response_model=schema.ItemShow)
def get_item(item_id:int,db:Session = Depends(get_db)):
    item = db.query(models.Item).filter(models.Item.id == item_id).first()
    if not item:
        raise HTTPException(status_code=404,detail="item not exist with this id")
    return item