import pandas as pd
import numpy as np
from datetime import datetime, timedelta
import random

np.random.seed(42)

n_rows = 50
departments = ['IT', 'Sales', 'HR', 'Engineering', 'Marketing']

# Generate base data
data = {
    'Employee_ID': [f"EMP_{i:03d}" for i in range(1, n_rows + 1)],
    'Name': [f"Employee_{i}" for i in range(1, n_rows + 1)],
    'Department': [random.choice(departments) for _ in range(n_rows)],
    'Hire_Date': [(datetime(2015, 1, 1) + timedelta(days=random.randint(0, 3000))) for _ in range(n_rows)],
    'Salary': np.random.randint(50000, 150000, size=n_rows)
}

df = pd.DataFrame(data)

# Inject 10 blank (NaN) Hire_Dates
missing_indices = random.sample(range(n_rows), 10)
df.loc[missing_indices, 'Hire_Date'] = np.nan

# Inject 5 exact duplicate rows
duplicates = df.sample(5)
df = pd.concat([df, duplicates], ignore_index=True)

# Shuffle the dataset to make it look realistic
df = df.sample(frac=1).reset_index(drop=True)

# Save to CSV
df.to_csv('dataset.csv', index=False)
print("✅ dataset.csv successfully generated with duplicates and missing hire dates!")