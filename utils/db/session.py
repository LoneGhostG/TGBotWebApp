from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker

from utils.config import config 


engine = create_async_engine(
    url=config.DatabaseDSN,
    echo=False
)

async_session = async_sessionmaker(
    bind=engine, 
    expire_on_commit=False
)


__all__ = ('engine', 'async_session')
