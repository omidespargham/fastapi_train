from fastapi import FastAPI
from routers.user import user
from routers.person import person
# models.Base.metadata.create_all(bind=engine)

app = FastAPI()
app.include_router(user.router)
app.include_router(person.router)








