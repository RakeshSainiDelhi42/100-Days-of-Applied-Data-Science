import pandas as pd
import numpy as np
from datetime import datetime, timedelta

# Set seed for reproducibility
np.random.seed(42)

# Generate 30 days of dates
n_days = 30
end_date = datetime.now()
dates = [(end_date - timedelta(days=x)).strftime('%Y-%m-%d') for x in range(n_days)]
dates.reverse() # Sort chronologically

# Generate mock data
# Signups fluctuate between 500 and 1500 a day
signups = np.random.randint(500, 1500, size=n_days)

# Upgrades correlate slightly with signups (around 10-15% conversion)
upgrades = (signups * np.random.uniform(0.10, 0.15, size=n_days)).astype(int)

# Inject a "Marketing Campaign Spike" in the last week
signups[-7:] = signups[-7:] + np.random.randint(800, 1200, size=7)
upgrades[-7:] = upgrades[-7:] + np.random.randint(150, 300, size=7)

df = pd.DataFrame({
    'Date': dates,
    'App_Signups': signups,
    'Premium_Upgrades': upgrades
})

# Save to CSV
df.to_csv('dataset.csv', index=False)
print("✅ dataset.csv successfully generated with 30 days of performance data!")