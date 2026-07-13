# Day 6: Relational Data (Merges & Joins)

## 🏢 The Business Scenario
You have been granted access to two separate company databases. One holds customer personal demographic information (Age, Location), and the other holds their transactional purchase history. 

## 🎯 The Objective
The marketing team wants to know where to allocate their ad budget. Your goal is to:
1. Load both datasets into memory.
2. Join them together using a common "key" (`User_ID`).
3. Group the customers into age brackets (18-25, 26-35, 36-50, 51+).
4. Calculate the total amount spent by each demographic to see if older demographics spend more money.

## 📊 Data Dictionary
**1. users.csv**
* `User_ID`: Unique identifier for the customer.
* `Age`: The customer's age.
* `Location`: The customer's city.

**2. purchases.csv**
* `Purchase_ID`: Unique identifier for the transaction.
* `User_ID`: The customer who made the purchase (The Foreign Key).
* `Amount_Spent`: The dollar amount of the transaction.