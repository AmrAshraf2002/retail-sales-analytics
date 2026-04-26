# 🛒 Retail Sales Analytics & Forecasting System

An end-to-end data analytics and machine learning project that analyzes Walmart retail sales data and predicts future weekly sales using economic indicators.

---

## 📌 Project Overview

This project builds a complete data pipeline starting from raw CSV data to a structured SQLite database, followed by data cleaning, exploratory data analysis (EDA), visualization, and machine learning modeling.

The goal is to understand how external economic factors such as unemployment, CPI, fuel prices, and temperature affect retail sales and to build a predictive model for future sales.

---

## 🎯 Objectives

* Design and implement a relational database using SQLite
* Clean and preprocess raw retail sales data using Python
* Perform SQL-based exploratory data analysis
* Visualize key business insights
* Build machine learning models to predict weekly sales

---

## 🧠 Dataset

Walmart Sales Forecasting Dataset containing:

* Store ID
* Date
* Weekly Sales
* Holiday Flag
* Temperature
* Fuel Price
* CPI
* Unemployment Rate

---

## 🏗️ Project Architecture

```
CSV Data
   ↓
Python (Data Cleaning / ETL)
   ↓
SQLite Database (Structured Storage)
   ↓
SQL + Python (EDA)
   ↓
Data Visualization (Matplotlib)
   ↓
Machine Learning (Sales Prediction)
```

---

## 🗄️ Database Schema

The database schema is defined in:

```
database/schema.sql
```

It includes:

* Table creation (Stores, Sales, External_Factors)
* Constraints (NOT NULL, CHECK)
* Indexes for performance optimization
* SQL view for simplified analysis

---

## 🔍 Exploratory Data Analysis

Performed analysis using SQL + Python:

* Total sales over time
* Top-performing stores
* Monthly sales trends
* Impact of unemployment on sales
* Correlation between economic factors and sales

---

## 📊 Data Visualization

Created visual insights using Matplotlib:

* Sales trends over time
* Store performance comparison
* Temperature vs Sales correlation
* Unemployment vs Sales relationship
* Distribution of weekly sales

---

## 🤖 Machine Learning

### Models Used:

* Linear Regression
* Random Forest Regressor

### Features:

* Store ID
* Temperature
* Fuel Price
* CPI
* Unemployment
* Holiday Flag

### Evaluation Metrics:

* Mean Absolute Error (MAE)
* Root Mean Squared Error (RMSE)

---

## 🛠️ Tech Stack

* Python (Pandas, NumPy, Scikit-learn)
* SQLite
* SQL
* Matplotlib
* Jupyter Notebook

---

## 🚀 Future Improvements

* Deploy model using Streamlit
* Add Power BI dashboard
* Try advanced models (XGBoost, LSTM)
* Automate ETL pipeline

---

## 👨‍💻 Author

**Amr Ashraf Mohamed Fawzy Abdelhamid**

---

## 📌 Key Learning Outcome

This project demonstrates a full data pipeline:

**Data Engineering → Analytics → Machine Learning → Insights**
