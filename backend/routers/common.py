import logging
from typing import Annotated

from fastapi import APIRouter, Request, Depends
import json

from dependencies import SessionDep, UserDep
from utils.config import config
from utils.db.models import UserModel
from utils.redis import rdb


router = APIRouter()


@router.get('/healthcheck', responses={200: {'content': {'application/json': {'example': 'OK'}}}})
async def healthcheck():
    return 'OK'

@router.get('/api/user')
async def telegram_webhook(request: Request, user: UserDep) -> str:
    logging.debug((user.username, request.state.user_data.get('first_name')))
    return 'Test'
