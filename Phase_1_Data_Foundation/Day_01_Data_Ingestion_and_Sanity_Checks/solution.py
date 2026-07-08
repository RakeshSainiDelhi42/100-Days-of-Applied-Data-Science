import pandas as pd
from datetime import datetime

# 1. Data Ingestion
print("Loading raw data...")
df = pd.read_csv('dataset.csv')
original_row_count = len(df)

# 2. Sanity Checks & Data Cleaning
# Convert Date column to actual datetime objects
df['Date'] = pd.to_datetime(df['Date'])

# Create a filter condition for valid data
valid_conditions = (
    (df['Quantity_Sold'] > 0) &          # Quantity must be positive
    (df['Price_Per_Unit'] > 0) &         # Price must be strictly greater than 0
    (df['Date'] <= pd.Timestamp.today()) # Date cannot be in the future
)

# Apply the filter and drop any rows with NaN (Missing) values
clean_df = df[valid_conditions].dropna()

# 3. Analytics & Reporting
# Calculate revenue per transaction
clean_df['Total_Revenue'] = clean_df['Quantity_Sold'] * clean_df['Price_Per_Unit']

# Calculate final metrics
total_revenue = clean_df['Total_Revenue'].sum()
rows_removed = original_row_count - len(clean_df)

print("\n--- 📊 DAILY BUSINESS REPORT ---")
print(f"Total Rows Processed: {original_row_count}")
print(f"Corrupted Rows Removed: {rows_removed}")
print(f"Valid Transactions: {len(clean_df)}")
print(f"✅ True Gross Revenue: ${total_revenue:,.2f}")