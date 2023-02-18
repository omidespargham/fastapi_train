from fastapi import HTTPException
from sqlalchemy.orm import Session
import schema
import db.models as models


def create_person(db: Session, request: schema.PersonCreate):
    obj = db.query(models.Person).filter(
        models.Person.name == request.name).first()
    if obj:
        raise HTTPException(
            status_code=404, detail="person exist with this name")
    person_db = models.Person(name=request.name)
    db.add(person_db)
    db.commit()
    db.refresh(person_db)
    return person_db


def get_person(person_id, db: Session):
    person = db.query(models.Person).filter(
        models.Person.id == person_id).first()
    if not person:
        raise HTTPException(
            status_code=404, detail="person not exist with this id")
    return person