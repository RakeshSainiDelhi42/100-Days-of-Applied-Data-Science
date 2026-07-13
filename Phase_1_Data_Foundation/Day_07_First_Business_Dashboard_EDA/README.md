# 📊 Day 7: First Business Dashboard (EDA)

## 🏢 The Business Scenario
The CEO requested a high-level visual summary of the company's performance over the last month to determine if the recent marketing push was successful. Looking at raw CSVs was no longer sufficient; leadership needed to see the trend of daily free app signups compared to paid premium upgrades.

## 🎯 The Objective
1. Load the last 30 days of performance data.
2. Create a professional dual-axis line chart using Matplotlib and Seaborn.
3. Display Daily App Signups on the primary Y-axis and Premium Upgrades on the secondary Y-axis.
4. Export the visualization as a high-resolution `.png` file.

## 🗂️ Data Dictionary
| Feature | Data Type | Description |
| :--- | :--- | :--- |
| **Date** | `Datetime` | The date of the record (last 30 days). |
| **App_Signups** | `Integer` | The total number of new free users acquired that day. |
| **Premium_Upgrades** | `Integer` | The total number of users who paid for a subscription that day. |

## 🛠️ Tools & Libraries Used
* **Python**
* **Pandas** (Datetime conversion)
* **Matplotlib & Seaborn** (Data visualization, dual-axis plotting, aesthetics)

## 🧠 Key Learnings & Takeaways
* **The Power of `twinx()`:** When comparing two metrics with vastly different scales (e.g., thousands of signups vs. hundreds of upgrades), plotting them on a single standard axis crushes the smaller line. Using Matplotlib's `twinx()` function allows both trends to be analyzed simultaneously on their own scales.
* **Visual Communication:** Saving the plot with high DPI (`dpi=300`) and clear contrasting colors ensures the dashboard is presentation-ready for executive leadership.

---
*This is Day 7 of my [100 Days of Applied Data Science](../README.md) journey.*