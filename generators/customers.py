import random
from datetime import datetime, timedelta
from typing import List, Dict

"""
Devuelve una lista de dicts, una fila por cliente.
Cada fila contiene:
"name" | "email" | "created_at"
"""
def generate_customers(num_customers: int = 500) -> List[Dict]:
    rows = []
    for i in range(1,num_customers +1):
        rows.append({
            "name": f"Customer {i}",
            "email": f"customer{i}@example.com",
            "created_at": datetime.now()
                - timedelta(days=random.randint(0, 365)),
        })
    return rows
