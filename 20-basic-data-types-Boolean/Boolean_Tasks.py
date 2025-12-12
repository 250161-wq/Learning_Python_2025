"""
Boolean_Tasks.py
Module 20 — Basic Data Types: Boolean
Author: Peyman Miyandashti
Year: 2025

Practice exercises for mastering boolean logic in Python.
Tasks progress from simple comparisons (Rank 1) to realistic, 
production-style decision logic (Rank 5).

Instructions:
- Try every task BEFORE checking the solutions file.
- Write your answers below each task as comments or Python code.
- Focus on clean, readable boolean expressions.
"""

# ---------------------------------------------------------------------------
# ⭐ RANK 1 — BEGINNER
# Very simple boolean expressions and comparisons.
# ---------------------------------------------------------------------------

# 1. Create a boolean variable called is_online and set it to True.

# 2. Compare two numbers: check if 15 is greater than 7.

# 3. Check if the string "python" is equal to "Python".

# 4. Create a variable temperature = 0 and check if it is freezing (<= 0).

# 5. Check if the number 100 is NOT equal to 50.


# ---------------------------------------------------------------------------
# ⭐ RANK 2 — EASY
# Combining comparisons and logical operators.
# ---------------------------------------------------------------------------

# 6. A student score is 78. Check if the student passed (score >= 60).

# 7. A user has is_member = True and has_coupon = False.
#    Check if they can receive a discount (member OR coupon).

# 8. A person is age = 13. Check if they are a teenager (13–19 range).

# 9. Check if two conditions are both True:
#    is_raining = True
#    has_umbrella = True

# 10. You have:
#       wallet = 20
#       price = 25
#     Check whether the wallet has enough money (>=) to buy the item.


# ---------------------------------------------------------------------------
# ⭐ RANK 3 — INTERMEDIATE
# Multi-step boolean logic.
# ---------------------------------------------------------------------------

# 11. A password must be at least 6 characters long.
#     Check if password = "abc123" is valid.

# 12. A user is considered "active" if:
#       - is_logged = True
#       - AND last_seen_minutes < 10
#     last_seen_minutes = 5
#     Check if the user is active.

# 13. A product is on sale if:
#       is_clearance = True
#       OR discount_percent >= 20
#     discount_percent = 15
#     Check if the product is on sale.

# 14. Determine if this email is valid:
#       - It must not be empty
#       - It must contain "@"
#     email = "hello@gmail.com"

# 15. A player can enter the dungeon if:
#       level >= 5
#       health > 0
#       NOT is_banned
#     level = 7, health = 20, is_banned = False


# ---------------------------------------------------------------------------
# ⭐ RANK 4 — ADVANCED
# Realistic boolean logic with multiple conditions.
# ---------------------------------------------------------------------------

# 16. A user qualifies for a loan if:
#       age >= 18
#       income >= 20000
#       credit_score >= 650
#     age = 25, income = 18000, credit_score = 700
#     Check qualification.

# 17. A website allows login if:
#       correct email AND correct password.
#     email_input = "test@mail.com"
#     correct_email = "test@mail.com"
#     password_input = "abc123"
#     correct_password = "abc123"

# 18. A car can start if:
#       has_key = True
#       battery_level > 20
#       NOT engine_fault
#     battery_level = 30, engine_fault = False

# 19. A student passes the course if:
#       final_grade >= 70
#       AND attendance_percent >= 80
#     final_grade = 65, attendance_percent = 92

# 20. A coupon is valid if:
#       - is_expired = False
#       - AND minimum_purchase <= cart_total
#     minimum_purchase = 50, cart_total = 45


# ---------------------------------------------------------------------------
# ⭐ RANK 5 — PROFESSIONAL
# Small production-style decision systems.
# ---------------------------------------------------------------------------

# 21. Write a boolean expression that checks if a user can access
#     a restricted area:
#       must be admin OR staff
#       must NOT be banned

# 22. Determine if a file upload is allowed:
#       file_size_mb <= max_size_mb
#       AND file_type is acceptable ("png", "jpg", "pdf")

# 23. A delivery is eligible for free shipping if:
#       order_total >= 100
#       OR user has free_shipping_membership

# 24. A smart-home system should turn on the AC if:
#       temperature >= 28
#       AND (house_occupied = True OR auto_mode = True)

# 25. A fraud detection system flags a transaction if:
#       amount > 5000
#       OR (location != user_location AND device_trust = False)
#     Make the boolean expression for this rule.
