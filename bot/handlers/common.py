from aiogram import Router
from aiogram.types import Message
from aiogram.filters import Command

router = Router()


@router.message(Command(commands=['start']))
async def _(message: Message):
    await message.answer('<b>Test</b>')
