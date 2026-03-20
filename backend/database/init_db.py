from database.db import get_connection

def init_db():
    #conectar a la base de datos
    conn = get_connection()
    cursor = conn.cursor()

    #crear tabla de sales
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS sales (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        date TEXT,
        revenue INTEGER
    )
    """)

    cursor.execute("""
INSERT INTO sales (date, product_id, revenue) VALUES
('2026-03-10', 1, 1200),
('2026-03-10', 2, 50),
('2026-03-11', 1, 900),
('2026-03-11', 3, 100)
""")
    #guardar los cambios y cerrar la conexión
    conn.commit()
    conn.close()

#iniciar la base de datos
if __name__ == "__main__":
    init_db()