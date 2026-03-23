from fastapi import APIRouter
from app.crud.customer import get_customer, get_customers_by_name,get_customers_by_email ,get_all_customers, create_customer, update_customer, delete_customer
router = APIRouter()

@router.get("/")
def read_customers():
    data = get_all_customers()
    return {
        "data": data
    }
@router.get("/search")
def search_customers(name: str = None, email: str = None):  
    if name:
        data = get_customers_by_name(name)
    elif email:
        data = get_customers_by_email(email)
    else:
        data = get_all_customers()
    return {
        "data": data
    }
@router.get("/{customer_id}")
def read_customer(customer_id: int):
    data = get_customer(customer_id)
    if data:
        return {
            "data": data
        }
    return {
        "error": "Customer not found"
    }, 404
@router.post("/")
def create_new_customer(name: str, email: str):
    customer_id = create_customer(name, email)
    return {
        "message": "Customer created successfully",
        "customer_id": customer_id
    }
@router.put("/{customer_id}")
def update_existing_customer(customer_id: int, name: str = None, email: str = None):
    success = update_customer(customer_id, name, email)
    if success:
        return {
            "message": "Customer updated successfully"
        }
    return {
        "error": "Customer not found"
    }, 404
@router.delete("/{customer_id}")
def delete_existing_customer(customer_id: int):
    success = delete_customer(customer_id)
    if success:
        return {
            "message": "Customer deleted successfully"
        }
    return {
        "error": "Customer not found"
    }, 404
