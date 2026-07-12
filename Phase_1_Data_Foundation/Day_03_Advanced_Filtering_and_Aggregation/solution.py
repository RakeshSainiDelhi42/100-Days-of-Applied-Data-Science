import pandas as pd

# 1. Data Ingestion
print("Loading logistics dataset...")
df = pd.read_csv('dataset.csv')

# 2. Advanced Filtering
# We only care about performance when external factors (traffic) are optimal
light_traffic_df = df[df['Traffic_Condition'] == 'Light']

# 3. Aggregation & Sorting
# Group by Route and Driver, calculate the mean delivery time, and sort highest to lowest
route_performance = (
    light_traffic_df.groupby(['Route_ID', 'Driver_Name'])['Delivery_Time_Minutes']
    .mean()
    .reset_index()
    .sort_values(by='Delivery_Time_Minutes', ascending=False)
)

# Rename column for clarity in the final report
route_performance.rename(columns={'Delivery_Time_Minutes': 'Avg_Time_Light_Traffic'}, inplace=True)

# 4. Final Output
worst_route = route_performance.iloc[0]

print("\n--- 📊 ROUTE EFFICIENCY REPORT (LIGHT TRAFFIC ONLY) ---")
print(route_performance.to_string(index=False))
print("\n🚨 ACTION REQUIRED 🚨")
print(f"Route {worst_route['Route_ID']} managed by {worst_route['Driver_Name']} is the least efficient.")
print(f"Average completion time in pure light traffic: {worst_route['Avg_Time_Light_Traffic']:.1f} minutes.")