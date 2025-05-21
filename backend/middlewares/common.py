import logging

from fastapi import Request, HTTPException
from starlette.middleware.base import BaseHTTPMiddleware
import json
from urllib.parse import parse_qsl
import hmac
import hashlib

from utils.config import config


class AuthMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request: Request, call_next):
        if not request.url.path.startswith("/user"):
            return await call_next(request)
        
        try:
            init_data = request.headers.get('initData')
            parsed_data = dict(parse_qsl(init_data))
            
            user_hash = parsed_data.pop('hash')
            
            data_check_string = '\n'.join(f'{key}={value}' for key, value in sorted(parsed_data.items()))
            
            token = config.bot_token.get_secret_value()
            secret_key = hmac.new(b"WebAppData", token.encode(), hashlib.sha256)
            
            hash = hmac.new(secret_key.digest(), data_check_string.encode(), hashlib.sha256).hexdigest()
            
            if hash != user_hash:
                raise
        except:
            raise HTTPException(status_code=401, detail='Bad initData')   
        
        request.state.user_data = json.loads(parsed_data.get('user'))
        logging.debug(request.state.user_data)
        return await call_next(request)     
