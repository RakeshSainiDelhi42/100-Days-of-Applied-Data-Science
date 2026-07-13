import pandas as pd
import numpy as np
import sqlite3
import random

# Set seed for reproducibility
np.random.seed(42)

# 1. Generate Customers Data
n_customers = 100
customer_ids = [f"C_{i:03d}" for i in range(1, n_customers + 1)]
countries = ['USA', 'Canada', 'UK', 'Germany', 'Australia']

customers_df = pd.DataFrame({
    'customer_id': customer_ids,
    'name': [f"Customer_{i}" for i in range(1, n_customers + 1)],
    'country': random.choices(countries, k=n_customers)
})

# 2. Generate Orders Data
n_orders = 500
orders_df = pd.DataFrame({
    'order_id': [f"ORD_{i:04d}" for i in range(1, n_orders + 1)],
    'customer_id': random.choices(customer_ids, k=n_orders),
    'order_date': pd.date_range(start='2023-01-01', periods=n_orders, freq='D').strftime('%Y-%m-%d'),
    # Generate amounts, mostly small, but some over $500
    'total_amount': np.round(np.random.exponential(scale=250, size=n_orders), 2)
})

# 3. Create a SQL Database and write the tables to it
conn = sqlite3.connect('company_data.db')

customers_df.to_sql('customers', conn, index=False, if_exists='replace')
orders_df.to_sql('orders', conn, index=False, if_exists='replace')

conn.close()

print("✅ 'company_data.db' successfully generated with 'customers' and 'orders' SQL tables!")