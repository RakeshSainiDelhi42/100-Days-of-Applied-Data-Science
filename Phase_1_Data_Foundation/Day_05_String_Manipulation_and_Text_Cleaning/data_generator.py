import pandas as pd
import random

# Set up raw data components
positive_phrases = ["LOved the PROduct!!!", "such a great experience...", "AWESOME service @support", "really good, highly recommend!"]
negative_phrases = ["terrible service... @support", "Worst product ever!!! #bad", "awful, just AWFUL.", "bad quality... do not buy!"]
neutral_phrases = ["just bought this today.", "it is okay I guess??", "shipping took 3 days.", "Product arrived  yesterday!!!"]

all_phrases = positive_phrases + negative_phrases + neutral_phrases
n_rows = 50

# Generate messy data
data = {
    'Tweet_ID': [f"TWT_{i:03d}" for i in range(1, n_rows + 1)],
    'Raw_Tweet': []
}

for _ in range(n_rows):
    phrase = random.choice(all_phrases)
    # Inject extra random spaces and symbols to make it extra messy
    messy_phrase = f"   {phrase}  " + random.choice(["!?!", "...", "***", "   "])
    data['Raw_Tweet'].append(messy_phrase)

df = pd.DataFrame(data)

# Save to CSV
df.to_csv('dataset.csv', index=False)
print("✅ dataset.csv successfully generated with messy text data!")