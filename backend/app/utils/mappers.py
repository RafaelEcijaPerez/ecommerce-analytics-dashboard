def map_product(row):
    return {
        "id": row["id"],
        "name": row["name"],
        "category": row["category"],
        "price": row["price"]
    }

def map_customer(row):
    return {
        "id": row["id"],
        "name": row["name"],
        "email": row["email"]
    }
def map_sale(row):
    return {
        "id": row["id"],
        "date": row["date"],
        "product_id": row["product_id"],
        "customer_id": row["customer_id"],
        "quantity": row["quantity"],
        "revenue": row["revenue"]
    }

def map_sale_with_names(row):
    return {
        "id": row["id"],
        "date": row["date"],
        "product_name": row["product_name"],
        "customer_name": row["customer_name"],
        "quantity": row["quantity"],
        "revenue": row["revenue"]
    }