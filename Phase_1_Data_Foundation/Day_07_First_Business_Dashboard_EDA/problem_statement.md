# Day 7: First Business Dashboard (EDA)

## 🏢 The Business Scenario
The CEO wants a high-level visual summary of the company's performance over the last month. Looking at raw CSVs is no longer sufficient; leadership needs to see the trend of daily free app signups compared to paid premium upgrades to understand if the recent marketing push was successful.

## 🎯 The Objective
1. Load the last 30 days of performance data.
2. Create a professional dual-axis line chart.
3. The primary Y-axis should display Daily App Signups.
4. The secondary Y-axis should display Premium Upgrades.
5. Save the output as a `.png` file to be attached in an email to the CEO.

## 📊 Data Dictionary
* `Date`: The date of the record.
* `App_Signups`: The total number of new free users acquired that day.
* `Premium_Upgrades`: The total number of users who paid for a subscription that day.