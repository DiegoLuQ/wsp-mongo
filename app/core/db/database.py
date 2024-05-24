from motor.motor_asyncio import AsyncIOMotorClient
from .config import settings as sett


class Database:
    def __init__(self):
        
        uri = sett.MONGO_URL
        self.client = AsyncIOMotorClient(uri)
        self.lianbot_db = self.client["lianbot_db"]
        self.menu_col = self.lianbot_db["menu_col"]
        self.usuario_col = self.lianbot_db["usuarios_col"]

    async def create_indexes(self):
        await self.menu_col.create_index([("numero_celular", 1)], unique=True)

db = Database()