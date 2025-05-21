from pydantic import SecretStr
from pydantic_settings import BaseSettings, SettingsConfigDict


class Config(BaseSettings):
    bot_token: SecretStr
    
    webhook_url: str = ''
    webhook_secret: SecretStr = ''
    
    webapp_url: str = ''
    
    backend_url: str = ''
    
    webhook_host: str = 'webhook'
    webhook_port: int = 5000
    
    backend_host: str = 'backend'
    backend_port: int = 8000
    
    postgres_db: str
    postgres_host: str
    postgres_port: int
    postgres_user: str
    postgres_password: SecretStr
    
    redis_host: str
    redis_port: int
    redis_password: SecretStr
    
    @property
    def DatabaseDSN(self):
        return f'postgresql+asyncpg://{self.postgres_user}:{self.postgres_password.get_secret_value()}@{self.postgres_host}:{self.postgres_port}/{self.postgres_db}'
    
    model_config = SettingsConfigDict(
        env_file='.env'
    )
    
config = Config()
