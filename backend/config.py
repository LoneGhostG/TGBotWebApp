from typing import AsyncGenerator

from fastapi import FastAPI


async def lifespan(app: FastAPI) -> AsyncGenerator:
    yield
    await app.state.dishka_container.close()

app = FastAPI(
    lifespan=lifespan
)
