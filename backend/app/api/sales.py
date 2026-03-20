#Ventas
from fastapi import APIRouter
from app.crud.sales import get_sales , get_sales_by_date, get_sales_with_products, get_Top_products
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

@router.get("/sales-by-date/{date}")
def sales_by_date(date: str):
    data = get_sales_by_date(date)

    if not data:
        return {"message": f"No sales found for date {date}"}

    return {"data": data}

@router.get("/sales-with-products")
def sales_with_products():
    data = get_sales_with_products()

    if not data:
        return {"message": "No sales found with products"}

    return {
        "data": data
    }
    
    
@router.get("/top-products")
def top_products():
    data = get_Top_products()

    if not data:
        return {"message": "No top products found"}

    return {
        "data": data
    }