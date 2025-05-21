import logging
import asyncio

import aiohttp
from dishka.integrations.aiogram import setup_dishka
from aiogram.types import Update
import json

from middlewares import ErrorMiddleware
from handlers import router
from dependencies.dishka import container
from config import bot, dp
from utils.config import config
from utils.redis import rdb
from utils.db.session import engine
from utils.db.models import Base


logging.basicConfig(level=logging.DEBUG)
logging.getLogger('aiogram').setLevel(logging.WARNING)


dp.update.middleware(ErrorMiddleware())

dp.include_router(router)

setup_dishka(container, router, auto_inject=True)


async def start_bot():
    async def bot_polling():
        logging.info("Bot started with polling")
        await bot.delete_webhook()
        await dp.start_polling(bot)
    
    async def bot_webhook():
        logging.info("Bot started with webhook")
        await bot.set_webhook(
            url=f'{config.webhook_url}/telegram',
            secret_token=config.webhook_secret.get_secret_value(),
            allowed_updates=dp.resolve_used_update_types(),
            drop_pending_updates=True
        )
        
        pubsub = rdb.pubsub()
        await pubsub.subscribe('telegram_updates')
        
        try:
            await dp.emit_startup()
            async for message in pubsub.listen():
                if message['type'] == 'message':
                    try:
                        update = Update.model_validate(
                            json.loads(message['data'].decode()),
                            context={'bot': bot}
                        )
                        await dp.feed_update(bot, update)
                    except Exception as e:
                        logging.error(e)
                else:
                    logging.debug(message['type'])
        finally:
            await bot.delete_webhook()
            await dp.emit_shutdown()
    
    webhook_health = bool(config.webhook_url)
    if webhook_health:
        async with aiohttp.ClientSession() as session:
            try:
                async with session.get(f'{config.webhook_url}/healthcheck') as response:
                    logging.debug(await response.json())
                    webhook_health = await response.json() == 'OK'
            except Exception as e:
                logging.error(e)
                webhook_health = False
    
    if webhook_health:
        return await bot_webhook()
    return await bot_polling()


async def main():
    ###########
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)
        await conn.run_sync(Base.metadata.create_all)
    ###########
    
    await start_bot()


if __name__ == '__main__':
    asyncio.run(main())
