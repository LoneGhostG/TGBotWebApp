import logging

from aiogram import Router, F
from aiogram.types import Message
from aiogram.filters import Command
from sqlalchemy.ext.asyncio import AsyncSession
from dishka.integrations.aiogram import FromDishka

from utils.db.models import UserModel
from utils.db.utils import get_user


router = Router()


@router.message(Command(commands=['start']))
async def _(
    message: Message, 
    session: FromDishka[AsyncSession], 
    user: FromDishka[UserModel]
):
    logging.debug('Start handler')
    # user = await get_user(session, message.from_user.id)
    
    if not user:
        user = UserModel(
            id = message.from_user.id,
            username = message.from_user.username
        )
        session.add(user)
        await session.commit()
        
        await message.answer(f'New user {message.from_user.first_name}!')
    else:
        await message.answer(f'Hello {message.from_user.first_name}!')


@router.message(Command(commands=['name']))
async def _(
    message: Message, 
    user: FromDishka[UserModel]
):
    logging.debug('User handler')
    await message.answer(f'Your username {user.username}!')


@router.message(F.content_type == 'web_app_data')
async def _(
    message: Message
):
    logging.debug(message.web_app_data)


@router.message()
async def _(
    message: Message
):
    logging.debug('Echo handler')
    await message.answer(message.text)
