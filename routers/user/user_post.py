from fastapi import APIRouter, Depends, HTTPException, Query,Body
from sqlalchemy.orm import Session
from database import SessionLocal, engine
import schema
import models
import database
# from two import get_db

router = APIRouter(prefix="", tags=["user_post"])


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.post("/create_post/", response_model=schema.PostShow, summary="Sakhte post !", description="in api baraye shoma post misazad", response_description="dar javab b shoma etelaate post ra br migardanad")
def create_post(post: schema.PostCreate, db: Session = Depends(get_db)):
    post = models.Post(title=post.title, description=post.description)
    db.add(post)
    db.commit()
    db.refresh(post)
    return post


@router.post("/create_user/", response_model=schema.UserShow, summary="sakhte user", description="is api baraye shoma post misazad")
def create_user(user: schema.UserCreate, db: Session = Depends(get_db)):
    db_user = db.query(models.User).filter(
        models.User.email == user.email).first()
    if db_user:
        raise HTTPException(status_code=400, detail="emial already exist !")
    user = models.User(
        email=user.email, username=user.username, password=user.password)
    db.add(user)
    db.commit()
    db.refresh(user)
    return user


@router.post("/test_user/", response_model=schema.UserShow)
def test_user(user: schema.UserCreate,
              name: str = Query(Ellipsis,
                                title="this is the title",
                                description="this is description",
                                alias="username",
                                deprecated=False),
              content: str = Body(Ellipsis, # required 
                                title="this is content")):
    return user
