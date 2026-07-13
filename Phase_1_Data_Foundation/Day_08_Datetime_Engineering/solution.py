import pandas as pd

# 1. Data Ingestion
print("Loading server logs...")
df = pd.read_csv('dataset.csv')
original_count = len(df)

# 2. Datetime Engineering
# Convert string logs into actual Pandas Datetime objects
df['Add_to_Cart_Time'] = pd.to_datetime(df['Add_to_Cart_Time'])
df['Checkout_Time'] = pd.to_datetime(df['Checkout_Time'])

# 3. Data Cleaning (Handling missing values and glitches)
# Drop abandoned carts (where Checkout_Time is NaT - Not a Time)
clean_df = df.dropna(subset=['Checkout_Time']).copy()

# Calculate the Timedelta (Time to Conversion)
clean_df['Time_to_Conversion'] = clean_df['Checkout_Time'] - clean_df['Add_to_Cart_Time']

# Filter out glitches (where time to conversion is negative)
clean_df = clean_df[clean_df['Time_to_Conversion'] >= pd.Timedelta(seconds=0)]

# 4. Feature Extraction
# Extract the total seconds from the timedelta, then convert to minutes
clean_df['Conversion_Minutes'] = clean_df['Time_to_Conversion'].dt.total_seconds() / 60

# 5. Reporting
avg_conversion = clean_df['Conversion_Minutes'].mean()
fastest_checkout = clean_df['Conversion_Minutes'].min()
slowest_checkout = clean_df['Conversion_Minutes'].max()
abandonment_rate = ((original_count - len(clean_df)) / original_count) * 100

print("\n--- 🛒 E-COMMERCE CONVERSION REPORT ---")
print(f"Total Sessions Logged: {original_count}")
print(f"Cart Abandonment Rate (incl. glitches): {abandonment_rate:.1f}%")
print("-" * 40)
print(f"⏱️  Average Time to Checkout: {avg_conversion:.2f} minutes")
print(f"⚡ Fastest Checkout: {fastest_checkout:.1f} minutes")
print(f"🐢 Slowest Checkout: {slowest_checkout:.1f} minutes")