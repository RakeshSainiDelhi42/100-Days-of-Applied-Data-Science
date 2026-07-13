# Day 10: SQL inside Python

## 🏢 The Business Scenario
The Sales Director wants a report on "High-Value Customers" (customers who placed individual orders over $500). However, the Data Engineering team didn't give you a CSV; they gave you access to a local SQLite database (`company_data.db`) containing two massive tables: `customers` and `orders`. 

## 🎯 The Objective
Loading the entire database into Pandas would crash your machine. You must:
1. Connect to the SQLite database using Python.
2. Write a raw SQL query that `JOIN`s the customers and orders tables.
3. Use a SQL `WHERE` clause to filter out any orders under $500 *before* the data ever reaches Pandas.
4. Read that highly optimized query directly into a Pandas DataFrame for final reporting.

## 📊 Data Dictionary (Inside `company_data.db`)
**Table 1: `customers`**
* `customer_id`: Unique identifier for the customer.
* `name`: Customer's full name.
* `country`: The country they are located in.

**Table 2: `orders`**
* `order_id`: Unique identifier for the order.
* `customer_id`: Foreign key linking to the customers table.
* `order_date`: The date the order was placed.
* `total_amount`: The total dollar value of the order.