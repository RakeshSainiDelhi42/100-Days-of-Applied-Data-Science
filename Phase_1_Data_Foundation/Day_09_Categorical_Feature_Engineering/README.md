# 📊 Day 9: Categorical Feature Engineering

## 🏢 The Business Scenario
A SaaS company wanted to train a Machine Learning model to predict which free users are most likely to upgrade. The Machine Learning Engineering team required the CRM data, but because ML models only understand mathematics, the text-based categorical columns needed to be engineered into numerical formats without losing their underlying meaning.

## 🎯 The Objective
1. **Ordinal Encoding:** Convert hierarchical text data (`Subscription_Tier`) into mathematical rankings.
2. **One-Hot Encoding:** Convert nominal text data (`Acquisition_Channel`) into binary dummy variables.
3. Output a 100% machine-readable, numerical dataset.

## 🛠️ Tools & Libraries Used
* **Python**
* **Pandas** (`.map()` for Ordinal Encoding, `pd.get_dummies()` for One-Hot Encoding)

## 🧠 Key Learnings & Takeaways
* **Ordinal vs. Nominal Data:** You cannot simply assign random numbers to categories. Because 'Gold' is strictly higher than 'Bronze', it requires **Ordinal Encoding** (0, 1, 2, 3). Because 'SEO' is not mathematically greater than 'Social Media', assigning them 1 and 2 would confuse the model. They require **One-Hot Encoding** (creating new binary columns).
* **The Dummy Variable Trap:** When using `pd.get_dummies()`, I utilized `drop_first=True`. This drops one of the generated binary columns to prevent multicollinearity (where independent variables are highly correlated), which can break certain models like Linear and Logistic Regression.

---
*This is Day 9 of my [100 Days of Applied Data Science](../README.md) journey.*