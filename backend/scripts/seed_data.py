import random
from datetime import datetime, timedelta
from database.db import get_connection


def seed_data():
    conn = get_connection()
    cursor = conn.cursor()

    # limpiar tablas
    cursor.execute("DELETE FROM sales")
    cursor.execute("DELETE FROM products")
    cursor.execute("DELETE FROM customers")

    # -------------------
    # PRODUCTS
    # -------------------
    categories = ["Electronics", "Clothing", "Home"]
    products = []

    for i in range(1, 51):
        products.append((
            f"Product_{i}",
            categories[i % len(categories)],
            (i * 10) + 5
        ))

    cursor.executemany(
        "INSERT INTO products (name, category, price) VALUES (?, ?, ?)",
        products
    )

    # -------------------
    # CUSTOMERS
    # -------------------
    customers = []

    for i in range(1, 51):
        customers.append((
            f"Customer_{i}",
            f"customer{i}@email.com"
        ))

    cursor.executemany(
        "INSERT INTO customers (name, email) VALUES (?, ?)",
        customers
    )

    # -------------------
    # SALES
    # -------------------
    sales = []
    start_date = datetime(2026, 3, 1)

    for _ in range(100):
        date = start_date + timedelta(days=random.randint(0, 10))
        product_id = random.randint(1, 50)
        customer_id = random.randint(1, 50)
        quantity = random.randint(1, 5)

        price = product_id * 10 + 5
        revenue = price * quantity

        sales.append((
            date.strftime("%Y-%m-%d"),
            product_id,
            customer_id,
            quantity,
            revenue
        ))

    cursor.executemany(
        "INSERT INTO sales (date, product_id, customer_id, quantity, revenue) VALUES (?, ?, ?, ?, ?)",
        sales
    )

    conn.commit()
    conn.close()

    print("✅ Datos generados correctamente")


if __name__ == "__main__":
    seed_data()