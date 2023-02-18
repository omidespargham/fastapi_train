from fastapi import APIRouter,Depends, HTTPException
from sqlalchemy.orm import Session
from db.database import SessionLocal, engine
import schema
import db.models as models
from db.database import get_db


router = APIRouter(prefix="",tags=["user_get"])



@router.get("/get_user/{user_id}/",response_model=schema.UserShow)
def show_user(user_id:int,db:Session=Depends(get_db)):
    user = db.query(models.User).filter(models.User.id == user_id).first()
    # user = db.query(models.User).get(models.User.id == user_id)
    if not user:
        raise HTTPException(status_code=400,detail="this user is not exist !")
    return user
