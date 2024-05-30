from fastapi import APIRouter, HTTPException
from fastapi.encoders import jsonable_encoder

from core.models.model_menu_flujo import MenuDocumento
from core.db.database import db

router = APIRouter()

@router.post('/add_menu')
async def registrar_menu(model: MenuDocumento):
    data = jsonable_encoder(model)
    data.pop("_id", None)
    
    if model.numero_celular:
        # Si no hay _id, buscamos por numero_celular
        existing_document = await db.menu_col.find_one({"numero_celular": model.numero_celular})
        
        if existing_document:
            # Actualiza el documento existente con la nueva información
            await db.menu_col.update_one(
                {"_id": existing_document['_id']},
                {"$set": data}
            )
            print("Menu actualizado")
            updated_document = await db.menu_col.find_one({"_id": existing_document['_id']})
            return updated_document
        
    else:
        existing_document = await db.menu_col.find_one({"_id": model.id})
        
        if existing_document:
            # Actualiza el documento existente con la nueva información
            await db.menu_col.update_one(
                {"_id": model.id},
                {"$set": data}
            )
            print("Menu actualizado")
            updated_document = await db.menu_col.find_one({"_id": model.id})
            return updated_document
        
    
    # Inserta un nuevo documento si no existe
    insert_result = await db.menu_col.insert_one(data)
    new_document = await db.menu_col.find_one({"_id": insert_result.inserted_id})
    return new_document