from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from database import SessionLocal, engine
import schema
import models
import database

# models.Base.metadata.create_all(bind=engine)

app = FastAPI()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.post("/create_user/",response_model=schema.UserShow)
def create_user(user:schema.UserCreate,db:Session= Depends(get_db)):
    db_user = db.query(models.User).filter(models.User.email==user.email).first()
    if db_user:
        raise HTTPException(status_code=400,detail="emial already exist !")
    user = models.User(email=user.email,username=user.username,password=user.password)
    db.add(user)
    db.commit()
    db.refresh(user)
    return user

@app.get("/get_user/{user_id}/",response_model=schema.UserShow)
def show_user(user_id:int,db:Session=Depends(get_db)):
    user = db.query(models.User).filter(models.User.id == user_id).first()
    # user = db.query(models.User).get(models.User.id == user_id)
    if not user:
        raise HTTPException(status_code=400,detail="this user is not exist !")
    return user
