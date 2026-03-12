-- ==============================
--  Dimensiones
-- ==============================
CREATE TABLE dim_date (
    date_id DATE PRIMARY KEY,
    year    INT,
    month   INT,
    day     INT,
    weekday TEXT
);

CREATE TABLE dim_customer (
    customer_id SERIAL PRIMARY KEY,
    name        TEXT NOT NULL,
    email       TEXT UNIQUE NOT NULL,
    created_at  TIMESTAMP DEFAULT now()
);

CREATE TABLE dim_product (
    product_id SERIAL PRIMARY KEY,
    name       TEXT NOT NULL,
    category   TEXT,
    price      NUMERIC(10,2)
);

-- ==============================
--  Hecho (Fact)
-- ==============================
CREATE TABLE fact_sales (
    sale_id      SERIAL PRIMARY KEY,
    date_id      DATE REFERENCES dim_date(date_id),
    customer_id  INT REFERENCES dim_customer(customer_id),
    product_id   INT REFERENCES dim_product(product_id),
    quantity     INT,
    total_amount NUMERIC(12,2)
);
