import pandas as pd
import numpy as np
import random

# Set seed for reproducibility
np.random.seed(42)
random.seed(42)

# 1. Generate users.csv (Demographics)
user_ids = [f"U_{i:03d}" for i in range(1, 101)]
ages = np.random.randint(18, 65, size=100)
locations = random.choices(['New York', 'Los Angeles', 'Chicago', 'Houston', 'Miami'], k=100)

users_df = pd.DataFrame({'User_ID': user_ids, 'Age': ages, 'Location': locations})

# 2. Generate purchases.csv (Transactions)
purchase_ids = [f"P_{i:04d}" for i in range(1, 301)]
# Randomly assign purchases to users (some will buy multiple times)
purchase_users = random.choices(user_ids, k=300)

# Simulate older demographics spending more money
amounts = []
for uid in purchase_users:
    # Look up the user's age
    age = users_df.loc[users_df['User_ID'] == uid, 'Age'].values[0]
    if age > 40:
        amounts.append(np.round(np.random.uniform(50.0, 500.0), 2))
    else:
        amounts.append(np.round(np.random.uniform(10.0, 150.0), 2))

purchases_df = pd.DataFrame({
    'Purchase_ID': purchase_ids,
    'User_ID': purchase_users,
    'Amount_Spent': amounts
})

# Save to CSV
users_df.to_csv('users.csv', index=False)
purchases_df.to_csv('purchases.csv', index=False)
print("✅ users.csv and purchases.csv successfully generated!")