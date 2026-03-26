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

## 📅 Día 6 — Mejora del modelo de datos y métricas reales

### 🎯 Objetivo

Mejorar la calidad del análisis introduciendo métricas más realistas y consultas más avanzadas combinando múltiples dimensiones.

---

### 🧱 Cambios realizados

* Se añadió el campo `quantity` a la tabla `sales`
* Se redefinió el concepto de “producto más vendido”
* Se mejoraron las consultas usando `SUM` en lugar de `COUNT`
* Se crearon nuevos endpoints analíticos
* Se realizaron consultas agrupadas por múltiples dimensiones

---

### 🗄️ Base de datos

#### Tabla `sales` actualizada

```sql
CREATE TABLE sales (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    date TEXT,
    product_id INTEGER,
    quantity INTEGER,
    revenue INTEGER,
    FOREIGN KEY (product_id) REFERENCES products(id)
);
```

---

### 🧠 Mejora clave

Antes:

```sql
COUNT(*)
```

Ahora:

```sql
SUM(quantity)
```

---

### 📊 Endpoint `/top-products`

Productos más vendidos por unidades:

```sql
SELECT p.name as product, SUM(s.quantity) as total_sold
FROM sales s
JOIN products p ON s.product_id = p.id
GROUP BY p.name
ORDER BY total_sold DESC;
```

---

### 📈 Endpoint `/sales-by-date`

Ingresos por día:

```sql
SELECT date, SUM(revenue) as total_revenue
FROM sales
GROUP BY date
ORDER BY date;
```

---

### 🔥 Endpoint `/sales-by-product-by-date`

Ingresos por producto y fecha:

```sql
SELECT s.date, p.name as product, SUM(s.revenue) as total_revenue
FROM sales s
JOIN products p ON s.product_id = p.id
GROUP BY s.date, p.name
ORDER BY s.date;
```

---

### 🧠 Conceptos aprendidos

* Diferencia entre:

  * `COUNT(*)` → número de ventas
  * `SUM(quantity)` → unidades vendidas
  * `SUM(revenue)` → ingresos
* Agrupaciones múltiples (`GROUP BY s.date, p.name`)
* Diseño de métricas de negocio
* Importancia del modelo de datos en analytics
* Construcción de endpoints para BI

---

### ⚠️ Problemas encontrados

* Uso incorrecto de `GROUP BY` (faltaban columnas)
* Confusión entre métricas (ventas vs ingresos)
* Necesidad de mejorar el modelo de datos

---

### 🚀 Próximos pasos

* Añadir filtros a endpoints (`?date=`)
* Crear endpoints más específicos (por producto, categoría…)
* Empezar a estructurar el modelo tipo Data Warehouse:

  * `fact_sales`
  * `dim_product`
  * `dim_date`
* Preparar backend para consumo desde frontend

---

### 🧠 Notas personales

Este día marca un cambio importante: se pasa de consultas simples a análisis más cercanos a un entorno real.

Se empieza a entender que el diseño de la base de datos influye directamente en la calidad del análisis.

También se consolida el uso de SQL como herramienta para obtener métricas de negocio.

## 📅 Día 7 — Filtros dinámicos y queries avanzadas

### 🎯 Objetivo

Convertir endpoints estáticos en dinámicos mediante el uso de parámetros en la URL y construcción de consultas SQL flexibles.

---

### 🚀 Cambios realizados

* Implementación de filtros dinámicos en endpoints
* Uso de query parameters en FastAPI
* Construcción de consultas SQL dinámicas
* Implementación de filtros múltiples:

  * por fecha
  * por producto
  * por rango de fechas

---

### 🌐 Endpoint `/sales-by-date`

#### Sin filtro

```text
/sales-by-date
```

#### Con filtro

```text
/sales-by-date?date=2026-03-10
```

---

### 🔥 Endpoint `/sales-by-product-by-date`

#### Ejemplos de uso

```text
/sales-by-product-by-date
/sales-by-product-by-date?product=Laptop
/sales-by-product-by-date?initial_date=2026-03-10&end_date=2026-03-11
/sales-by-product-by-date?product=Mouse&initial_date=2026-03-10
```

---

### 🧩 Query dinámica implementada

```sql
SELECT s.date, p.name as product, SUM(s.revenue) as total_revenue
FROM sales s
JOIN products p ON s.product_id = p.id
WHERE ...
GROUP BY s.date, p.name
ORDER BY s.date ASC, total_revenue DESC;
```

---

### 🧠 Construcción dinámica del WHERE

* Uso de lista de condiciones (`conditions`)
* Unión mediante `AND`
* Parámetros seguros (`?`) para evitar SQL Injection

---

### 🔐 Seguridad

Se utilizan parámetros en lugar de concatenar strings:

```python
params.append(value)
```

Esto evita vulnerabilidades de SQL Injection.

---

### 📊 Funcionalidad añadida

El sistema ahora permite:

* Filtrar por un día concreto
* Filtrar por producto
* Filtrar por rango de fechas
* Combinar múltiples filtros

---

### 🧠 Conceptos aprendidos

* Query parameters en APIs (`?param=value`)
* Construcción dinámica de SQL
* Uso de `WHERE` con múltiples condiciones
* Uso de `AND` en consultas
* Seguridad en consultas SQL
* Diseño de endpoints flexibles

---

### ⚠️ Problemas encontrados

* Duplicación de queries en primeras versiones
* Dificultad inicial en combinar múltiples filtros
* Gestión de parámetros en SQL

---

### 🚀 Próximos pasos

* Crear CRUD completos (products, customers, sales)
* Ampliar modelo de base de datos
* Introducir más tablas (customers, fechas)
* Simular entorno real de e-commerce

---

### 🧠 Notas personales

Este día marca un paso importante hacia un backend profesional.

Se pasa de endpoints simples a sistemas flexibles capaces de responder a múltiples escenarios.

También se introduce una forma de trabajar más cercana a proyectos reales, donde las consultas deben adaptarse dinámicamente según los filtros del usuario.

## 📅 Día 8 — Backend completo (CRUD + datos realistas)

### 🎯 Objetivo

Construir un backend completo con estructura realista, incluyendo base de datos con múltiples tablas, datos simulados y operaciones CRUD completas.

---

### 🧱 Cambios realizados

* Rediseño de la base de datos
* Creación de múltiples tablas relacionadas
* Generación automática de datos ficticios
* Implementación de CRUD completos
* Mejora de la estructura del proyecto

---

### 🗄️ Base de datos

Se implementó una estructura más cercana a un sistema real de e-commerce:

#### 📦 Tabla `products`

```sql id="xt3q9z"
id, name, category, price
```

---

#### 👤 Tabla `customers`

```sql id="u7v5ay"
id, name, email
```

---

#### 💰 Tabla `sales`

```sql id="h3bn4p"
id, date, product_id, customer_id, quantity, revenue
```

---

### 🔗 Relaciones

```text id="o1p1sd"
sales.product_id → products.id
sales.customer_id → customers.id
```

---

### ⚙️ Generación de datos

Se creó una carpeta `scripts/` con un script `seed_data.py` para generar datos automáticamente:

* ~50 productos
* ~50 clientes
* ~100 ventas

Esto permite simular un entorno real sin insertar datos manualmente.

---

### 🚀 CRUD implementados

#### 📦 Products

```text id="i8hplq"
GET    /products
GET    /products/{id}
POST   /products
PUT    /products/{id}
DELETE /products/{id}
```

---

#### 👤 Customers

```text id="8u2k9k"
GET    /customers
GET    /customers/{id}
POST   /customers
PUT    /customers/{id}
DELETE /customers/{id}
```

---

#### 💰 Sales

```text id="c9ldo2"
GET    /sales
GET    /sales/{id}
POST   /sales
PUT    /sales/{id}
DELETE /sales/{id}
```

---

### 🧠 Funcionalidades añadidas

* Filtros por:

  * producto
  * cliente
  * rango de fechas
* Queries dinámicas
* Uso de parámetros seguros (`?`) para evitar SQL Injection
* Generación automática de datos

---

### 🧠 Conceptos aprendidos

* Diseño de base de datos relacional
* Relaciones entre tablas (foreign keys)
* CRUD completo en backend
* Uso de SQLite en proyectos reales
* Generación de datos para testing
* Organización de código (api / crud / scripts)
* Queries dinámicas en SQL
* Buenas prácticas en backend

---

### ⚠️ Problemas encontrados

* Uso incorrecto de `%s` en SQLite (corregido a `?`)
* Uso de `RETURNING` (no compatible con SQLite)
* Construcción incorrecta de queries dinámas sin `WHERE`
* Validaciones faltantes en updates

---

### 🚀 Próximos pasos

* Mejorar estructura tipo Data Warehouse:

  * `fact_sales`
  * `dim_product`
  * `dim_customer`
* Preparar backend para frontend (React / Next.js)
* Añadir validaciones más estrictas
* Documentar la API

---

### 🧠 Notas personales

Este día marca el paso más importante del proyecto: se deja atrás el aprendizaje básico para construir un backend completo.

El proyecto ya tiene una estructura realista, con datos suficientes para análisis y funcionalidades que permiten escalar hacia un sistema más complejo.

Se empieza a trabajar con mentalidad de proyecto profesional, no solo de práctica.

## 📅 Día 9 — Limpieza, mappers y consultas avanzadas

### 🎯 Objetivo

Mejorar la calidad del backend, evitar duplicación de código y trabajar con consultas más avanzadas usando `JOIN` y alias.

---

### 🧱 Cambios realizados

* Refactorización del código
* Creación de mappers reutilizables
* Implementación de consultas con `JOIN`
* Corrección de errores en estructuras de datos
* Mejora de la consistencia del código

---

### 🧠 Mappers (utils)

Se creó una carpeta `utils/` con funciones para transformar los resultados de la base de datos:

```python
def map_sale(row):
    return {
        "id": row["id"],
        "date": row["date"],
        "product_id": row["product_id"],
        "customer_id": row["customer_id"],
        "quantity": row["quantity"],
        "revenue": row["revenue"]
    }
```

---

### 🚀 Mapper avanzado con JOIN

Para consultas más complejas se creó un mapper específico:

```python
def map_sale_with_names(row):
    return {
        "id": row["id"],
        "date": row["date"],
        "product_name": row["product_name"],
        "customer_name": row["customer_name"],
        "quantity": row["quantity"],
        "revenue": row["revenue"]
    }
```

---

### 🔗 Uso de JOIN

Se implementó una consulta que combina varias tablas:

```sql
SELECT 
    s.id,
    s.date,
    p.name AS product_name,
    c.name AS customer_name,
    s.quantity,
    s.revenue
FROM sales s
JOIN products p ON s.product_id = p.id
JOIN customers c ON s.customer_id = c.id
```

---

### ⚠️ Problemas encontrados

* Error al usar columnas sin alias (`p.name`)
* Uso incorrecto de estructuras `{}` en listas (creando sets)
* Inconsistencia entre query y mapper
* Errores al acceder a claves inexistentes (`IndexError`)

---

### ✅ Soluciones aplicadas

* Uso de `AS` para alias en SQL
* Corrección de list comprehensions
* Separación de mappers según tipo de consulta
* Alineación entre query y estructura de datos

---

### 🧠 Conceptos aprendidos

* Uso avanzado de `JOIN`
* Importancia de los alias (`AS`)
* Separación de responsabilidades (query vs mapper)
* Refactorización de código
* Buenas prácticas en backend
* Reutilización de lógica

---

### 🚀 Resultado

El backend ahora:

* Es más limpio
* Es más reutilizable
* Tiene consultas más potentes
* Está mejor preparado para escalar

---

### 🔥 Próximos pasos

* Endpoint `/top-products`
* Mejorar respuestas de la API (formato estándar)
* Preparar frontend
* Documentación final del proyecto

---

### 🧠 Notas personales

Este día ha sido clave para entender cómo funciona realmente un backend profesional.

Los errores han ayudado a comprender mejor cómo funcionan las consultas SQL y la relación entre los datos y el código.

Se empieza a trabajar con una mentalidad más cercana a proyectos reales.

## 📅 Día 10 — Endpoints de análisis y cierre del backend

### 🎯 Objetivo

Finalizar el backend implementando endpoints de análisis (analytics) y dejar la API lista para integrarse con un frontend.

---

### 🚀 Funcionalidades añadidas

Se han implementado endpoints avanzados para análisis de datos:

---

### 🔥 Top productos más vendidos

```text
GET /sales/top-products
```

Devuelve los productos con mayor cantidad de ventas.

---

### 🔥 Top clientes

```text
GET /sales/top-customers
```

Muestra los clientes que más dinero han gastado.

---

### 🔥 Resumen de ingresos

```text
GET /sales/revenue-summary
```

Incluye:

* Total de pedidos
* Ingresos totales
* Valor medio por pedido

---

### 🔥 Ventas por categoría

```text
GET /sales/top-sales-by-category
```

Permite analizar qué categorías generan más ingresos.

---

### 🧠 Conceptos trabajados

* Funciones agregadas en SQL (`SUM`, `COUNT`, `AVG`)
* Agrupaciones (`GROUP BY`)
* Ordenación de resultados (`ORDER BY`)
* Uso de `JOIN` para combinar tablas
* Creación de endpoints de tipo analytics

---

### ⚠️ Problemas encontrados

* Conflictos de rutas en FastAPI (`/{sale_id}` capturando otras rutas)
* Errores en alias SQL (`AS`)
* Inconsistencias entre consultas y mappers
* Errores en nombres de claves en diccionarios

---

### ✅ Soluciones aplicadas

* Reordenación de rutas (rutas dinámicas siempre al final)
* Uso correcto de alias en consultas SQL
* Separación de mappers según tipo de consulta
* Corrección de estructuras de datos

---

### 🧱 Estado final del backend

El backend ahora incluye:

* CRUD completo
* Filtros dinámicos
* Consultas con JOIN
* Endpoints de análisis
* Código modular y reutilizable

---

### 🚀 Resultado

API lista para:

* Integrarse con frontend (React u otro)
* Visualizar datos en dashboards
* Escalar con nuevas funcionalidades

---

### 🧠 Conclusión

Este día marca el cierre del backend.

Se ha pasado de operaciones básicas (CRUD) a un sistema capaz de generar métricas útiles para negocio.

El proyecto ya tiene estructura y funcionalidades similares a aplicaciones reales.

---

### 🔥 Próximo paso

👉 Desarrollo del frontend (visualización de datos)

* Gráficas
* Tablas dinámicas
* Dashboard interactivo

# 📅 Día 11 — Conexión Frontend + Backend (Dashboard funcional)

## 🚀 Objetivo

Conectar el frontend en React con el backend en FastAPI y mostrar datos reales en un dashboard.

---

## 🧱 Trabajo realizado

### 🔗 Conexión API

* Se conectó el frontend (React + Vite) con el backend (FastAPI)
* Se realizaron peticiones HTTP usando `fetch`
* Se validó la correcta respuesta del backend (status 200)

---

### ⚠️ Problema encontrado: CORS

Al intentar conectar el frontend con el backend, surgió el error:

```
No 'Access-Control-Allow-Origin' header
```

#### ✅ Solución:

Se añadió el middleware de CORS en FastAPI:

```python
from fastapi.middleware.cors import CORSMiddleware

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
```

---

### 📊 Dashboard básico

Se creó el componente `Dashboard.jsx` que:

* Obtiene datos desde la API (`/sales/revenue-summary`)
* Muestra métricas clave:

  * Total Orders
  * Total Revenue
  * Avg Order Value

---

### 🧩 Componentes reutilizables

#### Card.jsx

* Componente reutilizable para mostrar métricas
* Mejora la organización del código

---

### 🏆 Top Products

* Se integró el endpoint `/sales/top-products`
* Se muestran los productos más vendidos
* Renderizado dinámico con `.map()`

---

## 🧠 Conceptos aprendidos

* Comunicación frontend ↔ backend
* Manejo de estados con `useState`
* Uso de `useEffect` para llamadas async
* Manejo de errores reales (CORS)
* Renderizado dinámico en React
* Separación de responsabilidades (components / services)

---

## 📁 Estructura del frontend

```
src/
 ├── components/
 │    └── Card.jsx
 ├── pages/
 │    └── Dashboard.jsx
 ├── services/
 │    └── api.js
```

---

## 📌 Estado actual del proyecto

✅ Backend completo
✅ CRUD funcionando
✅ Datos ficticios realistas
✅ Frontend conectado
✅ Dashboard funcional

---

## 🚀 Próximos pasos (Día 12)

* 📊 Añadir gráficas (Recharts)
* 🎨 Mejorar diseño UI
* 📈 Visualización avanzada de datos

---

## 💬 Notas

Este día marca el paso de un proyecto backend a una aplicación fullstack funcional, siendo un punto clave en el desarrollo del dashboard.

---

## 👨‍💻 Autor

Rafael Ecija Perez
 