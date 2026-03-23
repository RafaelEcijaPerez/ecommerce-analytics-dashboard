from database.db import get_connection

def init_db():
    #conectar a la base de datos
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""Drop TABLE IF EXISTS sales""")

    cursor.execute("""
        Drop TABLE IF EXISTS products
    """)

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS products (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT,
        category TEXT,
        price REAL
    )
    """)

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS customers (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT,
        email TEXT
    )
    """)

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS sales (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        date TEXT,
        product_id INTEGER,
        customer_id INTEGER,
        quantity INTEGER,
        revenue INTEGER,
        FOREIGN KEY (product_id) REFERENCES products(id),
        FOREIGN KEY (customer_id) REFERENCES customers(id)
    )
    """)
    #Generar datos de ejemplo para la tabla de productos
    products = [
        ("Laptop", "Electronics", 999.99),
        ("Smartphone", "Electronics", 499.99),
        ("Headphones", "Electronics", 199.99),
        ("Coffee Maker", "Home Appliances", 79.99),
        ("Blender", "Home Appliances", 59.99)
    ]
    cursor.executemany("""
        INSERT INTO products (name, category, price) VALUES (?, ?, ?)
    """, products)
    #Generar datos de ejemplo para la tabla de clientes
    

    #guardar los cambios y cerrar la conexión
    conn.commit()
    conn.close()

#iniciar la base de datos
if __name__ == "__main__":
    init_db()