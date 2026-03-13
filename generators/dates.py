from datetime import date, timedelta
from typing import List, Dict

"""
Devuelve una lista de dicts, una fila por día.
Cada fila contiene:
date_id (date) | year | month | day | weekday

"""
def generate_dates(num_days: int = 180) -> List[Dict]:
    today = date.today()
    rows= []
    for i in range(num_days):
        d = today - timedelta(days=i)
        rows.append({
            "date_id": d,
            "year": d.year,
            "month": d.month,
            "day": d.day,
            "weekday": d.strftime("%A")
        })
    return rows

"""

"""