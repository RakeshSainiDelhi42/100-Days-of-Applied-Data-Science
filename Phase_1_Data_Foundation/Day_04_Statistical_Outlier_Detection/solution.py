import pandas as pd

# 1. Data Ingestion
print("Loading ride-sharing data...")
df = pd.read_csv('dataset.csv')

# 2. Feature Engineering
# We calculate a standardized metric to compare all rides fairly
df['Price_Per_Mile'] = df['Fare_Amount'] / df['Distance_Miles']

# 3. Statistical Outlier Detection (Using IQR)
# Q1 is the 25th percentile, Q3 is the 75th percentile
Q1 = df['Price_Per_Mile'].quantile(0.25)
Q3 = df['Price_Per_Mile'].quantile(0.75)
IQR = Q3 - Q1

# Define the upper bound for what is considered mathematically "normal"
# Any value above this threshold is a statistical outlier
upper_bound = Q3 + 1.5 * IQR

# 4. Filter and Isolate Anomalies
anomalous_rides = df[df['Price_Per_Mile'] > upper_bound].sort_values(by='Price_Per_Mile', ascending=False)

# 5. Output Report
print("\n--- 🚨 RIDE FARE AUDIT REPORT 🚨 ---")
print(f"Total Rides Processed: {len(df)}")
print(f"Normal Average Price/Mile: ${df[df['Price_Per_Mile'] <= upper_bound]['Price_Per_Mile'].mean():.2f}")
print(f"Anomalous Rides Detected: {len(anomalous_rides)}")
print(f"Percentage of Fraudulent Rides: {(len(anomalous_rides) / len(df)) * 100:.2f}%\n")

print("Top 5 Most Suspicious Rides:")
print(anomalous_rides[['Ride_ID', 'Distance_Miles', 'Fare_Amount', 'Price_Per_Mile']].head(5).to_string(index=False))