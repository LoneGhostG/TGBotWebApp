import logging

from fastapi import APIRouter, Request
import ipaddress
import json

from utils.config import config
from utils.redis import rdb


telegram_ips = []

router = APIRouter()


@router.get('/healthcheck', responses={200: {'content': {'application/json': {'example': 'OK'}}}})
async def healthcheck():
    return 'OK'

@router.post('/telegram')
async def telegram_webhook(request: Request) -> None:
    # 149.154.160.0/20
    # 91.108.4.0/22
    data = await request.json()
    if request.headers.get('x-telegram-bot-api-secret-token') == config.webhook_secret.get_secret_value():
        await rdb.publish('telegram_updates', json.dumps(data, ensure_ascii=False))

@router.get('/', responses={200: {'content': {'application/json': {'example': 'Test'}}}})
async def _(request: Request):
    return 'Test'
