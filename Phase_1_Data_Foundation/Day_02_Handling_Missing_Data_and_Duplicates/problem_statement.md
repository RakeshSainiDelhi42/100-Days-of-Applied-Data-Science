# Day 2: Handling Missing Data & Duplicates

## 🏢 The Business Scenario
[cite_start]HR handed you an employee roster to calculate average tenure. [cite_start]However, the file was merged from two different legacy systems[cite: 226]. [cite_start]Because of this messy migration, there are duplicate employee records and missing hire dates[cite: 226].

## 🎯 The Objective
1. Ingest the HR dataset.
2. [cite_start]Identify and drop exact duplicate records.
3. [cite_start]Use logical imputation to fill missing hire dates (using the median hire date of their specific department, rather than the entire company).

## 📊 Data Dictionary
* `Employee_ID`: Unique ID for the employee.
* `Name`: Employee's full name.
* `Department`: The department they work in (e.g., IT, Sales, HR).
* `Hire_Date`: The date the employee joined the company.
* `Salary`: The employee's annual salary.