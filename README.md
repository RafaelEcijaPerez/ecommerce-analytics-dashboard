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
