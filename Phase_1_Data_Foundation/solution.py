import pandas as pd

# 1. Data Ingestion
print("Loading raw social media data...")
df = pd.read_csv('dataset.csv')

# 2. Text Cleaning Pipeline
# - .str.lower(): Converts to lowercase
# - .str.replace(r'[^\w\s]', ''): Uses Regex to remove punctuation (keeps words and spaces)
# - .str.strip(): Removes leading and trailing white spaces
# - .str.replace(r'\s+', ' '): Replaces multiple internal spaces with a single space

df['Clean_Tweet'] = (
    df['Raw_Tweet']
    .str.lower()
    .str.replace(r'[^\w\s]', '', regex=True)
    .str.strip()
    .str.replace(r'\s+', ' ', regex=True)
)

# 3. Keyword Frequency Analysis
positive_keywords = ['loved', 'great', 'awesome', 'good']
negative_keywords = ['terrible', 'worst', 'awful', 'bad']

# Create functions to count keyword hits
def count_positive(text):
    return sum(1 for word in positive_keywords if word in text.split())

def count_negative(text):
    return sum(1 for word in negative_keywords if word in text.split())

# Apply the functions to create new columns
df['Positive_Count'] = df['Clean_Tweet'].apply(count_positive)
df['Negative_Count'] = df['Clean_Tweet'].apply(count_negative)

# 4. Final Output & Reporting
total_positive = df['Positive_Count'].sum()
total_negative = df['Negative_Count'].sum()

print("\n--- 📊 SOCIAL MEDIA SENTIMENT REPORT ---")
print(f"Total Tweets Processed: {len(df)}")
print(f"Positive Keywords Found: {total_positive}")
print(f"Negative Keywords Found: {total_negative}")

# Determine overall sentiment
if total_positive > total_negative:
    print("✅ Overall Sentiment: POSITIVE")
elif total_negative > total_positive:
    print("🚨 Overall Sentiment: NEGATIVE")
else:
    print("⚖️ Overall Sentiment: NEUTRAL")

print("\nSample of Cleaned Data:")
print(df[['Raw_Tweet', 'Clean_Tweet']].head().to_string(index=False))