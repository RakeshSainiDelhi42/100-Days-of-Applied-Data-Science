import pandas as pd
import numpy as np
import random

# Set seed for reproducibility
np.random.seed(42)
n_rows = 300

# Generate normal ride data
data = {
    'Ride_ID': [f"RIDE_{i:04d}" for i in range(1, n_rows + 1)],
    'Distance_Miles': np.round(np.random.uniform(1.0, 30.0, size=n_rows), 2)
}
df = pd.DataFrame(data)

# Base fare calculation (e.g., $2.50 per mile + $5 base fee + slight random variation)
df['Fare_Amount'] = np.round((df['Distance_Miles'] * 2.50) + 5.00 + np.random.normal(0, 2, n_rows), 2)

# INJECT ANOMALIES: 15 drivers exploiting the glitch
anomalous_indices = random.sample(range(n_rows), 15)
for idx in anomalous_indices:
    # Artificially inflate the fare by 3x to 5x
    df.loc[idx, 'Fare_Amount'] = df.loc[idx, 'Fare_Amount'] * np.random.uniform(3.0, 5.0)

df['Fare_Amount'] = np.round(df['Fare_Amount'], 2)

# Save to CSV
df.to_csv('dataset.csv', index=False)
print("✅ dataset.csv successfully generated with anomalous fares!")