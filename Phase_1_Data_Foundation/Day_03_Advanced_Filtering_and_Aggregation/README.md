# 📊 Day 3: Advanced Filtering & Aggregation

## 🏢 The Business Scenario
[cite_start]A logistics company wants to know which delivery routes are the least efficient so they can reassign drivers[cite: 231].

## 🎯 The Objective
To isolate driver/route inefficiency from external factors, I needed to:
1. [cite_start]Filter the dataset to isolate days with "Light" traffic[cite: 233].
2. [cite_start]Group the data by `Route_ID`[cite: 233].
3. [cite_start]Calculate the average delivery time to identify the most inefficient route and driver combo under optimal conditions[cite: 233].

## 🗂️ Data Dictionary
| Feature | Data Type | Description |
| :--- | :--- | :--- |
| **Route_ID** | `String` | [cite_start]Unique identifier for the delivery route[cite: 232]. |
| **Driver_Name** | `String` | [cite_start]The driver assigned to the route[cite: 232]. |
| **Traffic_Condition** | `String` | [cite_start]The traffic state during the delivery (Light, Moderate, Heavy)[cite: 232]. |
| **Delivery_Time_Minutes**| `Integer`| [cite_start]The total time taken to complete the delivery[cite: 232]. |

## 🛠️ Tools & Libraries Used
* **Python**
* **Pandas** (Boolean indexing, GroupBy operations, aggregation methods, and sorting)

## 🧠 Key Learnings & Takeaways
* **Contextual Filtering:** Running a `.mean()` on the entire dataset would have skewed the results, as a great driver stuck in Heavy traffic would appear inefficient. Filtering for `Traffic_Condition == 'Light'` isolated the true performance metric[cite: 233].
* **Chaining Pandas Methods:** Successfully used chained operations (`.groupby().mean().reset_index().sort_values()`) to transform raw operational data into a clean, actionable business report in a single block of code.

---
*This is Day 3 of my [100 Days of Applied Data Science](../README.md) journey.*