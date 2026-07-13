import pandas as pd
import numpy as np
from datetime import datetime, timedelta
import random

np.random.seed(42)
n_rows = 200

# Base timestamps
start_time = datetime(2023, 10, 1, 8, 0, 0)
add_times = [start_time + timedelta(minutes=random.randint(0, 10000)) for _ in range(n_rows)]

# Generate Checkout Times (usually 2 to 45 minutes after adding to cart)
checkout_times = []
for t in add_times:
    if random.random() > 0.2: # 80% of users actually checkout
        checkout_times.append(t + timedelta(minutes=random.randint(2, 45), seconds=random.randint(0, 59)))
    else:
        # 20% abandon their cart
        checkout_times.append(np.nan)

df = pd.DataFrame({
    'Session_ID': [f"SESS_{i:04d}" for i in range(1, n_rows + 1)],
    'Add_to_Cart_Time': add_times,
    'Checkout_Time': checkout_times
})

# Format as string to mimic raw server logs
df['Add_to_Cart_Time'] = df['Add_to_Cart_Time'].dt.strftime('%Y-%m-%d %H:%M:%S')
df['Checkout_Time'] = pd.to_datetime(df['Checkout_Time']).dt.strftime('%Y-%m-%d %H:%M:%S')

# INJECT A GLITCH: One user somehow checked out 5 minutes BEFORE adding to cart
df.loc[15, 'Checkout_Time'] = (pd.to_datetime(df.loc[15, 'Add_to_Cart_Time']) - timedelta(minutes=5)).strftime('%Y-%m-%d %H:%M:%S')

df.to_csv('dataset.csv', index=False)
print("✅ dataset.csv successfully generated with shopping cart logs!")