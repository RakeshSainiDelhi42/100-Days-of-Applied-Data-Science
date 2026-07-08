# Day 1: Data Ingestion & Sanity Checks

## 🏢 The Business Scenario
You have just joined a retail company as a Data Analyst. The Database Administrator (DBA) exported last month’s sales data for you to calculate the total gross revenue. 

However, the DBA warned you that the legacy POS (Point of Sale) system glitches occasionally. It has been known to record physically impossible data, such as negative quantities, prices of $0, and dates in the future. 

## 🎯 The Objective
1. Ingest the raw data.
2. Write automated sanity checks to flag and remove corrupted rows.
3. Calculate the true, corrected total gross revenue.

## 📊 Data Dictionary
* `Transaction_ID`: Unique identifier for the sale.
* `Date`: The date of the transaction.
* `Product_Category`: The department the item belongs to.
* `Quantity_Sold`: Number of units purchased.
* `Price_Per_Unit`: The cost of a single unit.