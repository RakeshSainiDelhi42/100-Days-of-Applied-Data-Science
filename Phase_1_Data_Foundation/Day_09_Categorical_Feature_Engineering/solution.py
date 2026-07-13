import pandas as pd

# 1. Data Ingestion
print("Loading CRM data...")
df = pd.read_csv('dataset.csv')

print("\n--- 🛑 ORIGINAL DATA (First 3 Rows) ---")
print(df.head(3).to_string(index=False))

# 2. Ordinal Encoding (For data with a strict order/hierarchy)
# We map Free to 0, Bronze to 1, etc. so the ML model understands Gold > Bronze.
tier_mapping = {
    'Free': 0,
    'Bronze': 1,
    'Silver': 2,
    'Gold': 3
}
df['Subscription_Tier_Encoded'] = df['Subscription_Tier'].map(tier_mapping)

# 3. One-Hot Encoding (For nominal data with no mathematical order)
# We use drop_first=True to avoid the "Dummy Variable Trap" (Multicollinearity)
df_encoded = pd.get_dummies(df, columns=['Acquisition_Channel'], drop_first=True)

# Convert the boolean True/False outputs from get_dummies into 1s and 0s
for col in df_encoded.columns:
    if df_encoded[col].dtype == bool:
        df_encoded[col] = df_encoded[col].astype(int)

# 4. Clean up the final dataset for the ML model
# Drop the original text column and the User_ID (since ID doesn't predict anything)
ml_ready_df = df_encoded.drop(columns=['User_ID', 'Subscription_Tier'])

print("\n--- ✅ MACHINE-LEARNING READY DATA (First 3 Rows) ---")
print(ml_ready_df.head(3).to_string(index=False))

# Verify that all columns are now numerical
print("\n--- 📊 DATA TYPES CONFIRMATION ---")
print(ml_ready_df.dtypes)