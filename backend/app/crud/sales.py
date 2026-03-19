#Ejemplo para sacar las ventas, esto se puede modificar para sacar las ventas de la base de datos
def get_sales():
    """
    return {
        "message": "Sales endpoint working",
        "data": [
            {"date": "2026-03-10", "revenue": 1200},
            {"date": "2026-03-11", "revenue": 900}
        ]
    }"""


    data = [
        {"date": "2026-03-10", "revenue": 1200},
        {"date": "2026-03-11", "revenue": 900}
    ]

    total = sum(item["revenue"] for item in data)

    return data, total
