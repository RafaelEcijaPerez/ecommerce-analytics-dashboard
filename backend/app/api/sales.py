#Ventas
from fastapi import APIRouter

router=APIRouter()

@router.get("/")
#sacar todas las ventas
def get_sales():
    return {
        "message": "Sales endpoint working",
        "data": [
            {"date": "2026-03-10", "revenue": 1200},
            {"date": "2026-03-11", "revenue": 900}
        ]
    }