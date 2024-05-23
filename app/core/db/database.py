from motor.motor_asyncio import AsyncIOMotorClient
from .config import settings as sett



class Creden:
    MONGO_USER: str = sett.MONGO_USER
    MONGO_PASSWORD: str = sett.MONGO_PASSWORD
    MONGO_HOST: str = sett.MONGO_HOST
    MONGO_DB: str = sett.MONGO_DB

cred = Creden()

class Database:
    def __init__(self):
        # uri = f"mongodb://root:example@pro_mongo:27020/lianbot_db?authSource=admin"
        
        uri = f"mongodb://{cred.MONGO_USER}:{cred.MONGO_PASSWORD}@{cred.MONGO_HOST}/{cred.MONGO_DB}?authSource=admin"
        # mongodb://root:example@localhost:27018/lianbot_db?authSource=admin
        self.client = AsyncIOMotorClient(uri)
        self.lianbot_db = self.client["lianbot_db"]
        self.menu_col = self.lianbot_db["menu_col"]
        self.usuario_col = self.lianbot_db["usuarios_col"]

    async def create_indexes(self):
        await self.menu_col.create_index([("numero_celular", 1)], unique=True)

db = Database()