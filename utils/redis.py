from redis.asyncio import Redis

from utils.config import config


rdb = Redis(host=config.redis_host, port=config.redis_port, password=config.redis_password.get_secret_value())


__all__ = ('rdb', )
