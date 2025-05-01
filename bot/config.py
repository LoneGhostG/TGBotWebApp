from aiogram import Bot, Dispatcher
from aiogram.client.default import DefaultBotProperties
from aiogram.client.session.aiohttp import AiohttpSession
from aiogram.fsm.storage.redis import RedisStorage

from utils.config import config


session = AiohttpSession()

bot = Bot(
    token=config.bot_token.get_secret_value(),
    session=session,
    default=DefaultBotProperties(
        parse_mode='HTML'
    )
)

storage = RedisStorage.from_url(
    url=f'redis://:{config.redis_password.get_secret_value()}@{config.redis_host}:{config.redis_port}/0'
)

dp = Dispatcher(
    storage=storage
)
