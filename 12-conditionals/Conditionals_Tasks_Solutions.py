"""
Module 12 — Conditionals (if, elif, else)
Practice Task Solutions

This file contains clean and professional solutions to all exercises in
Conditionals_Tasks.py. Many tasks can be solved in multiple ways; these
solutions show clear, readable approaches appropriate for beginners and
intermediate learners.

Only read this file after attempting the tasks yourself.
"""

# ---------------------------------------------------------------------------
# Rank 1 — Beginner
# ---------------------------------------------------------------------------

# Task 1.1
number = 5
if number > 0:
    print("Positive")

# Task 1.2
password = "python123"
if password == "python123":
    print("Access granted")
else:
    print("Access denied")

# Task 1.3
age = 18
if age >= 18:
    print("Adult")
else:
    print("Minor")


# ---------------------------------------------------------------------------
# Rank 2 — Easy
# ---------------------------------------------------------------------------

# Task 2.1
score = 78
if score >= 90:
    print("A")
elif score >= 80:
    print("B")
elif score >= 70:
    print("C")
else:
    print("D or below")

# Task 2.2
temperature = 15
if temperature < 0:
    print("Freezing")
elif temperature < 10:
    print("Very cold")
elif temperature < 20:
    print("Cold")
else:
    print("Warm")

# Task 2.3
color = "red"
if color in ["red", "blue", "yellow"]:
    print("Primary color")
elif color in ["green", "purple", "orange"]:
    print("Secondary color")
else:
    print("Unknown color")


# ---------------------------------------------------------------------------
# Rank 3 — Intermediate
# ---------------------------------------------------------------------------

# Task 3.1
age = 22
user_is_member = True
if age >= 18 and user_is_member:
    print("Entry allowed")
else:
    print("Blocked")

# Task 3.2
number = 12
if number > 0 and number != 10:
    print("Valid")
else:
    print("Invalid")

# Task 3.3
username = "admin"
password = "1234"
if username == "admin" and password == "1234":
    print("Login successful")
else:
    print("Invalid credentials")


# ---------------------------------------------------------------------------
# Rank 4 — Advanced
# ---------------------------------------------------------------------------

# Task 4.1
user_role = "admin"
account_active = True

if user_role == "admin":
    if account_active:
        print("Admin panel opened")
    else:
        print("Account inactive")
else:
    print("Standard user")

# Task 4.2
user_input = 5  # example value
if user_input < 0:
    print("Error: negative")
elif user_input == 0:
    print("Zero")
else:
    print("Positive number")

# Task 4.3
purchase = 120
customer_is_vip = True

if purchase >= 100:
    discount = 20
elif purchase >= 50:
    discount = 10
else:
    discount = 0

if customer_is_vip:
    discount += 5

print("Final discount:", discount)


# ---------------------------------------------------------------------------
# Rank 5 — Professional
# ---------------------------------------------------------------------------

# Task 5.1
weight = 3
express_shipping = True

if weight < 1:
    cost = 5
elif weight < 5:
    cost = 10
elif weight < 20:
    cost = 20
else:
    cost = 50

if express_shipping:
    cost += 15

print("Shipping cost:", cost)

# Task 5.2
grade = 75
attendance = 85

if grade >= 70 and attendance >= 80:
    print("Pass")
elif grade >= 70 and attendance < 80:
    print("Fail due to attendance")
elif grade < 70 and attendance >= 80:
    print("Fail due to grade")
else:
    print("Fail")

# Task 5.3
menu_choice = 2
if menu_choice == 1:
    print("Start")
elif menu_choice == 2:
    print("Settings")
elif menu_choice == 3:
    print("Exit")
else:
    print("Invalid option")


# End of Solutions
