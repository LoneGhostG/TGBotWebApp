from fastapi import APIRouter, Request
import json

from utils.redis import rdb


router = APIRouter()


@router.get('/healthcheck')
async def healthcheck():
    return 'OK'

@router.post('/webhook/telegram')
async def telegram_webhook(request: Request) -> None:
    data = await request.json()
    await rdb.publish('test', json.dumps(data))

@router.get('/')
async def _(request: Request):
    return 'Test'
