#Rutas de enlace con las otros archivos
from fastapi import APIRouter
from app.api.sales import router as sales_router
from app.api.product import router as product_router

api_router = APIRouter()
#incluir la rutas
api_router.include_router(sales_router, prefix="/sales", tags=["Sales"])
api_router.include_router(product_router, prefix="/products", tags=["Products"])