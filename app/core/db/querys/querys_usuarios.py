from core.db.database import db
from core.models.model_usuario import Model_Usuario

async def insert_usuario(usuario_data: dict):

    existing_user = await db.usuario_col.find_one({"wsp_wamid": usuario_data['wsp_wamid']})
    if existing_user:
        # Si ya existe un usuario con el mismo wamid de usuario, puedes decidir cómo manejarlo
        # Aquí simplemente retornamos el usuario existente
        return False
    
    else:
        result = await db.usuario_col.insert_one(usuario_data)
        if result:
            return True
    
    return False
    

async def get_usuario(usuario_id: str):
    usuario = await db.usuario_col.find_one({"_id": usuario_id})
    return usuario

async def update_usuario(usuario_id: str, usuario_data: dict):
    try:
        usuario = await db.usuario_col.find_one({'_id': usuario_id},{'_id':0})
        if usuario:
            stored_item_model = Model_Usuario(**usuario)
            update_data = usuario.model_dump(exclude_unset=True)
            updated_item = stored_item_model.model_copy(update=update_data)

        data_update = await db.usuario_col.update_one({'_id': usuario_id},
                                                    {'$set': updated_item})
        if data_update:
            return {**usuario_data, "_id": usuario_id}
        return False
    except Exception as e:
        print(e)

async def delete_usuario(usuario_id: str):
    await db.usuario_col.delete_one({"_id": usuario_id})
    return {"message": "Usuario deleted successfully"}
