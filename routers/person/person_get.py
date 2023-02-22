from fastapi import APIRouter, Depends, HTTPException, Query,Body
from sqlalchemy.orm import Session
import schema
import db.models as models
from db.database import get_db
from typing import List
from db import person_db
from auth.oauth2 import oauth_scheme


router = APIRouter(prefix="",tags=["person"])



@router.get("/get_person/{person_id}",response_model=schema.PersonShow)
def get_person(person_id:int,db:Session=Depends(get_db),token:str=Depends(oauth_scheme)):
    return person_db.get_person(person_id,db)
    

@router.get("/get_item/{item_id}",response_model=schema.ItemShow)
def get_item(item_id:int,db:Session = Depends(get_db)):
    item = db.query(models.Item).filter(models.Item.id == item_id).first()
    if not item:
        raise HTTPException(status_code=404,detail="item not exist with this id")
    return item


@router.get("/get_items/{person_id}",response_model=List[schema.ItemShow])
def get_items(person_id:int,db:Session=Depends(get_db)):
    items = db.query(models.Item).filter(models.Item.person_id==person_id).all()
    return items

@router.get("/get_all_items",response_model=List[schema.ItemShow])
def get_items(db:Session=Depends(get_db)):
    items = db.query(models.Item).all()
    return items


@router.get("/delete_item/{item_id}")
def delete_item(item_id,db:Session=Depends(get_db)): # if we get item id str the query will work
    item = get_item(item_id,db)
    db.delete(item)
    db.commit()
    return "ok"

@router.post("/update_item")
def update_item(item_id,item:schema.ItemCreate,db:Session=Depends(get_db)):
    item_db = db.query(models.Item).filter(models.Item.id == item_id)
    item_db.update({
        models.Item.title:item.title,
        models.Item.person_id:item.person_id
    })
    db.commit()
    # db.refresh(item)
    return "ok"
    