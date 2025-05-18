import logging

from fastapi import APIRouter, Request
import json

from utils.config import config
from utils.redis import rdb


router = APIRouter()


@router.get('/healthcheck', responses={200: {'content': {'application/json': {'example': 'OK'}}}})
async def healthcheck():
    return 'OK'

@router.get('/api/user')
async def telegram_webhook(request: Request, user_id: int) -> None:
    logging.debug(user_id)
    return 
    ...
