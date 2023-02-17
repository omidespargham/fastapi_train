from fastapi import APIRouter
from . import person_get,person_post

router = APIRouter(prefix="/person")

router.include_router(person_post.router)
router.include_router(person_get.router)


