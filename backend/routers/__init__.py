from fastapi import APIRouter

from . import common


router = APIRouter(prefix='/api')

router.include_router(
    common.router
)

__all__ = ('router')
