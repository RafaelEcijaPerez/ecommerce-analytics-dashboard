import random
from typing import List, Dict

#Categorías de los productos
CATEGORIES = ["Electronics", "Clothing", "Books", "Home", "Sports"]

"""
Devuelve una lista de dicts, una fila por producto.
Cada fila contiene:
"name" | "category" | "price"
"""

def generate_products(num_products: int = 150) -> List[Dict]:
    rows=[]
    for i in range(1, num_products +1):
        rows.append({
            "name": f"Product {i}",
            "category": random.choice(CATEGORIES),
            "price": round(random.uniform(5.0, 500.0), 2),
        }
        )
    return rows