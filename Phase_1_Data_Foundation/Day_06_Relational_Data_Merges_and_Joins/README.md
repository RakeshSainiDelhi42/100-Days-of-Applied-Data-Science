# 📊 Day 6: Relational Data (Merges & Joins)

## 🏢 The Business Scenario
The marketing team needed to know where to allocate their advertising budget. However, customer demographic data (Age, Location) and transactional data (Purchase amounts) lived in two entirely separate databases. 

## 🎯 The Objective
1. Load both datasets into memory.
2. Perform a Relational Join using a common primary/foreign key (`User_ID`).
3. Engineer a new categorical feature by grouping exact ages into marketing Age Brackets (18-25, 26-35, 36-50, 51+).
4. Aggregate total revenue by demographic to identify the most valuable customer base.

## 🛠️ Tools & Libraries Used
* **Python**
* **Pandas** * `pd.merge()` for SQL-style Left Joins.
  * `pd.cut()` for numerical binning/segmentation.
  * `.groupby()` for aggregation.

## 🧠 Key Learnings & Takeaways
* **SQL Logic in Python:** Using `pd.merge(..., how='left')` mimics a SQL `LEFT JOIN`. This ensures that every single purchase is retained in the final dataframe, even if a user's demographic data was somehow missing.
* **Continuous to Categorical:** Raw ages (e.g., 23, 45, 61) are difficult to group for high-level marketing reports. Using `pd.cut()` quickly translates continuous numerical data into discrete categorical bins for cleaner aggregation.

---
*This is Day 6 of my [100 Days of Applied Data Science](../README.md) journey.*