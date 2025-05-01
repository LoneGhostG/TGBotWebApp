from fastapi import APIRouter

from . import common

router = APIRouter()

router.include_router(
    common.router
)

__all__ = ('router')
