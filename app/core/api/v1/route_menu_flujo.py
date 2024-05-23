from fastapi import APIRouter
from fastapi.encoders import jsonable_encoder

from core.models.model_menu_flujo import MenuDocumento
from core.db.database import db

 
router = APIRouter()



@router.post('/add_menu')
async def registrar_menu(model:MenuDocumento):
    data = jsonable_encoder(model)
    await db.menu_col.insert_one(data)
    return data