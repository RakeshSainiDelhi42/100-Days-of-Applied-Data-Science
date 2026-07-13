# Day 5: String Manipulation & Text Cleaning

## 🏢 The Business Scenario
The marketing team scraped Twitter for customer mentions of your new product. However, the raw data is a complete mess of uppercase letters, lowercase letters, special characters, and inconsistent spacing. They need a clean dataset to run sentiment analysis.

## 🎯 The Objective
1. Ingest the messy text dataset.
2. Build a text-cleaning pipeline to convert everything to lowercase, remove all punctuation/special characters, and strip out extra whitespace.
3. Perform a basic keyword frequency analysis to count how many times positive keywords (like "loved") appear compared to negative keywords (like "terrible").

## 📊 Data Dictionary
* `Tweet_ID`: Unique identifier for the scraped tweet.
* `Raw_Tweet`: The uncleaned, messy text scraped from social media.