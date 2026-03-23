from database.db import get_connection
# CRUD operations for the Customer model
# Create
def create_customer(name, email):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO customers (name, email) VALUES (?, ?)", (name, email))
    customer_id = cursor.lastrowid
    conn.commit()
    cursor.close()
    conn.close()
    return customer_id
# Read
def get_customer(customer_id):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT id, name, email FROM customers WHERE id = ?", (customer_id,))
    customer = cursor.fetchone()
    cursor.close()
    conn.close()
    if customer:
        return {
            "id": customer["id"],
            "name": customer["name"],
            "email": customer["email"]
        }
    return None

def get_customers_by_name(name):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT id, name, email FROM customers WHERE name = ?", (name,))
    customers = cursor.fetchall()
    cursor.close()
    conn.close()
    return [
        {
            "id": customer["id"],
            "name": customer["name"],
            "email": customer["email"]
        }
        for customer in customers
    ]
def get_customers_by_email(email):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT id, name, email FROM customers WHERE email = ?", (email,))
    customers = cursor.fetchall()
    cursor.close()
    conn.close()
    return [
        {
            "id": customer["id"],
            "name": customer["name"],
            "email": customer["email"]
        }
        for customer in customers
    ]

# Update
def update_customer(customer_id, name=None, email=None):
    conn = get_connection()
    cursor = conn.cursor()
    
    query = "UPDATE customers SET "
    updates = []
    params = []

    if name:
        updates.append("name = ?")
        params.append(name)
    if email:
        updates.append("email = ?")
        params.append(email)

    query += ", ".join(updates) + " WHERE id = ?"
    params.append(customer_id)

    cursor.execute(query, params)
    conn.commit()
    cursor.close()
    conn.close()

# Delete
def delete_customer(customer_id):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM customers WHERE id = ?", (customer_id,))
    conn.commit()
    cursor.close()
    conn.close()

def get_all_customers():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT id, name, email FROM customers")
    customers = cursor.fetchall()
    cursor.close()
    conn.close()
    return [
        {
            "id": customer["id"],
            "name": customer["name"],
            "email": customer["email"]
        }
        for customer in customers
    ]
