import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Set the visual style for a professional look
sns.set_theme(style="whitegrid")

# 1. Data Ingestion
print("Loading performance data...")
df = pd.read_csv('dataset.csv')
df['Date'] = pd.to_datetime(df['Date'])

# 2. Dashboard Creation (Dual-Axis Line Chart)
fig, ax1 = plt.subplots(figsize=(14, 7))

# Plotting the Primary Axis (App Signups)
color1 = '#1f77b4' # Professional Blue
ax1.set_xlabel('Date (Last 30 Days)', fontsize=12, fontweight='bold')
ax1.set_ylabel('New App Signups', color=color1, fontsize=12, fontweight='bold')
line1 = ax1.plot(df['Date'], df['App_Signups'], color=color1, marker='o', linewidth=2, label='App Signups')
ax1.tick_params(axis='y', labelcolor=color1)
plt.xticks(rotation=45)

# Plotting the Secondary Axis (Premium Upgrades)
ax2 = ax1.twinx()  # Instantiate a second axes that shares the same x-axis
color2 = '#ff7f0e' # Professional Orange
ax2.set_ylabel('Premium Upgrades', color=color2, fontsize=12, fontweight='bold')
line2 = ax2.plot(df['Date'], df['Premium_Upgrades'], color=color2, marker='s', linestyle='--', linewidth=2, label='Premium Upgrades')
ax2.tick_params(axis='y', labelcolor=color2)

# 3. Aesthetics & Legends
plt.title('Executive Summary: Daily App Signups vs. Premium Upgrades', fontsize=16, fontweight='bold', pad=20)

# Combine legends from both axes
lines = line1 + line2
labels = [l.get_label() for l in lines]
ax1.legend(lines, labels, loc='upper left', frameon=True, shadow=True)

# Adjust layout to prevent clipping of labels
fig.tight_layout()

# 4. Save and Output
output_filename = 'dashboard.png'
plt.savefig(output_filename, dpi=300) # Save in high resolution (300 dpi)
print(f"✅ Dashboard successfully generated and saved as '{output_filename}'!")

# Optional: plt.show() will pop up the image window if running locally
# plt.show()