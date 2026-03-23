#Ventas
from fastapi import APIRouter, Query
from app.crud.sales import get_sale, get_sales_by_product_id, get_sales_by_product_category, get_sales_by_date_range ,get_all_sales, crate_sale, update_sale, delete_sale
router=APIRouter()

@router.get("/")
def read_sales():
    data = get_all_sales()
    return {
        "data": data
    }
@router.get("/search")
def search_sales(customer_id: int = Query(None), product_id: int = Query(None), min_amount: float = Query(None), max_amount: float = Query(None)):
    data = get_sales_by_product_id(product_id) if product_id else get_all_sales()
    return {
        "data": data
    }

@router.get("/{sale_id}")
def read_sale(sale_id: int):
    data = get_sale(sale_id)
    if data:
        return {
            "data": data
        }
    return {
        "error": "Sale not found"
    }, 404
@router.post("/")
def create_new_sale(customer_id: int, product_id: int, amount: float):
    sale_id = crate_sale(customer_id, product_id, amount)
    return {
        "message": "Sale created successfully",
        "sale_id": sale_id
    }
@router.put("/{sale_id}")
def update_existing_sale(sale_id: int, customer_id: int = None, product_id : int = None, amount: float = None):
    success = update_sale(sale_id, customer_id, product_id, amount)
    if success:
        return {
            "message": "Sale updated successfully"
        }
    return {
        "error": "Sale not found"
    }, 404
@router.delete("/{sale_id}")
def delete_existing_sale(sale_id: int):
    success = delete_sale(sale_id)
    if success:
        return {
            "message": "Sale deleted successfully"
        }
    return {
        "error": "Sale not found"
    }, 404
@router.get("/category/{category}")
def read_sales_by_category(category: str):
    data = get_sales_by_product_category(category)
    return {
        "data": data
    }
@router.get("/date-range")
def read_sales_by_date_range(start_date: str, end_date: str):
    data = get_sales_by_date_range(start_date, end_date)
    return {
        "data": data
    }
