from pydantic import SecretStr
from pydantic_settings import BaseSettings, SettingsConfigDict


class Config(BaseSettings):
    bot_token: SecretStr
    
    webhook_url: str = ''
    webapp_url: str = ''
    
    app_host: str = 'webhook'
    app_port: int = 8080
    
    redis_host: str
    redis_port: int
    redis_password: SecretStr
    
    model_config = SettingsConfigDict(
        env_file='.env'
    )
    
config = Config()
