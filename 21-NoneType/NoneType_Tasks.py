"""
NoneType_Tasks.py
Module 21 — NoneType
Author: Peyman Miyandashti
Year: 2025

Practice exercises for mastering Python's NoneType.
Tasks progress from simple checks (Rank 1) to production-style logic (Rank 5).

Instructions:
- Try every task BEFORE checking the solutions file.
- Write your answers below each task as comments or Python code.
- Focus on clean, Pythonic checks using "is None" and "is not None".
"""

# ---------------------------------------------------------------------------
# ⭐ RANK 1 — BEGINNER
# Very simple tasks working directly with None.
# ---------------------------------------------------------------------------

# 1. Create a variable called result and set it to None.

# 2. Check if the variable user_age = None is actually None.

# 3. Create a function empty() with no return statement.
#    Save the result of calling empty() and check whether it is None.

# 4. Create a variable data = None and print its type.

# 5. A variable name = "" is an empty string.
#    Check if name is None (it should NOT be).


# ---------------------------------------------------------------------------
# ⭐ RANK 2 — EASY
# Simple logic checks involving None.
# ---------------------------------------------------------------------------

# 6. A variable temperature = None.
#    Write an if-statement that prints:
#       "No temperature data" if temperature is None
#       Otherwise print the temperature.

# 7. A function get_level(user) returns None if user == "guest".
#    Call the function twice: with "guest" and with "admin".
#    Check which result is None.

# 8. A variable email = None.
#    Use an if-statement to print:
#       "Email missing" if email is None
#       "Email provided" otherwise.

# 9. A function test() returns 10 and ignore() returns None.
#    Call both and compare results: which one is None?

# 10. Create a variable score = None and check:
#       - If it is None, print "No score yet".
#       - Otherwise print "Score available".


# ---------------------------------------------------------------------------
# ⭐ RANK 3 — INTERMEDIATE
# Multi-step logic with None values.
# ---------------------------------------------------------------------------

# 11. Create a function find_price(item) that:
#       returns 10.0 if item == "apple"
#       returns None otherwise
#     Test the function with "apple" and "banana".

# 12. You have:
#       user_status = None
#     Write logic that prints:
#       "Status missing" if user_status is None
#       Otherwise print the status.

# 13. A function search_list(numbers) returns:
#       - The first number greater than 50
#       - None if no such number exists
#     Test with [10, 20, 30] and with [20, 70, 10].

# 14. A variable user_balance = None.
#     Write a clean boolean expression checking if user_balance is NOT None.

# 15. A function get_discount(level) returns:
#       0.3 for "vip"
#       0.1 for "premium"
#       None otherwise
#     Write logic that prints whether a discount is available.


# ---------------------------------------------------------------------------
# ⭐ RANK 4 — ADVANCED
# Realistic usage of None in optional parameters and decisions.
# ---------------------------------------------------------------------------

# 16. Create a function send_notification(msg, user=None) that:
#       - Prints "Broadcast: msg" if user is None
#       - Prints "To user: msg" otherwise
#     Test with:
#       send_notification("Hello")
#       send_notification("Hello", "Peyman")

# 17. A function get_user(id) returns:
#       a dictionary {"name": "Peyman"} if id == 1
#       None otherwise
#     Write logic that:
#       - Prints "User found" if the function returns data
#       - Prints "User not found" if None is returned.

# 18. A variable location = None represents unknown GPS location.
#     Write logic:
#       If location is None → print "Location unavailable"
#       Otherwise print its value.

# 19. A function fetch_age(database, key) returns None if key doesn’t exist.
#     Use an if-statement to check whether the result is valid.

# 20. Create a function safe_divide(a, b) that:
#       - Returns None if b == 0
#       - Otherwise returns a / b
#     Test with safe_divide(10, 0) and safe_divide(10, 2).


# ---------------------------------------------------------------------------
# ⭐ RANK 5 — PROFESSIONAL
# Production-style decision logic where None represents missing or invalid data.
# ---------------------------------------------------------------------------

# 21. A function load_profile(username) returns:
#       {"username": username, "role": "user"} for valid usernames
#       None if username is empty or None
#     Write logic that checks if a profile loaded successfully.

# 22. A function validate_payment(amount) returns:
#       True for valid amounts
#       None for invalid or missing amounts
#     Write code that:
#       - Prints "Payment OK" if True
#       - Prints "Payment invalid" if None

# 23. A function next_step(result) returns:
#       None if the process is incomplete
#       "done" when finished
#     Write logic printing:
#       "Still processing" if None
#       "Completed" if not None.

# 24. A shipping system uses:
#       shipping_cost = None (no data yet)
#       tax = 3.50
#     Write a condition that prints:
#       "Waiting for shipping cost" if shipping_cost is None
#       "Total ready" otherwise.

# 25. A function get_temperature(sensor) returns:
#       a float (valid temperature)
#       None if sensor fails
#     Write logic that prints:
#       - "Sensor error" if None
#       - "Temperature: value" otherwise.
