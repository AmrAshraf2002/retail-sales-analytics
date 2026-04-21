import pandas as pd
import sqlite3

# =========================
# 1. Connect to Database
# =========================
conn = sqlite3.connect("database/database.db")
cursor = conn.cursor()

print("✅ Connected to SQLite database")


# =========================
# 2. Load Cleaned Data
# =========================
df = pd.read_csv("data/processed/cleaned_data.csv")

print("Data loaded:", df.shape)


# =========================
# 3. Insert into Stores
# =========================
stores_df = df[["store_id"]].drop_duplicates()

stores_df.to_sql("Stores", conn, if_exists="append", index=False)

print("✅ Stores inserted")


# =========================
# 4. Insert into Sales
# =========================
sales_df = df[["store_id", "date", "weekly_sales", "holiday_flag"]]

sales_df.to_sql("Sales", conn, if_exists="append", index=False)

print("✅ Sales inserted")


# =========================
# 5. Insert into External Factors
# =========================
external_df = df[[
    "store_id",
    "date",
    "temperature",
    "fuel_price",
    "cpi",
    "unemployment"
]]

external_df.to_sql("External_Factors", conn, if_exists="append", index=False)

print("✅ External Factors inserted")


# =========================
# 6. Close Connection
# =========================
conn.commit()
conn.close()

print("🎉 Data successfully inserted into database!")