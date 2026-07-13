import pandas as pd
import numpy as np
import random

# Set seed for reproducibility
np.random.seed(42)
random.seed(42)

n_rows = 250

tiers = ['Free', 'Bronze', 'Silver', 'Gold']
channels = ['SEO', 'Social Media', 'Email', 'Referral']

df = pd.DataFrame({
    'User_ID': [f"USR_{i:04d}" for i in range(1, n_rows + 1)],
    'Engagement_Score': np.random.randint(10, 100, size=n_rows),
    'Subscription_Tier': random.choices(tiers, weights=[0.6, 0.2, 0.15, 0.05], k=n_rows),
    'Acquisition_Channel': random.choices(channels, k=n_rows)
})

# Save to CSV
df.to_csv('dataset.csv', index=False)
print("✅ dataset.csv successfully generated with categorical text data!")