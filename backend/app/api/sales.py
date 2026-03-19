#Ventas
from fastapi import APIRouter
from app.crud.sales import get_sales
router=APIRouter()

@router.get("/")
#sacar todas las ventas
def read_sales():
    """Ejemplo para sacar las ventas, esto se puede modificar para sacar las ventas de la base de datos
    return {
        "message": "Sales endpoint working",
        "data": [
            {"date": "2026-03-10", "revenue": 1200},
            {"date": "2026-03-11", "revenue": 900}
        ]
    }"""
    data, total = get_sales()
    return {
        "data": data,
        "total_revenue": total
    }
@router.get("/summary")
def sales_summary():
    data, total = get_sales()

    return {
        "total_revenue": total,
        "days": len(data)
    }