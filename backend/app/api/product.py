from fastapi import APIRouter
from app.crud.product import get_product, get_products_by_argument, get_all_products, create_product, update_product, delete_product

router = APIRouter()

@router.get("/")
def read_products():
    data = get_all_products()
    return {
        "data": data
    }
@router.get("/search")
def search_products(name: str = None, category: str = None, min_price: float = None, max_price: float = None):
    data = get_products_by_argument(name, category, min_price, max_price)
    return {
        "data": data
    }
@router.get("/{product_id}")
def read_product(product_id: int):
    data = get_product(product_id)
    if data:
        return {
            "data": data
        }
    return {
        "error": "Product not found"
    }, 404
@router.post("/")
def create_new_product(name: str, category: str, price: float):
    product_id = create_product(name, category, price)
    return {
        "message": "Product created successfully",
        "product_id": product_id
    }
@router.put("/{product_id}")
def update_existing_product(product_id: int, name: str = None, category: str = None, price: float = None):
    success = update_product(product_id, name, category, price)
    if success:
        return {
            "message": "Product updated successfully"
        }
    return {
        "error": "Product not found"
    }, 404
@router.delete("/{product_id}")
def delete_existing_product(product_id: int):
    success = delete_product(product_id)
    if success:
        return {
            "message": "Product deleted successfully"
        }
    return {
        "error": "Product not found"
    }, 404
