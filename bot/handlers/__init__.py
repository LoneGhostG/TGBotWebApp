from aiogram import Router, Dispatcher

from . import common


router = Router()

router.include_routers(
    common.router,
)

__all__ = ('router')
