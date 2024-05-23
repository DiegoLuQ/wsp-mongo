from pathlib import Path
from dotenv import load_dotenv
import os

env_path = Path('.') / '.env'
load_dotenv(dotenv_path=env_path)

class Settings:
    DB_MONGO = os.environ.get('DB_MONGO')
    RUTA_CLUSTER=os.environ.get('RUTA_CLUSTER')
    
    
    MONGO_USER=os.environ.get("MONGO_USER")
    MONGO_PASSWORD=os.environ.get("MONGO_PASSWORD")
    MONGO_HOST=os.environ.get("MONGO_HOST")
    MONGO_DB=os.environ.get("MONGO_DB")
    
    ACCESS_TOKEN_EXPIRE_MINUTES = 180
    ALGORITHM = os.environ.get('ALGORITHM')
    ORIGINS_MAIN = os.environ.get('ORIGINS_MAIN')
    SECRET_KEY = os.environ.get('SECRET_KEY')

settings = Settings()