import logging
from typing import AsyncGenerator

from dishka import make_async_container, Provider, Scope, provide, from_context
from dishka.integrations.fastapi import FastapiProvider
from fastapi import Request
from sqlalchemy.ext.asyncio import AsyncSession

from utils.db.models import UserModel
from utils.db.session import async_session
from utils.db.utils import get_user


class DatabaseProvider(Provider):
    scope = Scope.REQUEST
    
    @provide
    async def provide_db_session(self) -> AsyncGenerator[AsyncSession, None]:
        logging.debug('Dishka: Создана сессия базы данных')
        async with async_session() as session:
            yield session

class UserProvider(Provider):
    scope = Scope.REQUEST
    
    request = from_context(provides=Request, scope=Scope.REQUEST)
    
    @provide
    async def provide_user(self, session: AsyncSession, request: Request) -> UserModel:
        return UserModel()
        # logging.debug(f'Dishka: Пользователь {event.from_user.id} найден')
        # return await get_user(session, event.from_user.id)


container = make_async_container(DatabaseProvider(), UserProvider(), FastapiProvider())

__all__ = ('container', )
