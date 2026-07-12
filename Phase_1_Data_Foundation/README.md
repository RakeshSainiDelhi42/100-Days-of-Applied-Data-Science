# 📊 Day 5: String Manipulation & Text Cleaning

## 🏢 The Business Scenario
The marketing team scraped Twitter for customer mentions of a new product. However, the raw data was a complete mess of uppercase letters, lowercase letters, special characters, and inconsistent spacing, rendering it useless for standard sentiment analysis.

## 🎯 The Objective
1. Build a text-cleaning pipeline to sanitize the raw scraped data.
2. Standardize the text by converting it to lowercase, stripping out all punctuation, and normalizing whitespace.
3. Perform a basic keyword frequency analysis to determine if the overall social media sentiment was positive or negative.

## 🗂️ Data Dictionary
| Feature | Data Type | Description |
| :--- | :--- | :--- |
| **Tweet_ID** | `String` | Unique identifier for the scraped tweet. |
| **Raw_Tweet** | `String` | The uncleaned, messy text scraped from social media. |
| **Clean_Tweet** | `String` | The engineered text formatted for machine reading. |
| **Positive_Count** | `Integer` | Number of positive keywords found in the tweet. |
| **Negative_Count** | `Integer` | Number of negative keywords found in the tweet. |

## 🛠️ Tools & Libraries Used
* **Python**
* **Pandas** (String methods chaining: `.str.lower()`, `.str.strip()`)
* **Regex** (Regular Expressions for punctuation and space removal)

## 🧠 Key Learnings & Takeaways
* **Regex is Essential:** Standard string methods are not enough for highly messy data. Using `r'[^\w\s]'` efficiently strips out all rogue punctuation like `@`, `!`, and `?` in a single line of code.
* **Method Chaining:** Grouping Pandas `.str` operations together creates a highly readable, memory-efficient pipeline compared to overwriting the column multiple times.

---
*This is Day 5 of my [100 Days of Applied Data Science](../README.md) journey.*