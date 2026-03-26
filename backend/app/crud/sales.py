from database.db import get_connection
from app.utils.mappers import map_sale, map_sale_with_names
# CRUD operations for the Sales model
# Create
def crate_sale(date,product_id,customer_id,quantity,revenue):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO sales (date, product_id, customer_id, quantity, revenue) VALUES (?, ?, ?, ?, ?)",
                   (date, product_id, customer_id, quantity, revenue))
    sale_id = cursor.lastrowid
    conn.commit()
    cursor.close()
    conn.close()
    return sale_id
# Read
def get_sale(sale_id):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT s.id, s.date, p.name as product_name, c.name as customer_name, s.quantity, s.revenue FROM sales s JOIN products p ON s.product_id = p.id JOIN customers c ON s.customer_id = c.id WHERE s.id = ?", (sale_id,))
    sale = cursor.fetchone()
    cursor.close()
    conn.close()
    if sale:
        return  map_sale_with_names(sale)
        
    return None

def get_sales_by_product_id(product_id):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT s.id, s.date, p.name as product_name, c.name as customer_name, s.quantity, s.revenue FROM sales s JOIN products p ON s.product_id = p.id JOIN customers c ON s.customer_id = c.id WHERE s.product_id = ?", (product_id,))
    sales = cursor.fetchall()
    cursor.close()
    conn.close()
    return [
        map_sale_with_names(sale)
        for sale in sales
    ]
def get_sales_by_customer_id(customer_id):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT s.id, s.date, p.name as product_name, c.name as customer_name, s.quantity, s.revenue FROM sales s JOIN products p ON s.product_id = p.id JOIN customers c ON s.customer_id = c.id WHERE s.customer_id = ?", (customer_id,))
    sales = cursor.fetchall()
    cursor.close()
    conn.close()
    return [
        
            map_sale_with_names(sale)
            for sale in sales
        
        
    ]
def get_sales_by_date_range(start_date, end_date):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT s.id, s.date, p.name as product_name, c.name as customer_name, s.quantity, s.revenue FROM sales s JOIN products p ON s.product_id = p.id JOIN customers c ON s.customer_id = c.id WHERE s.date BETWEEN ? AND ?", (start_date, end_date))
    sales = cursor.fetchall()
    cursor.close()
    conn.close()
    return [
        
            map_sale_with_names(sale)
            for sale in sales
        
    ]
def get_all_sales():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT s.id, s.date, p.name as product_name, c.name as customer_name, s.quantity, s.revenue FROM sales s JOIN products p ON s.product_id = p.id JOIN customers c ON s.customer_id = c.id")
    sales = cursor.fetchall()
    cursor.close()
    conn.close()
    return [
        
            map_sale_with_names(sale)
            for sale in sales
        
    ]
# Get information about sales by product category
def get_sales_by_product_category(category):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("""
        SELECT s.id, s.date, s.product_id, s.customer_id, s.quantity, s.revenue
        FROM sales s
        JOIN products p ON s.product_id = p.id
        WHERE p.category = ?
    """, (category,))
    sales = cursor.fetchall()
    cursor.close()
    conn.close()
    return [
        
            map_sale_with_names(sale)
            for sale in sales
        
    ]
def get_top_products():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("""
        SELECT p.name, count(*) AS total_quantity
        FROM sales s
        JOIN products p ON s.product_id = p.id
        GROUP BY s.product_id
        ORDER BY total_quantity DESC
        LIMIT 5
    """)
    top_products = cursor.fetchall()
    cursor.close()
    conn.close()
    return [
        {
            "product_name": product["name"],
            "total_quantity": product["total_quantity"]
        }
        for product in top_products
    ]
# Update
def update_sale(sale_id, date=None, product_id=None, customer_id=None, quantity=None, revenue=None):
    conn = get_connection()
    cursor = conn.cursor()
    
    query = "UPDATE sales SET "
    updates = []
    params = []

    if date:
        updates.append("date = ?")
        params.append(date)

    if product_id:
        updates.append("product_id = ?")
        params.append(product_id)

    if customer_id:
        updates.append("customer_id = ?")
        params.append(customer_id)

    if quantity is not None:
        updates.append("quantity = ?")
        params.append(quantity)

    if revenue is not None:
        updates.append("revenue = ?")
        params.append(revenue)

    if updates:
        query += ", ".join(updates) + " WHERE id = ?"
        params.append(sale_id)
        cursor.execute(query, params)
        conn.commit()

    cursor.close()
    conn.close()

# Delete
def delete_sale(sale_id):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM sales WHERE id = ?", (sale_id,))
    conn.commit()
    cursor.close()
    conn.close()
