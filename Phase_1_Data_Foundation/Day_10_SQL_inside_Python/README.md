# 📊 Day 10: SQL inside Python

## 🏢 The Business Scenario
The Sales Director requested a report on "High-Value Customers" (customers who placed individual orders over $500). The data was stored in a relational database (`company_data.db`) across multiple tables. Loading a massive database entirely into computer RAM via Pandas is highly inefficient and prone to crashing, so the data needed to be filtered at the source.

## 🎯 The Objective
1. Connect to the SQLite database using Python's `sqlite3` library.
2. Write a raw SQL query to `JOIN` the `customers` and `orders` tables.
3. Use a SQL `WHERE` clause to filter out orders under $500 *before* data ingestion.
4. Load the optimized, pre-filtered data into a Pandas DataFrame for final reporting.

## 🛠️ Tools & Libraries Used
* **Python**
* **SQLite3** (Database connection management)
* **Pandas** (`pd.read_sql_query()` for SQL execution and dataframe creation)
* **SQL** (`JOIN`, `WHERE`, `ORDER BY`)

## 🧠 Key Learnings & Takeaways
* **Server-Side Filtering:** By leveraging SQL to perform the `JOIN` and `WHERE` operations, the database engine does the heavy computational lifting. Pandas only downloads the final, lightweight result, preventing RAM overload.
* **SQL/Python Integration:** The `pd.read_sql_query()` function is incredibly powerful. It completely removes the need to write complex standard-library cursor loops to fetch SQL data, seamlessly bridging the gap between Data Engineering (SQL databases) and Data Science (Pandas DataFrames).
* **Connection Management:** Always ending scripts with `conn.close()` is a vital engineering best practice to prevent database memory leaks and locked files.

---
*This is Day 10 of my [100 Days of Applied Data Science](../README.md) journey.*