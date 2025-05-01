import asyncio

from aiogram.types import Update
import json

from handlers import router as bot_router
from config import bot, dp
from utils.config import config
from utils.redis import rdb


dp.include_router(bot_router)


pubsub = rdb.pubsub()


async def main(channel):
    await bot.set_webhook(
        url=f'{config.webhook_url}/webhook/telegram',
        allowed_updates=dp.resolve_used_update_types(),
        drop_pending_updates=True
    )
    
    await bot.send_message(5000937803, 'Bot Started!')
    
    await pubsub.subscribe(channel)
    
    async for message in pubsub.listen():
        if message['type'] == 'message':
            try:
                update = Update.model_validate(
                    json.loads(message['data'].decode()),
                    context={'bot': bot}
                )
                await dp.feed_update(bot, update)
            except: ...
        else:
            print(message['type'])
        

if __name__ == '__main__':
    asyncio.run(main('test'))
    # uvicorn.run(app, host=config.app_host, port=config.app_port)
