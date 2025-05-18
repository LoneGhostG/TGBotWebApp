import logging

from fastapi import Request, HTTPException
from starlette.middleware.base import BaseHTTPMiddleware
import hmac
import hashlib

from utils.config import config


class AuthMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request: Request, call_next):
        auth = request.headers.get('authorization').split('\n')
        
        
        
        logging.debug(auth)
        token = config.bot_token.get_secret_value()
        key = hmac.new(bytes(token), b'WebAppData', hashlib.sha256)
        
        if False:
            raise HTTPException(status_code=401, detail='Bad initData') 
        return await call_next(request)
