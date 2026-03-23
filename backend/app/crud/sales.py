from database.db import get_connection

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
    cursor.execute("SELECT id, date, product_id, customer_id, quantity, revenue FROM sales WHERE id = ?", (sale_id,))
    sale = cursor.fetchone()
    cursor.close()
    conn.close()
    if sale:
        return {
            "id": sale["id"],
            "date": sale["date"],
            "product_id": sale["product_id"],
            "customer_id": sale["customer_id"],
            "quantity": sale["quantity"],
            "revenue": sale["revenue"]
        }
    return None
def get_sales_by_product_id(product_id):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT id, date, product_id, customer_id, quantity, revenue FROM sales WHERE product_id = ?", (product_id,))
    sales = cursor.fetchall()
    cursor.close()
    conn.close()
    return [
        {
            "id": sale["id"],
            "date": sale["date"],
            "product_id": sale["product_id"],
            "customer_id": sale["customer_id"],
            "quantity": sale["quantity"],
            "revenue": sale["revenue"]
        }
        for sale in sales
    ]
def get_sales_by_customer_id(customer_id):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT id, date, product_id, customer_id, quantity, revenue FROM sales WHERE customer_id = ?", (customer_id,))
    sales = cursor.fetchall()
    cursor.close()
    conn.close()
    return [
        {
            "id": sale["id"],
            "date": sale["date"],
            "product_id": sale["product_id"],
            "customer_id": sale["customer_id"],
            "quantity": sale["quantity"],
            "revenue": sale["revenue"]
        }
        for sale in sales
    ]
def get_sales_by_date_range(start_date, end_date):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT id, date, product_id, customer_id, quantity, revenue FROM sales WHERE date BETWEEN ? AND ?", (start_date, end_date))
    sales = cursor.fetchall()
    cursor.close()
    conn.close()
    return [
        {
            "id": sale["id"],
            "date": sale["date"],
            "product_id": sale["product_id"],
            "customer_id": sale["customer_id"],
            "quantity": sale["quantity"],
            "revenue": sale["revenue"]
        }
        for sale in sales
    ]
def get_all_sales():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT id, date, product_id, customer_id, quantity, revenue FROM sales")
    sales = cursor.fetchall()
    cursor.close()
    conn.close()
    return [
        {
            "id": sale["id"],
            "date": sale["date"],
            "product_id": sale["product_id"],
            "customer_id": sale["customer_id"],
            "quantity": sale["quantity"],
            "revenue": sale["revenue"]
        }
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
        {
            "id": sale["id"],
            "date": sale["date"],
            "product_id": sale["product_id"],
            "customer_id": sale["customer_id"],
            "quantity": sale["quantity"],
            "revenue": sale["revenue"]
        }
        for sale in sales
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
