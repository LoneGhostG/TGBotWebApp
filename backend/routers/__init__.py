from fastapi import FastAPI, APIRouter

from . import common, user
from middlewares import AuthMiddleware


router = APIRouter()

router.include_router(common.router)
router.include_router(user.router)

__all__ = ('router', 'app')
