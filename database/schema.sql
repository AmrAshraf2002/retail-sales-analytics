-- =====================================
-- Retail Sales Database Schema (SQLite)
-- =====================================

-- Enable foreign key constraints
PRAGMA foreign_keys = ON;

-- =========================
-- 1. Stores Table
-- =========================
CREATE TABLE IF NOT EXISTS Stores (
    store_id INTEGER PRIMARY KEY
);

-- =========================
-- 2. Sales Table (FACT TABLE)
-- =========================
CREATE TABLE IF NOT EXISTS Sales (
    sales_id INTEGER PRIMARY KEY AUTOINCREMENT,
    store_id INTEGER NOT NULL,
    date TEXT NOT NULL,
    weekly_sales REAL NOT NULL,
    holiday_flag INTEGER CHECK (holiday_flag IN (0,1)),

    FOREIGN KEY (store_id) REFERENCES Stores(store_id)
);

-- =========================
-- 3. External Factors Table
-- =========================
CREATE TABLE IF NOT EXISTS External_Factors (
    record_id INTEGER PRIMARY KEY AUTOINCREMENT,
    store_id INTEGER NOT NULL,
    date TEXT NOT NULL,
    temperature REAL,
    fuel_price REAL,
    cpi REAL,
    unemployment REAL,

    FOREIGN KEY (store_id) REFERENCES Stores(store_id)
);

-- =========================
-- 4. Indexes (Performance Optimization 🔥)
-- =========================

-- Speed up joins
CREATE INDEX IF NOT EXISTS idx_sales_store_date 
ON Sales(store_id, date);

CREATE INDEX IF NOT EXISTS idx_external_store_date 
ON External_Factors(store_id, date);

-- =========================
-- 5. Optional View (Advanced 🔥)
-- =========================
-- This creates a ready-to-use joined dataset

CREATE VIEW IF NOT EXISTS Sales_Full_View AS
SELECT 
    s.sales_id,
    s.store_id,
    s.date,
    s.weekly_sales,
    s.holiday_flag,
    e.temperature,
    e.fuel_price,
    e.cpi,
    e.unemployment
FROM Sales s
JOIN External_Factors e
ON s.store_id = e.store_id AND s.date = e.date;