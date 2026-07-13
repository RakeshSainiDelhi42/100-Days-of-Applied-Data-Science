# Day 8: Datetime Engineering

## 🏢 The Business Scenario
An e-commerce company wants to optimize their checkout process. The Product team needs to know the average "Time-to-Conversion"—exactly how much time elapses between a user adding an item to their cart and successfully completing the checkout. 

## 🎯 The Objective
1. Load the shopping cart logs.
2. Convert the raw text timestamps into Python Datetime objects.
3. Calculate the time difference (Timedelta) for each user.
4. Filter out users who "abandoned" their carts (missing checkout times) and remove any systemic glitches (where checkout time is somehow *before* the add-to-cart time).
5. Calculate the average time to conversion in minutes.

## 📊 Data Dictionary
* `Session_ID`: Unique identifier for the user's shopping session.
* `Add_to_Cart_Time`: The exact timestamp the user added the item.
* `Checkout_Time`: The exact timestamp the purchase was finalized.