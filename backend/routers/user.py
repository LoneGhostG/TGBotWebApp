import logging

from fastapi import APIRouter, Request

from dependencies import SessionDep, UserDep
from utils.config import config
from utils.db.models import UserModel
from utils.redis import rdb


router = APIRouter()


@router.get('/user')
async def _(request: Request, user: UserDep) -> str:
    logging.debug((user.username, request.state.user_data.get('first_name')))
    return request.state.user_data.get('username')
