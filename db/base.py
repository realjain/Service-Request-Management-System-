from pydantic_settings import BaseSettings,SettingsConfigDict
class settings(BaseSettings):
    model_config=SettingsConfigDict(env_file='.env',extra="ignore")
    DATABASE_URL:str
    SECRET_KEY:str
    # ALGORITHM:str
    # EXPIRE_TIME:int

setting=settings()
