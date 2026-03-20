from database.db import get_connection

def get_products():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT name, category FROM products")
    rows = cursor.fetchall()

    products = []
    for row in rows:
        products.append({
            "name": row["name"],
            "category": row["category"]
        })

    cursor.close()
    conn.close()

    return products