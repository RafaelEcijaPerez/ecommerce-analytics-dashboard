#Conecion a la base de datos
import os
import psycopg2
from psycopg2 import pool

#Variables de entorno para la conexion a la base de datos
HOST = os.getenv("PGHOST", "localhost")
PORT = int(os.getenv("PGPORT", 5432))
DB   = os.getenv("PGDATABASE", "oltp")
USER = os.getenv("PGUSER", "admin")
PASS = os.getenv("PGPASSWORD", "admin")

#Crear un pool de conexiones
_pool = None

def _init_pool() -> None:
    global _pool
    if _pool is None:
        _pool = pool.SimpleConnectionPool(
            minconn=1,
            maxconn=5,
            host=HOST,
            port=PORT,
            database=DB,
            user=USER,
            password=PASS,
        )

#Obtener una conexion del pool
def get_connection():
    if _pool is None:
        _init_pool()
    return _pool.getconn()

#Cerrar una conexion
def close_connection(conn):
    if _pool:
        _pool.closeall()

#Devolver la conexion pool
def relase_connection(conn):
    if _pool:
        _pool.putconn(conn)