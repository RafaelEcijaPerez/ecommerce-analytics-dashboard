import random
from typing import List, Dict

"""
Crea filas de venta aleatoria.
    - customer_id y product_id son índices (1‑based) que apuntan a
    las listas `customers` y `products`.
    - date_id proviene de la lista de fechas.
"""

def generate_sales(
        customers: List[Dict], 
        products: List[Dict], 
        dates: List[Dict], 
        num_sales: int = 5000
) -> List[Dict]:
    rows: List[Dict] = []
    for _ in range(num_sales):
        cust_id = random.randint(1, len(customers))
        prod_id = random.randint(1, len(products))
        date_id = random.choice(dates)["date_id"]
        qty = random.randint(1, 10)
        price = products[prod_id - 1]["price"]
        total = round(price * qty, 2)

        rows.append(
            {
                "date_id": date_id,
                "customer_id": cust_id,
                "product_id": prod_id,
                "quantity": qty,
                "total_amount": total,
            }
        )
    return rows