import pandas as pd
import sqlite3

# 1. Establish a connection to the SQL database
print("Connecting to the database...")
conn = sqlite3.connect('company_data.db')

# 2. Write the raw SQL Query
# We join the tables and filter for orders > $500 on the server side to save RAM
sql_query = """
    SELECT 
        c.name, 
        c.country, 
        o.order_id, 
        o.order_date, 
        o.total_amount
    FROM customers c
    JOIN orders o ON c.customer_id = o.customer_id
    WHERE o.total_amount > 500
    ORDER BY o.total_amount DESC;
"""

# 3. Data Ingestion (Executing SQL via Pandas)
# Pandas sends the query to the DB, the DB does the heavy lifting, and Pandas just downloads the result
high_value_df = pd.read_sql_query(sql_query, conn)

# ALWAYS close your database connections!
conn.close()

# 4. Analytics & Reporting
total_high_value_revenue = high_value_df['total_amount'].sum()
top_country = high_value_df['country'].value_counts().index[0]

print("\n--- 💎 HIGH-VALUE CUSTOMER REPORT (Orders > $500) ---")
print(f"Total High-Value Orders Found: {len(high_value_df)}")
print(f"Total Revenue from these orders: ${total_high_value_revenue:,.2f}")
print(f"Top Country for High-Value Orders: {top_country}")
print("-" * 50)
print("Top 5 Largest Single Orders:")
print(high_value_df.head().to_string(index=False))