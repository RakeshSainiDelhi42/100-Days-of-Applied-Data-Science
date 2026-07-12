# Day 3: Advanced Filtering & Aggregation

## 🏢 The Business Scenario
[cite_start]A logistics company wants to know which delivery routes are the least efficient so they can reassign drivers[cite: 231]. 

## 🎯 The Objective
The goal is to mathematically isolate driver/route inefficiency from external factors. 
1. Filter the dataset to only include days where the `Traffic_Condition` was "Light". 
2. [cite_start]Group the data by `Route_ID`[cite: 233]. 
3. [cite_start]Find the route with the highest average delivery time under these light traffic conditions (which indicates a problem with the driver or route, not the traffic)[cite: 233].

## 📊 Data Dictionary
* [cite_start]`Route_ID`: Unique identifier for the delivery route[cite: 232].
* [cite_start]`Driver_Name`: The driver assigned to the route[cite: 232].
* [cite_start]`Traffic_Condition`: The traffic state during the delivery (Light, Moderate, Heavy)[cite: 232].
* [cite_start]`Delivery_Time_Minutes`: The total time taken to complete the delivery[cite: 232].