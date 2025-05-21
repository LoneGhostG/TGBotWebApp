import logging
from typing import Annotated, AsyncGenerator

from fastapi import Request, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from utils.db.models import UserModel
from utils.db.session import async_session
from utils.db.utils import get_user


async def provide_db_session() -> AsyncGenerator[AsyncSession, None]:
    logging.debug('Dependencies: Создана сессия базы данных')
    async with async_session() as session:
        yield session

SessionDep = Annotated[AsyncSession, Depends(provide_db_session)]


async def provide_user(request: Request, session: SessionDep) -> UserModel:
    logging.debug(f'Dependencies: Пользователь {request.state.user_data.get('id')} найден')
    return await get_user(session, request.state.user_data.get('id'))

UserDep = Annotated[UserModel, Depends(provide_user)]


__all__ = ('SessionDep', 'UserDep', )
