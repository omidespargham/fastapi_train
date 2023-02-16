from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from database import SessionLocal, engine
import schema
import models
import database
from routers.user import user
# models.Base.metadata.create_all(bind=engine)

app = FastAPI()
app.include_router(user.router)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()








