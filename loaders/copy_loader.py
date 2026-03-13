# backend/loaders/copy_loader.py
import io                     # necesario para BytesIO
import pandas as pd
from conexion.connection import get_connection, relase_connection


def copy_from_dataframe(
    df: pd.DataFrame,
    table_name: str,
    columns: list[str] | None = None,
) -> None:
    """
    Inserta el contenido de un DataFrame en la tabla indicada usando COPY.

    Parámetros
    ----------
    df : pd.DataFrame
        DataFrame sin índice y sin header (COPY los ignora).
    table_name : str
        Nombre de la tabla destino (debe existir).
    columns : list[str] | None
        Lista de columnas **en el mismo orden que aparecen en el CSV**.
        Si se omite, COPY asume que el CSV sigue el mismo orden que la tabla.
    """
    # ------------------------------------------------------------------
    # Convertimos el DataFrame a CSV (tab‑separado) en memoria
    # ------------------------------------------------------------------
    csv_bytes = df.to_csv(
        index=False,
        header=False,
        sep="\t",
        lineterminator="\n",
        encoding="utf-8",
    ).encode()

    csv_stream = io.BytesIO(csv_bytes)   # objeto file‑like para psycopg2

    # ------------------------------------------------------------------
    # Construimos la sentencia COPY; si se especifican columnas, las incluimos
    # ------------------------------------------------------------------
    if columns:
        cols_sql = f"({', '.join(columns)})"
    else:
        cols_sql = ""

    copy_sql = (
        f"COPY {table_name} {cols_sql} "
        f"FROM STDIN WITH (FORMAT csv, DELIMITER E'\\t')"
    )

    # ------------------------------------------------------------------
    # Ejecutamos COPY
    # ------------------------------------------------------------------
    conn = get_connection()
    cur = conn.cursor()
    try:
        cur.copy_expert(copy_sql, csv_stream)
        conn.commit()
    finally:
        cur.close()
        relase_connection(conn)
