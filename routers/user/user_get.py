from fastapi import APIRouter,Depends, HTTPException
from sqlalchemy.orm import Session
from database import SessionLocal, engine
import schema
import models
import database
# from two import get_db

router = APIRouter(prefix="",tags=["user_get"])


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/get_user/{user_id}/",response_model=schema.UserShow)
def show_user(user_id:int,db:Session=Depends(get_db)):
    user = db.query(models.User).filter(models.User.id == user_id).first()
    # user = db.query(models.User).get(models.User.id == user_id)
    if not user:
        raise HTTPException(status_code=400,detail="this user is not exist !")
    return user
