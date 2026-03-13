# ecommerce-analytics-dashboard

# E‑Commerce Analytics Dashboard

**Objetivo**: Construir un panel de métricas de ventas (SQL + Data‑Warehouse) con frontend React/Next, API FastAPI y BI Metabase.

## Tecnologías
- Frontend: Next.js + TypeScript + Chakra UI
- API: FastAPI (Python) + SQLAlchemy
- DB OLTP: PostgreSQL (Docker)
- DW: PostgreSQL con modelo estrella (citus opcional)
- ETL: dbt
- BI: Metabase (Docker)

## Quick‑start (local)

```bash
# 1️⃣ Clonar el repo
git clone https://github.com/TU_USUARIO/ecommerce-analytics-dashboard.git
cd ecommerce-analytics-dashboard

# 2️⃣ Frontend
cd frontend
npm install
npm run dev   # http://localhost:3000

# 3️⃣ DB
cd ..
docker run -d --name pg-oltp \
  -e POSTGRES_USER=admin -e POSTGRES_PASSWORD=admin \
  -e POSTGRES_DB=oltp -p 5432:5432 postgres:15-alpine
psql -h localhost -U admin -d oltp -f db/schema.sql


Dia 2
“Poblar la base de datos con datos sintéticos”
Este documento explica cómo generar y cargar datos de ejemplo en la base de datos PostgreSQL del proyecto e‑commerce‑analytics‑dashboard.
Todo el proceso está automatizado mediante scripts Python, generadores de datos y un loader que usa el comando COPY (muy rápido).

ecommerce-analytics-dashboard/
│
├─ conexion/                     # todo lo relacionado con la conexión y helpers de DB
│   ├─ __init__.py
│   └─ connection.py       # gestión de conexión (singleton)
│
├─ generators/             # generación de datos sintéticos (sin tocar la BD)
│   ├─ __init__.py
│   ├─ dates.py
│   ├─ customers.py
│   ├─ products.py
│   └─ sales.py
│
├─ loaders/                 # lógica que inserta data en PostgreSQL (usa COPY)
│   ├─ __init__.py
│   └─ copy_loader.py
│
├─ tests/                   # tests unitarios (pytest)
│   ├─ __init__.py
│   ├─ test_dates.py
│   ├─ test_customers.py
│   └─ test_products.py
│
├─ populate.py              # orquestador (punto de entrada)
├─ requirements.txt        # dependencias mínimas del pipeline
├─ README.md
└─ db/schema.sql           
Nota: Los scripts están diseñados para ejecutarse desde la raíz del proyecto (ecommerce-analytics-dashboard/) con el entorno virtual activado.

🛠️ Requisitos previos
Herramienta	Versión mínima	Comentario
Python	3.12	Usamos venv y paquetes pandas, psycopg2‑binary, SQLAlchemy.
Docker Desktop	4.x	Necesario para el contenedor PostgreSQL (pg-oltp).
PostgreSQL	15 (imagen postgres:15-alpine)	Ya viene dentro del contenedor.
Git	cualquier	Para versionado y CI.
Instalar dependencias (solo la primera vez)
# 1️⃣ Crear y activar el entorno virtual
python -m venv .venv
source .venv/Scripts/activate   # PowerShell: .\.venv\Scripts\Activate.ps1

# 2️⃣ Instalar paquetes
pip install --upgrade pip
pip install -r backend/requirements.txt

El archivo backend/requirements.txt contiene:

pandas==3.0.1
psycopg2-binary==2.9.11

🐳 Levantar la base de datos (Docker)
# Desde la raíz del proyecto
docker run -d `
  --name pg-oltp `
  -e POSTGRES_USER=admin `
  -e POSTGRES_PASSWORD=admin `
  -e POSTGRES_DB=oltp `
  -p 5432:5432 `
  postgres:15-alpine
Puerto: 5432 en tu máquina → se conecta con localhost:5432.
Credenciales: admin / admin.
Base: oltp.
Si el contenedor ya existe y está detenido: docker start pg-oltp.

🚀 Ejecutar el script de población
# Asegúrate de que el entorno virtual sigue activo (prompt con (.venv))
python backend/populate.py
Salida esperada
🧹  Tablas truncadas (limpias).
✅ dim_date → 180 filas
✅ dim_customer → 500 filas
✅ dim_product → 150 filas
✅ fact_sales → 5000 filas

🎉  Población completada. Ya tienes datos reales en la BD.
Qué hace el script
Trunca todas las tablas (fact_sales, dim_date, dim_customer, dim_product) y reinicia los IDs.
Genera datos sintéticos:
dim_date → 180 días a partir de hoy.
dim_customer → 500 clientes (name, email, created_at).
dim_product → 150 productos (categoría aleatoria, precio 5‑500).
fact_sales → 5 000 ventas aleatorias (FK a cliente, producto y fecha).
Convierte cada lista a pandas.DataFrame.
Inserta los DataFrames en PostgreSQL usando COPY (a través de loaders/copy_loader.py).
Imprime un resumen y finaliza.
🧪 Tests unitarios (generadores)
Los tests están en backend/tests/. Ejecuta:

pytest -q
Salida típica:

....                                            [100%]
4 passed in 0.78s
Qué verifican
Test	Qué comprueba
test_dates.py	Genera 180 fechas correctas y el campo weekday es una cadena.
test_customers.py	Genera 500 clientes; email tiene formato customer{i}@example.com.
test_products.py	Genera 150 productos; categoría pertenece a la lista predefinida y el precio está entre 5‑500.
test_sales.py	Crea 5 000 ventas y verifica que los IDs (customer_id, product_id) están dentro del rango de los datos generados.
