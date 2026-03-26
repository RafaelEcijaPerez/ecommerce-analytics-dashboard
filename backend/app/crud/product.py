from database.db import get_connection
from app.utils.mappers import map_product

# CRUD operations for the Product model
#create
def create_product(name, category, price):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO products (name, category, price) VALUES (?, ?, ?) ",
                   (name, category, price))
    product_id = cursor.lastrowid
    conn.commit()
    cursor.close()
    conn.close()
    return product_id

#read
def get_product(product_id):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT id, name, category, price FROM products WHERE id = ?", (product_id,))
    product = cursor.fetchone()
    cursor.close()
    conn.close()
    if product:
        return map_product(product)
    return None
#Read products for arguments
def get_products_price_range(min_price, max_price):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT id, name, category, price FROM products WHERE price BETWEEN ? AND ?",
                   (min_price, max_price))
    products = cursor.fetchall()
    cursor.close()
    conn.close()
    return [
        map_product(product)
        for product in products
    ]

def get_products_by_argument(name=None, category=None, min_price=None, max_price=None):
    conn = get_connection()
    cursor = conn.cursor()
    
    query = "SELECT id, name, category, price FROM products"
    conditions = []
    params = []

    if name:
        conditions.append("name = ?")
        params.append(name)

    if category:
        conditions.append("category = ?")
        params.append(category)

    if min_price is not None:
        conditions.append("price >= ?")
        params.append(min_price)

    if max_price is not None:
        conditions.append("price <= ?")
        params.append(max_price)

    if conditions:
        query += " WHERE " + " AND ".join(conditions)

    cursor.execute(query, params)
    products = cursor.fetchall()
    cursor.close()
    conn.close()
    return [
        {
            map_product(product)
            for product in products
        }
    ]

def get_all_products():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT id, name, category, price FROM products")
    products = cursor.fetchall()
    cursor.close()
    conn.close()
    return [
        map_product(product)
        for product in products
    ]

#update
def update_product(product_id, name=None, category=None, price=None):
    conn = get_connection()
    cursor = conn.cursor()
    
    query = "UPDATE products SET"
    params = []

    if name:
        query += " name = ?,"
        params.append(name)
    if category:
        query += " category = ?,"
        params.append(category)
    if price is not None:
        query += " price = ?,"
        params.append(price)
    if not params:
        return  None
    # Remove the trailing comma
    query = query.rstrip(',')
    query += " WHERE id = ?"
    params.append(product_id)

    cursor.execute(query, params)
    conn.commit()
    cursor.close()
    conn.close()

#delete
def delete_product(product_id):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM products WHERE id = ?", (product_id,))
    conn.commit()
    cursor.close()
    conn.close()

