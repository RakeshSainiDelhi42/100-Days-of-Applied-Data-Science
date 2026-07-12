# 📊 Day 4: Statistical Outlier Detection

## 🏢 The Business Scenario
A ride-sharing startup is auditing their driver payouts. [cite_start]Some drivers figured out a glitch in the app to charge artificially high fares. 

## 🎯 The Objective
To mathematically isolate the fraudulent charges, I needed to:
1. [cite_start]Calculate the "Price per Mile" to standardize the data across both short and long trips[cite: 238].
2. [cite_start]Apply the **Interquartile Range (IQR)** method to define the upper mathematical bound of a normal fare.
3. Filter out and report the top anomalous rides for review.

## 🗂️ Data Dictionary
| Feature | Data Type | Description |
| :--- | :--- | :--- |
| **Ride_ID** | `String` | [cite_start]Unique identifier for the ride[cite: 237]. |
| **Distance_Miles** | `Float` | [cite_start]Total distance of the trip[cite: 237]. |
| **Fare_Amount** | `Float` | [cite_start]The total amount charged to the rider[cite: 237]. |
| **Price_Per_Mile** | `Float` | Engineered feature used to detect outliers. |

## 🛠️ Tools & Libraries Used
* **Python**
* **Pandas** (Feature engineering, Quantile calculation, Boolean indexing)

## 🧠 Key Learnings & Takeaways
* **Standardizing Metrics First:** Looking only at total `Fare_Amount` is misleading because a $100 fare is normal for a 40-mile trip, but fraudulent for a 2-mile trip. Creating the `Price_Per_Mile` metric solved this.
* **Math Over Guesswork:** Instead of arbitrarily deciding that "$10 per mile" is fraudulent, using the Interquartile Range (IQR) dynamically adapts to the dataset to mathematically flag true statistical outliers.

---
*This is Day 4 of my [100 Days of Applied Data Science](../README.md) journey.*