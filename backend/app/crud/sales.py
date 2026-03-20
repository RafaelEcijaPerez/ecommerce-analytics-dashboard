from database.db import get_connection

#Ejemplo para sacar las ventas, esto se puede modificar para sacar las ventas de la base de datos
def get_sales():
    # Simulación de datos de ventas
    """
    return {
        "message": "Sales endpoint working",
        "data": [
            {"date": "2026-03-10", "revenue": 1200},
            {"date": "2026-03-11", "revenue": 900}
        ]
    }"""

    """
    data = [
        {"date": "2026-03-10", "revenue": 1200},
        {"date": "2026-03-11", "revenue": 900}
    ]

    total = sum(item["revenue"] for item in data)

    return data, total
    """

    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT date, revenue FROM sales")

    # Obtener la primera fila de resultados
    #rows = cursor.fetchall()

    #obtener todas las filas de resultados
    rows = cursor.fetchall()
    
    data = []
    #bucle para sacar todas las ventas
    for row in rows:
        #añade en el diccionario la fecha y el ingreso
        data.append({
            "date": row["date"],
            "revenue": row["revenue"]
        })

    #cierra la conexión a la base de datos
    cursor.close()
    conn.close()

    #devolver el total de las ventas
    total = sum(item["revenue"] for item in data)
    return data , total

#ejemplo para sacar las ventas por fecha, esto se puede modificar para sacar las ventas de la base de datos
def get_sales_by_date(date: str):
    #Concetar a la base de datos
    conn = get_connection()
    cursor = conn.cursor()

    #Ejecutar la consulta para sacar las ventas por fecha
    cursor.execute("SELECT date, revenue FROM sales WHERE date = ?", (date,))

    #obtener todas las filas de resultados
    rows = cursor.fetchall()

    data = []
    #bucle para sacar todas las ventas por fecha
    for row in rows:
        #añade en el diccionario la fecha y el ingreso
        data.append({
            "date": row["date"],
            "revenue": row["revenue"]
        })

    #cierra la conexión a la base de datos
    cursor.close()
    conn.close()

    return data 

def get_sales_with_products():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT s.date, p.name as product, s.revenue
        FROM sales s
        JOIN products p ON s.product_id = p.id
    """)

    rows = cursor.fetchall()

    data = []
    for row in rows:
        data.append({
            "date": row["date"],
            "product": row["product"],
            "revenue": row["revenue"]
        })

    conn.close()
    return data

def get_Top_products():
    conn = get_connection()
    cursor = conn.cursor()
    #producto que mas se ha vendido
    cursor.execute("""
        SELECT p.name as product, COUNT(*) as total_sales
        FROM sales s
        JOIN products p ON s.product_id = p.id
        GROUP BY p.name
        ORDER BY total_sales DESC
        LIMIT 5
    """)
    rows = cursor.fetchall()
    data = []
    for row in rows:
        data.append({
            "product": row["product"],
            "total_sales": row["total_sales"]
        })

    conn.close()
    return data
