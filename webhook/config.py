from typing import AsyncGenerator

from fastapi import FastAPI


# async def lifespan(app: FastAPI) -> AsyncGenerator:
#     await bot.set_webhook(
#         url=config.webhook_url,
#         allowed_updates=dp.resolve_used_update_types(),
#         drop_pending_updates=True
#     )
    
#     yield
    
#     await bot.session.close()


app = FastAPI(
    # lifespan=lifespan
)
