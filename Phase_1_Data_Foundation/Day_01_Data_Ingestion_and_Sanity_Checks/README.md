# 📊 Day 1: Data Ingestion & Sanity Checks

## 🏢 The Business Scenario
I have just joined a retail company as a Data Analyst. The Database Administrator (DBA) exported last month’s sales data for me to calculate the total gross revenue. 

However, the DBA warned me that the legacy POS (Point of Sale) system glitches occasionally. It has been known to record physically impossible data, such as negative quantities, prices of $0, and dates in the future. 

## 🎯 The Objective
The goal of this task is to prevent corrupted data from skewing the company's financial reporting. The objectives are to:
1. Ingest the raw, messy data using Python.
2. Write automated mathematical and logical sanity checks to flag and remove corrupted rows.
3. Calculate the true, corrected total gross revenue.

## 🗂️ Data Dictionary
| Feature | Data Type | Description |
| :--- | :--- | :--- |
| **Transaction_ID** | `String` | Unique identifier for the sale. |
| **Date** | `Datetime` | The date of the transaction. |
| **Product_Category** | `String` | The department the item belongs to. |
| **Quantity_Sold** | `Integer` | Number of units purchased (Must be > 0). |
| **Price_Per_Unit** | `Float` | The cost of a single unit (Must be > 0). |

## 🛠️ Tools & Libraries Used
* **Python**
* **Pandas** (Data manipulation, boolean filtering, datetime conversion)
* **NumPy** (Used in data generation)

## 🧠 Key Learnings & Takeaways
* **Never Trust Raw Data:** Real-world enterprise databases will always have glitches. Calculating revenue immediately on raw data would have resulted in reporting a mathematically impossible number to stakeholders.
* **Boolean Filtering in Pandas:** Used strict chained conditions `(df['Quantity_Sold'] > 0) & (df['Price_Per_Unit'] > 0) & (df['Date'] <= pd.Timestamp.today())` to programmatically isolate the valid data without using slow `for` loops.
* **Data Accountability:** Successfully identified and stripped out exactly 22 corrupted rows (including `NaN` values, negative quantities, zero-dollar prices, and future dates) before running the final revenue aggregation.

---
*This is Day 1 of my [100 Days of Applied Data Science](../README.md) journey.*