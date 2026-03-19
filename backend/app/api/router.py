#Rutas de enlace con las otros archivos
from fastapi import APIRouter
from app.api.sales import router as sales_router

api_router = APIRouter()
#incluir la rutas
api_router.include_router(sales_router, prefix="/sales", tags=["Sales"])