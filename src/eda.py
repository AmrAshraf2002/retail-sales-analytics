#connect python to DB
import sqlite3
import pandas as pd

# =========================
# Connect to DB
# =========================
conn = sqlite3.connect("database/database.db")

print("✅ Connected to SQLite database")

#load tables into pandas using SQL queries
sales_df = pd.read_sql_query("SELECT * FROM Sales", conn)
stores_df = pd.read_sql_query("SELECT * FROM Stores", conn)
external_df = pd.read_sql_query("SELECT * FROM External_Factors", conn)

print(sales_df.head())

#==========================
query = """
SELECT SUM(weekly_sales) AS total_sales
FROM Sales;
"""

result = pd.read_sql_query(query, conn)
print(result)

#==========================
query = """
SELECT store_id, SUM(weekly_sales) AS total_sales
FROM Sales
GROUP BY store_id
ORDER BY total_sales DESC;
"""

store_sales = pd.read_sql_query(query, conn)
print(store_sales.head())

#==========================
query = """
SELECT store_id, SUM(weekly_sales) AS total_sales
FROM Sales
GROUP BY store_id
ORDER BY total_sales DESC;
"""

store_sales = pd.read_sql_query(query, conn)
print(store_sales.head())
#==========================
#top 5 stores by sales
print(store_sales.head(5))