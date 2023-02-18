from fastapi import APIRouter, Depends, HTTPException, Query,Body
from sqlalchemy.orm import Session
from db.database import SessionLocal, engine
import schema
import db.models as models
from db.database import get_db

router = APIRouter(prefix="",tags=["person"])

        
@router.post("/create_item",response_model=schema.ItemShow)
def create_item(item:schema.ItemCreate,db:Session=Depends(get_db)):
    person = db.query(models.Person).filter(models.Person.id == item.person_id).first()
    if not person:
        raise HTTPException(status_code=404,detail="person voojood nadarad !")
    item = models.Item(title=item.title,person_id=item.person_id)
    db.add(item)
    db.commit()
    db.refresh(item)
    return item

@router.post("/create_person",response_model=schema.PersonShow)
def create_person(person:schema.PersonCreate,db:Session=Depends(get_db)):
    obj = db.query(models.Person).filter(models.Person.name == person.name).first()
    if obj:
        raise HTTPException(status_code=404,detail="person exist with this name")
    person_db = models.Person(name=person.name)
    db.add(person_db)
    db.commit()
    db.refresh(person_db)
    return person_db


