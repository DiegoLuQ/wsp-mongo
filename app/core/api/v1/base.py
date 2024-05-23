from fastapi import APIRouter
from .route_menu_flujo import router as router_menu_flujo
from .route_usuarios import router as router_usuarios

router = APIRouter()


router.include_router(router_menu_flujo, prefix='/menu', tags=['Menu'])
router.include_router(router_usuarios, prefix='/user', tags=['Usuarios'])
