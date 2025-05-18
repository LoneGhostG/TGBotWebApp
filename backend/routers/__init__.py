from fastapi import APIRouter
from dishka.integrations.fastapi import DishkaRoute

from . import common


router = APIRouter(route_class=DishkaRoute)

router.include_router(
    common.router
)

__all__ = ('router')
