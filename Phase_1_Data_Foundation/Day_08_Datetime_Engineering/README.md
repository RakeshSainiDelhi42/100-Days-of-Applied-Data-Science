# 📊 Day 8: Datetime Engineering

## 🏢 The Business Scenario
An e-commerce company wanted to optimize their checkout flow. The Product team needed to calculate the average "Time-to-Conversion"—the exact time elapsed between a user adding an item to their cart and completing the checkout. 

## 🎯 The Objective
1. Convert raw text server logs into Python Datetime objects.
2. Filter out "abandoned carts" (Missing values).
3. Calculate the time difference (Timedelta) for each user.
4. Catch and remove systemic time-glitches (negative timedeltas).
5. Extract the final metric into easily readable minutes to find the average conversion time.

## 🗂️ Data Dictionary
| Feature | Data Type | Description |
| :--- | :--- | :--- |
| **Session_ID** | `String` | Unique identifier for the user's shopping session. |
| **Add_to_Cart_Time** | `Datetime` | The exact timestamp the user added the item. |
| **Checkout_Time** | `Datetime` | The exact timestamp the purchase was finalized. |
| **Time_to_Conversion** | `Timedelta` | Engineered feature representing the difference between checkout and cart addition. |
| **Conversion_Minutes** | `Float` | Engineered feature converting the timedelta into a flat numerical float. |

## 🛠️ Tools & Libraries Used
* **Python**
* **Pandas** (`pd.to_datetime()`, `pd.Timedelta()`, `.dt.total_seconds()`)

## 🧠 Key Learnings & Takeaways
* **The Power of `.dt` accessor:** Just like the `.str` accessor is used for string manipulation, Pandas provides a `.dt` accessor to reach inside Datetime and Timedelta objects. Using `.dt.total_seconds() / 60` safely and accurately translated the time gap into a flat mathematical float suitable for machine learning models.
* **Catching Time Glitches:** Subtracting two dates without verifying chronological order is dangerous. Filtering for `Time_to_Conversion >= pd.Timedelta(seconds=0)` automatically stripped out a rogue server glitch where a checkout seemingly happened *before* an item was added.

---
*This is Day 8 of my [100 Days of Applied Data Science](../README.md) journey.*