from fastapi import APIRouter
from . import user_post,user_get
router = APIRouter(prefix="/user",tags=["user"])

router.include_router(user_get.router)
router.include_router(user_post.router)
