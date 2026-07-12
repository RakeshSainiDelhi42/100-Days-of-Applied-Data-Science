import pandas as pd
import numpy as np
import random

np.random.seed(42)

n_rows = 200
routes = ['RT_01', 'RT_02', 'RT_03', 'RT_04', 'RT_05']
drivers = ['Alice', 'Bob', 'Charlie', 'David', 'Eve']
traffic_states = ['Light', 'Moderate', 'Heavy']

# Map drivers to routes
driver_map = dict(zip(routes, drivers))

data = {
    'Route_ID': [random.choice(routes) for _ in range(n_rows)],
    'Traffic_Condition': [random.choice(traffic_states) for _ in range(n_rows)]
}

df = pd.DataFrame(data)
df['Driver_Name'] = df['Route_ID'].map(driver_map)

# Generate Delivery Times based on traffic logic
def generate_time(row):
    base_time = np.random.randint(30, 50) # Normal delivery takes 30-50 mins
    
    # Add time based on traffic
    if row['Traffic_Condition'] == 'Moderate':
        base_time += np.random.randint(15, 30)
    elif row['Traffic_Condition'] == 'Heavy':
        base_time += np.random.randint(45, 90)
        
    # INJECT ANOMALY: Make David on RT_04 unusually slow during Light traffic
    if row['Route_ID'] == 'RT_04' and row['Traffic_Condition'] == 'Light':
        base_time += np.random.randint(40, 60) 
        
    return base_time

df['Delivery_Time_Minutes'] = df.apply(generate_time, axis=1)

# Save to CSV
df.to_csv('dataset.csv', index=False)
print("✅ dataset.csv successfully generated with delivery logs!")