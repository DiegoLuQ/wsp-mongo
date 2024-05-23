from fastapi import APIRouter, HTTPException, status
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse
from core.models.model_usuario import Model_Usuario
from core.db.querys.querys_usuarios import *
from core.db.database import db
router = APIRouter()


@router.post("/usuarios/")
async def create_usuario(model: Model_Usuario):
    try:
        data = await insert_usuario(jsonable_encoder(model))
        if data:
            
            return JSONResponse(status_code=status.HTTP_200_OK,
                            content={
                                "msg": "Usuario creado con exito"
                            })
        return JSONResponse(status_code=status.HTTP_200_OK,
                            content={
                                "msg": "Mensaje ya estaba creado"
                            })
    except Exception as e:
        print(e)


@router.get("/usuarios/{usuario_id}")
async def read_usuario(usuario_id: str):
    usuario = await get_usuario(usuario_id)
    if usuario:
        return usuario
    raise HTTPException(status_code=404, detail="Usuario not found")


@router.patch("/usuarios/{usuario_id}")
async def put_usuario(usuario_id: str, usuario: dict):
    return await update_usuario(usuario_id, usuario)


@router.delete("/usuarios/{usuario_id}")
async def remove_usuario(usuario_id: str):
    return await delete_usuario(usuario_id)
