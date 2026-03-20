# 📊 Ecommerce Analytics Dashboard

Proyecto personal enfocado en construir una plataforma completa de analítica para e-commerce, combinando:

* Data Engineering
* APIs con FastAPI
* Frontend con Next.js
* SQL y Data Warehouse

---

## 🚀 Estado del proyecto

🔧 Día 1 — Setup inicial completado

Actualmente incluye:

* Backend con FastAPI funcionando
* Frontend con Next.js inicializado
* Estructura de proyecto profesional
* Entorno virtual configurado
* Control de versiones con Git

---

## 🧱 Estructura del proyecto

```
ecommerce-analytics-dashboard/

backend/
   app/
      main.py
      api/
   venv/
   requirements.txt

frontend/
   (Next.js app)

etl/

docs/

comandos.txt
.gitignore
README.md
```

---

## ⚙️ Tecnologías utilizadas

### Backend

* Python
* FastAPI
* Uvicorn

### Frontend

* Next.js
* React
* TailwindCSS

### Herramientas

* Git & GitHub
* Node.js

---

## ▶️ Cómo ejecutar el proyecto

### 1. Clonar repositorio

```
git clone <url-del-repo>
cd ecommerce-analytics-dashboard
```

---

### 2. Backend (FastAPI)

```
cd backend
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
uvicorn app.main:app --reload
```

Abrir en navegador:

```
http://localhost:8000/docs
```

---

### 3. Frontend (Next.js)

```
cd frontend
npm install
npm run dev
```

Abrir en navegador:

```
http://localhost:3000
```

---

## 🎯 Objetivo del proyecto

Construir un dashboard donde se puedan consultar:

* Ventas por día
* Productos más vendidos
* Cohortes de usuarios
* Predicción de ventas

---

## 🧠 Aprendizajes del Día 1

* Configuración de entorno backend con FastAPI
* Inicialización de proyecto frontend con Next.js
* Uso de Git y control de versiones
* Estructuración profesional de un proyecto full-stack

---

## 📅 Próximos pasos

* Crear rutas en FastAPI
* Diseñar endpoints de analytics
* Conectar base de datos
* Consumir API desde el frontend

---

## Día 2 — API básica

Se ha implementado la estructura inicial de la API:

- Router principal
- Endpoint `/sales`
- Organización modular (api, router, endpoints)

Se ha aprendido:

- Cómo funcionan los routers en FastAPI
- Cómo estructurar un backend profesional
- Resolución de errores de imports en Python

## 📅 Día 3 — Conexión API y lógica (CRUD)

### 🎯 Objetivo

Separar la lógica de negocio de los endpoints y construir una API más estructurada y mantenible.

---

### 🧱 Cambios realizados

Se ha implementado una arquitectura más limpia separando:

* **API (endpoints)** → `app/api/`
* **Lógica de datos (CRUD)** → `app/crud/`

---

### 🔌 Endpoint implementado

#### `/sales`

Devuelve datos de ventas junto con métricas básicas:

```json
{
  "data": [
    {"date": "2026-03-10", "revenue": 1200},
    {"date": "2026-03-11", "revenue": 900}
  ],
  "total_revenue": 2100
}
```

---

### 🧠 Flujo de la aplicación

```text
Cliente (browser)
   ↓
Endpoint (/sales)
   ↓
api/sales.py
   ↓
crud/sale.py
   ↓
Datos
```

---

### 📁 Estructura relevante

```text
app/
 ├── api/
 │    ├── router.py
 │    └── sales.py
 │
 ├── crud/
 │    └── sale.py
 │
 └── main.py
```

---

### ⚙️ Lógica implementada

En `crud/sale.py`:

* Obtención de datos de ventas (simulados)
* Cálculo de métricas:

  * total revenue

---

### 💡 Conceptos aprendidos

* Separación de responsabilidades (API vs lógica)
* Organización modular en backend
* Flujo completo de una petición HTTP
* Uso de funciones CRUD
* Mejora de la mantenibilidad del código

---

### 🚀 Próximos pasos

* Conectar con base de datos real (SQLite)
* Ejecutar queries SQL reales
* Añadir filtros (por fecha, etc.)

---

### 🧠 Notas personales

Este paso es clave para evitar código desordenado y facilita escalar el proyecto en el futuro.

## 📅 Día 4 — Base de datos (SQLite) + SQL real

### 🎯 Objetivo

Conectar la API con una base de datos real y empezar a trabajar con consultas SQL.

---

### 🧱 Cambios realizados

* Creación de base de datos con SQLite
* Definición de tabla `sales`
* Inserción de datos de prueba
* Conexión desde el backend a la base de datos
* Lectura de datos desde SQL en lugar de datos simulados

---

### 🗄️ Base de datos

Tabla inicial utilizada:

```sql
CREATE TABLE sales (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    date TEXT,
    revenue INTEGER
);
```

---

### 🔌 Conexión a la base de datos

Archivo: `database/db.py`

* Se establece conexión con SQLite
* Uso de `row_factory` para trabajar con diccionarios

---

### 📊 Endpoint `/sales`

Ahora obtiene datos reales desde la base de datos:

```json
{
  "data": [
    {"date": "2026-03-10", "revenue": 1200},
    {"date": "2026-03-11", "revenue": 900}
  ],
  "total_revenue": 2100
}
```

---

### 🧠 Flujo actualizado

```text
Cliente (browser)
   ↓
Endpoint (/sales)
   ↓
api/sales.py
   ↓
crud/sales.py
   ↓
SQLite (database)
```

---

### ⚙️ Lógica implementada

* Uso de `SELECT` para obtener datos
* Uso de `fetchall()` para recuperar múltiples filas
* Conversión de resultados SQL a formato JSON
* Cálculo de métricas (`total_revenue`)

---

### 🔍 Filtros con SQL

Se han implementado consultas con condiciones:

```sql
SELECT date, revenue 
FROM sales 
WHERE date = ?
```

Uso de parámetros para evitar SQL Injection.

---

### 💡 Conceptos aprendidos

* Conexión a base de datos con SQLite
* Diferencia entre `fetchone()` y `fetchall()`
* Ejecución de consultas SQL desde Python
* Uso de parámetros (`?`) en queries
* Transformación de datos SQL → JSON
* Separación de lógica (CRUD)

---

### ⚠️ Problemas encontrados

* Errores en imports (`ModuleNotFoundError`)
* Uso incorrecto de `fetchone()`
* Problemas con tipos de datos (`row` como string)
* Errores de sintaxis SQL

---

### 🚀 Próximos pasos

* Añadir más tablas (products)
* Realizar consultas con JOIN
* Mejorar filtros (múltiples condiciones)
* Preparar estructura para modelo dimensional (Data Warehouse)

---

### 🧠 Notas personales

Este día marca el paso de una API básica a una aplicación real conectada a datos.

Se empieza a trabajar con lógica de datos, consultas SQL y estructura profesional de backend.

## 📅 Día 5 — Relaciones (JOIN) y agregaciones SQL

### 🎯 Objetivo

Introducir relaciones entre tablas y realizar consultas más avanzadas usando `JOIN`, `GROUP BY` y funciones de agregación.

---

### 🧱 Cambios realizados

* Creación de la tabla `products`
* Relación entre `sales` y `products` mediante `product_id`
* Implementación de consultas con `JOIN`
* Creación de endpoints más avanzados
* Introducción a agregaciones (`COUNT`, `SUM`)

---

### 🗄️ Base de datos

#### Tabla `products`

```sql
CREATE TABLE products (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    category TEXT
);
```

#### Relación con `sales`

```text
sales.product_id → products.id
```

---

### 🔗 JOIN implementado

Consulta para obtener ventas con información del producto:

```sql
SELECT s.date, p.name as product, s.revenue
FROM sales s
JOIN products p ON s.product_id = p.id;
```

---

### 🌐 Endpoint `/sales-with-products`

Devuelve ventas con nombre de producto:

```json
{
  "data": [
    {"date": "2026-03-10", "product": "Laptop", "revenue": 1200}
  ]
}
```

---

### 🏆 Endpoint `/top-products`

Consulta para obtener productos más vendidos:

```sql
SELECT p.name as product, COUNT(*) as total_sales
FROM sales s
JOIN products p ON s.product_id = p.id
GROUP BY p.name
ORDER BY total_sales DESC;
```

---

### 🧠 Conceptos aprendidos

* Relaciones entre tablas (foreign keys)
* Uso de `JOIN` para combinar datos
* Agrupación de datos con `GROUP BY`
* Funciones de agregación (`COUNT`, `SUM`)
* Ordenación de resultados (`ORDER BY`)
* Diferencia entre:

  * producto más vendido (COUNT)
  * producto más rentable (SUM)

---

### ⚠️ Problemas encontrados

* Errores en queries SQL (sintaxis, uso incorrecto de funciones)
* Confusión entre `WHERE` y funciones agregadas
* Diferencias entre métricas (ventas vs ingresos)
* Separación incorrecta de archivos (API vs CRUD)

---

### 🚀 Próximos pasos

* Añadir campo `quantity` a `sales`
* Mejorar métricas (ventas reales vs ingresos)
* Avanzar hacia modelo tipo Data Warehouse (`fact_sales`, `dim_product`)
* Añadir más endpoints analíticos

---

### 🧠 Notas personales

Este día marca el paso a trabajar con datos relacionales reales.

Se empieza a pensar en términos de análisis de datos, no solo en código, entendiendo qué métricas tienen sentido y cómo obtenerlas correctamente.


## 👨‍💻 Autor

Rafael Ecija Perez
