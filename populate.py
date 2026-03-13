#!/usr/bin/env python
"""
populate.py
~~~~~~~~~~~
Genera datos sintéticos y los inserta en PostgreSQL mediante COPY.
Trunca las tablas antes de cargar para evitar duplicados.
"""

import pandas as pd
from conexion.connection import get_connection, relase_connection
from generators.customers import generate_customers
from generators.dates import generate_dates
from generators.products import generate_products
from generators.sales import generate_sales
from loaders.copy_loader import copy_from_dataframe

# ----------------------------------------------------------------------
# Parámetros (puedes ajustarlos si deseas más/menos datos)
# ----------------------------------------------------------------------
NUM_DAYS = 180
NUM_CUSTOMERS = 500
NUM_PRODUCTS = 150
NUM_SALES = 5_000


def truncate_tables():
    """Vacía todas las tablas del modelo estrella y reinicia los IDs."""
    sql = """
    TRUNCATE TABLE fact_sales,
                  dim_date,
                  dim_customer,
                  dim_product
    RESTART IDENTITY CASCADE;
    """
    conn = get_connection()
    cur = conn.cursor()
    try:
        cur.execute(sql)
        conn.commit()
        print("🧹  Tablas truncadas (limpias).")
    finally:
        cur.close()
        relase_connection(conn)


def main() -> None:
    # 1️⃣  Vaciar tablas antes de cargar
    truncate_tables()

    # ---------------------- dim_date ----------------------
    dates = generate_dates(NUM_DAYS)
    df_dates = pd.DataFrame(dates)
    # dim_date tiene el mismo orden que el DataFrame → no necesitamos columns
    copy_from_dataframe(df_dates, "dim_date")
    print(f"✅ dim_date → {len(df_dates)} filas")

    # ---------------------- dim_customer ----------------------
    customers = generate_customers(NUM_CUSTOMERS)
    df_customers = pd.DataFrame(customers)
    # La tabla tiene: customer_id (SERIAL), name, email, created_at
    copy_from_dataframe(
        df_customers,
        "dim_customer",
        columns=["name", "email", "created_at"],   # omitimos customer_id
    )
    print(f"✅ dim_customer → {len(df_customers)} filas")

    # ---------------------- dim_product ----------------------
    products = generate_products(NUM_PRODUCTS)
    df_products = pd.DataFrame(products)
    # Tabla: product_id (SERIAL), name, category, price
    copy_from_dataframe(
        df_products,
        "dim_product",
        columns=["name", "category", "price"],   # omitimos product_id
    )
    print(f"✅ dim_product → {len(df_products)} filas")

    # ---------------------- fact_sales ----------------------
    fact_sales = generate_sales(
        customers=customers,
        products=products,
        dates=dates,
        num_sales=NUM_SALES,
    )
    df_sales = pd.DataFrame(fact_sales)
    # Tabla: sale_id (SERIAL), date_id, customer_id, product_id, quantity, total_amount
    copy_from_dataframe(
        df_sales,
        "fact_sales",
        columns=[
            "date_id",
            "customer_id",
            "product_id",
            "quantity",
            "total_amount",
        ],
    )
    print(f"✅ fact_sales → {len(df_sales)} filas")

    # -------------------------------------------------------
    print("\n🎉  Población completada. Ya tienes datos reales en la BD.")


if __name__ == "__main__":
    main()
