import logging

from fastapi.middleware.cors import CORSMiddleware
import uvicorn

from routers import router as app_router
from config import app
from utils.config import config


logging.basicConfig(level=logging.DEBUG)

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        '*',
        # "https://web.telegram.org",
    ],
    allow_credentials=True,
    allow_methods=['*'],
    allow_headers=['*'],
)

app.include_router(app_router)


if __name__ == '__main__':
    uvicorn.run(app, host=config.webhook_host, port=config.webhook_port)
