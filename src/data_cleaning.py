import pandas as pd

# =========================
# 1. Load Data
# =========================
file_path = "data/raw/walmart-sales-dataset-of-45stores.csv"
df = pd.read_csv(file_path)

print("Initial Shape:", df.shape)
print(df.head())


# =========================
# 2. Rename Columns (clean naming)
# =========================
df.columns = df.columns.str.strip().str.lower()

# Optional: make names consistent
df.rename(columns={
    "store": "store_id",
    "weekly_sales": "weekly_sales",
    "holiday_flag": "holiday_flag",
    "temperature": "temperature",
    "fuel_price": "fuel_price",
    "cpi": "cpi",
    "unemployment": "unemployment"
}, inplace=True)


# =========================
# 3. Handle Missing Values
# =========================
print("\nMissing Values Before:\n", df.isnull().sum())

# Fill numeric columns with median
numeric_cols = ["weekly_sales", "temperature", "fuel_price", "cpi", "unemployment"]

for col in numeric_cols:
    df[col] = df[col].fillna(df[col].median())

# Fill holiday_flag with 0 (assume non-holiday)
df["holiday_flag"] = df["holiday_flag"].fillna(0)

print("\nMissing Values After:\n", df.isnull().sum())


# =========================
# 4. Fix Data Types
# =========================

# Convert date to datetime
df["date"] = pd.to_datetime(df["date"], errors="coerce")

# Convert back to string (SQLite-friendly)
df["date"] = df["date"].dt.strftime("%Y-%m-%d")

# Ensure integer types
df["store_id"] = df["store_id"].astype(int)
df["holiday_flag"] = df["holiday_flag"].astype(int)


# =========================
# 5. Remove Duplicates
# =========================
before = df.shape[0]
df = df.drop_duplicates()
after = df.shape[0]

print(f"\nRemoved {before - after} duplicate rows")


# =========================
# 6. Basic Validation
# =========================
print("\nData Types:\n", df.dtypes)
print("\nSummary:\n", df.describe())


# =========================
# 7. Save Cleaned Data
# =========================
output_path = "data/processed/cleaned_data.csv"
df.to_csv(output_path, index=False)

print("\n✅ Cleaned data saved to:", output_path)