# Day 9: Categorical Feature Engineering

## 🏢 The Business Scenario
A SaaS (Software as a Service) company wants to train a Machine Learning model to predict which free users are most likely to upgrade. The Machine Learning Engineering team needs you to prepare the CRM data. However, the data contains text categories like `Subscription_Tier` and `Acquisition_Channel`. Because ML models only understand math, you must translate these text columns into numbers without losing their meaning.

## 🎯 The Objective
1. **Ordinal Encoding:** Convert `Subscription_Tier` into numerical rankings because there is an inherent mathematical order (Free < Bronze < Silver < Gold).
2. **One-Hot Encoding:** Convert `Acquisition_Channel` into numerical columns. Because there is no mathematical order between "SEO" and "Social Media", you must create binary dummy variables.
3. Drop the original text columns and output a 100% machine-readable dataset.

## 📊 Data Dictionary
* `User_ID`: Unique identifier for the user.
* `Engagement_Score`: A numerical score (1-100) of how active the user is.
* `Subscription_Tier`: The user's current level (Free, Bronze, Silver, Gold).
* `Acquisition_Channel`: How the user found the software (SEO, Social Media, Email, Referral).