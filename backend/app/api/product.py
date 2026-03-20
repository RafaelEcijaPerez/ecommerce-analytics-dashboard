from fastapi import APIRouter
from app.crud.product import get_products

router = APIRouter()

@router.get("/")
def read_products():
    data = get_products()
    return {
        "data": data
    }