#Ventas
from fastapi import APIRouter, Query
from app.crud.sales import get_sale, get_sales_by_product_id, get_sales_by_product_category, get_sales_by_date_range ,get_all_sales, crate_sale, update_sale, delete_sale, get_top_products, get_top_customers,get_top_sales_by_category,get_revenue_summary, get_sales_by_customer_id
from typing import Optional
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
@router.get("/top-products")
def read_top_products():
    data = get_top_products()
    return {
        "data": data
    }
@router.get("/top-customers")
def read_top_customers():
    data = get_top_customers()
    return {
        "data": data
    }
@router.get("/top-sales-by-category")
def read_top_sales_by_category():
    data = get_top_sales_by_category()
    return {
        "data": data
    }
@router.get("/revenue-summary")
def read_revenue_summary():
    data = get_revenue_summary()
    return {
        "data": data
    }
@router.get("/date-range")
def read_sales_by_date_range(
    start_date: Optional[str] = Query(None, alias="start_date"),
    end_date: Optional[str] = Query(None, alias="end_date"),
    start: Optional[str] = Query(None, alias="start"),
    end: Optional[str] = Query(None, alias="end")
):
    # support both query param names for backward/forward compatibility
    s = start_date or start
    e = end_date or end
    data = get_sales_by_date_range(s, e)
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
@router.get("/category/{category}")
def read_sales_by_category(category: str):
    data = get_sales_by_product_category(category)
    return {
        "data": data
    }

@router.get("/customer/{customer_id}")
def read_sales_by_customer_id(customer_id: int):
    data = get_sales_by_customer_id(customer_id)
    return {
        "data": data
    }


@router.post("/")
def create_new_sale(date: str, product_id: int, customer_id: int, quantity: int, revenue: float):
    sale_id = crate_sale(date, product_id, customer_id, quantity, revenue)
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

