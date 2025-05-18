from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from utils.db.models import UserModel


async def get_user(session: AsyncSession, id: int):
    user = await session.get(UserModel, id)
    return user
