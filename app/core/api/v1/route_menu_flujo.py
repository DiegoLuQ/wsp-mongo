from fastapi import APIRouter, HTTPException
from fastapi.encoders import jsonable_encoder

from core.models.model_menu_flujo import MenuDocumento
from core.db.database import db

router = APIRouter()

@router.post('/add_menu')
async def registrar_menu(model:MenuDocumento):
    data = jsonable_encoder(model)
    existing_document = await db.menu_col.find_one({"numero_celular": model.numero_celular})
    
    if existing_document:
        print("Menu Registrado")
        return existing_document

    await db.menu_col.insert_one(data)
    return data