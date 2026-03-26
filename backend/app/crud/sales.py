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
        
            map_sale(sale)
            for sale in sales
        
    ]

def get_top_products():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT p.name AS product_name, SUM(s.quantity) AS total_sold
        FROM sales s
        JOIN products p ON s.product_id = p.id
        GROUP BY p.name
        ORDER BY total_sold DESC
        LIMIT 5
    """)

    rows = cursor.fetchall()

    cursor.close()
    conn.close()

    return [
        {
            "product_name": row["product_name"],
            "total_sold": row["total_sold"]
        }
        for row in rows
    ]

def get_top_customers():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("""
        SELECT c.name AS customer_name,SUM(s.revenue) AS total_spent
        FROM sales s
        JOIN customers c ON s.customer_id = c.id
        GROUP BY c.name
        ORDER BY total_spent DESC
        LIMIT 5
    """)
    top_customers = cursor.fetchall()
    cursor.close()
    conn.close()
    return [
        {
            "customer_name": customer["customer_name"],
            "total_spent": customer["total_spent"]
        }
        for customer in top_customers
    ]

def get_revenue_summary():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("""
        SELECT COUNT(*) AS total_orders, SUM(revenue) AS total_revenue, AVG(revenue) AS avg_order_value
        FROM sales
    """)
    revenue_summary = cursor.fetchall()
    cursor.close()
    conn.close()
    return [
        {
            "total_orders": summary["total_orders"],
            "total_revenue": summary["total_revenue"],
            "avg_order_value": summary["avg_order_value"]
        }
        for summary in revenue_summary
    ]
def get_top_sales_by_category():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("""
        SELECT p.category, SUM(s.revenue) AS total_revenue
        FROM sales s
        JOIN products p ON s.product_id = p.id
        GROUP BY p.category
        ORDER BY total_revenue DESC
        LIMIT 5
    """)
    top_sales_by_category = cursor.fetchall()
    cursor.close()
    conn.close()
    return [
        {
            "category": category["category"],
            "total_revenue": category["total_revenue"]
        }
        for category in top_sales_by_category
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

