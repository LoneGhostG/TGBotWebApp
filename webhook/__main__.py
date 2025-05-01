from fastapi.middleware.cors import CORSMiddleware
import uvicorn

from routers import router as app_router
from config import app
from utils.config import config


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(app_router)


if __name__ == '__main__':
    uvicorn.run(app, host=config.app_host, port=config.app_port)
