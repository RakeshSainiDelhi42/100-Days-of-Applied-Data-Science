import pandas as pd

# 1. Data Ingestion
print("Loading HR dataset...")
df = pd.read_csv('dataset.csv')
original_row_count = len(df)
print(f"Original Rows: {original_row_count}")

# Convert Hire_Date to datetime objects
df['Hire_Date'] = pd.to_datetime(df['Hire_Date'])

# 2. Dropping Duplicates
df_deduped = df.drop_duplicates()
deduped_row_count = len(df_deduped)
print(f"Duplicates Removed: {original_row_count - deduped_row_count}")

# 3. Handling Missing Data (Departmental Median Imputation)
missing_before = df_deduped['Hire_Date'].isna().sum()
print(f"Missing Hire Dates before imputation: {missing_before}")

# Calculate median hire date per department
# We use transform() to align the department median back to the original index
department_medians = df_deduped.groupby('Department')['Hire_Date'].transform('median')

# Fill NaN values in Hire_Date with the corresponding department median
df_clean = df_deduped.copy()
df_clean['Hire_Date'] = df_clean['Hire_Date'].fillna(department_medians)

missing_after = df_clean['Hire_Date'].isna().sum()

print("\n--- 📊 HR ROSTER CLEANING REPORT ---")
print(f"Total Rows Processed: {original_row_count}")
print(f"Valid Unique Employees: {len(df_clean)}")
print(f"Missing Dates Imputed: {missing_before - missing_after}")
print(f"✅ Data cleaning complete. Final missing values: {missing_after}")