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


## 👨‍💻 Autor

Rafael Ecija Perez
