import pandas as pd

# 1. Data Ingestion
print("Loading databases...")
users_df = pd.read_csv('users.csv')
purchases_df = pd.read_csv('purchases.csv')

# 2. Relational Join
# We use a 'left' join on the purchases table to ensure we keep every single transaction, 
# while bringing in the matching demographic data from the users table based on 'User_ID'
merged_df = pd.merge(purchases_df, users_df, on='User_ID', how='left')

# 3. Feature Engineering (Binning)
# Define the edges of our age brackets and their labels
bins = [17, 25, 35, 50, 100]
labels = ['18-25', '26-35', '36-50', '51+']

# pd.cut() automatically categorizes numerical data into these bins
merged_df['Age_Bracket'] = pd.cut(merged_df['Age'], bins=bins, labels=labels)

# 4. Aggregation & Reporting
# Group by the new Age_Bracket and sum the Amount_Spent
demographic_spend = (
    merged_df.groupby('Age_Bracket', observed=True)['Amount_Spent']
    .sum()
    .reset_index()
    .sort_values(by='Amount_Spent', ascending=False)
)

# Format the output for the business report
demographic_spend['Amount_Spent'] = demographic_spend['Amount_Spent'].apply(lambda x: f"${x:,.2f}")

print("\n--- 📊 DEMOGRAPHIC SPEND REPORT ---")
print(demographic_spend.to_string(index=False))

# Extract the top spending demographic
top_demo = demographic_spend.iloc[0]
print(f"\n💡 BUSINESS INSIGHT: The {top_demo['Age_Bracket']} demographic drives the most revenue ({top_demo['Amount_Spent']}).")
print("Recommendation: Shift primary ad spend targeting to this age group.")