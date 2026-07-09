# 📊 Day 2: Handling Missing Data & Duplicates

## 🏢 The Business Scenario
[cite_start]HR handed over an employee roster to calculate average tenure[cite: 225]. [cite_start]However, the file was merged from two different legacy systems[cite: 226]. [cite_start]Because of this messy migration, there are duplicate employee records and missing hire dates[cite: 788].

## 🎯 The Objective
The goal of this task is to clean the HR roster by:
1. [cite_start]Ingesting the HR dataset[cite: 788].
2. [cite_start]Identifying and dropping exact duplicate records[cite: 788].
3. [cite_start]Using logical imputation to fill missing hire dates by using the median hire date of their specific department, rather than the entire company[cite: 229, 788, 792].

## 🗂️ Data Dictionary
| Feature | Data Type | Description |
| :--- | :--- | :--- |
| **Employee_ID** | `String` | [cite_start]Unique ID for the employee[cite: 788]. |
| **Name** | `String` | [cite_start]Employee's full name[cite: 788]. |
| **Department** | `String` | [cite_start]The department they work in (e.g., IT, Sales, HR)[cite: 788]. |
| **Hire_Date** | `Datetime` | [cite_start]The date the employee joined the company[cite: 788]. |
| **Salary** | `Integer` | [cite_start]The employee's annual salary[cite: 788]. |

## 🛠️ Tools & Libraries Used
* **Python**
* **Pandas** (Data manipulation, dropping duplicates, groupby operations, and targeted imputation)

## 🧠 Key Learnings & Takeaways
* **Targeted Imputation:** Filling missing values using a subset median (e.g., grouping by `Department`) yields a much more accurate and logical replacement than using a dataset-wide median[cite: 229, 792].
* **Handling System Migrations:** Merging legacy systems frequently results in duplicated records; [cite_start]`drop_duplicates()` is essential for establishing a reliable baseline before running analytics[cite: 226, 792]. 

---
*This is Day 2 of my [100 Days of Applied Data Science](../README.md) journey.*