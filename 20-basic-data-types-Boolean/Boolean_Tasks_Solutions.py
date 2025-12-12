"""
Boolean_Tasks_Solutions.py
Module 20 — Basic Data Types: Boolean
Author: Peyman Miyandashti
Year: 2025

Solutions for all boolean practice tasks.
These solutions provide clean, professional boolean expressions for each level.
Use this file only after attempting the tasks honestly.
"""

# ---------------------------------------------------------------------------
# ⭐ RANK 1 — BEGINNER
# ---------------------------------------------------------------------------

# 1.
is_online = True

# 2.
result_2 = (15 > 7)

# 3.
result_3 = ("python" == "Python")

# 4.
temperature = 0
is_freezing = (temperature <= 0)

# 5.
result_5 = (100 != 50)


# ---------------------------------------------------------------------------
# ⭐ RANK 2 — EASY
# ---------------------------------------------------------------------------

# 6.
score = 78
passed = (score >= 60)

# 7.
is_member = True
has_coupon = False
can_get_discount = (is_member or has_coupon)

# 8.
age = 13
is_teenager = (13 <= age <= 19)

# 9.
is_raining = True
has_umbrella = True
both_true = (is_raining and has_umbrella)

# 10.
wallet = 20
price = 25
enough_money = (wallet >= price)


# ---------------------------------------------------------------------------
# ⭐ RANK 3 — INTERMEDIATE
# ---------------------------------------------------------------------------

# 11.
password = "abc123"
is_valid_password = (len(password) >= 6)

# 12.
is_logged = True
last_seen_minutes = 5
is_active = (is_logged and last_seen_minutes < 10)

# 13.
is_clearance = True
discount_percent = 15
on_sale = (is_clearance or discount_percent >= 20)

# 14.
email = "hello@gmail.com"
valid_email = (email != "") and ("@" in email)

# 15.
level = 7
health = 20
is_banned = False
can_enter_dungeon = (level >= 5) and (health > 0) and (not is_banned)


# ---------------------------------------------------------------------------
# ⭐ RANK 4 — ADVANCED
# ---------------------------------------------------------------------------

# 16.
age = 25
income = 18000
credit_score = 700
qualifies_for_loan = (age >= 18) and (income >= 20000) and (credit_score >= 650)

# 17.
email_input = "test@mail.com"
correct_email = "test@mail.com"
password_input = "abc123"
correct_password = "abc123"
login_allowed = (email_input == correct_email) and (password_input == correct_password)

# 18.
has_key = True
battery_level = 30
engine_fault = False
car_can_start = has_key and (battery_level > 20) and (not engine_fault)

# 19.
final_grade = 65
attendance_percent = 92
course_passed = (final_grade >= 70) and (attendance_percent >= 80)

# 20.
is_expired = False
minimum_purchase = 50
cart_total = 45
coupon_valid = (not is_expired) and (minimum_purchase <= cart_total)


# ---------------------------------------------------------------------------
# ⭐ RANK 5 — PROFESSIONAL
# ---------------------------------------------------------------------------

# 21. Access control rule
is_admin = False
is_staff = True
is_banned = False
can_access = (is_admin or is_staff) and (not is_banned)

# 22. File upload rule
file_size_mb = 8
max_size_mb = 10
file_type = "png"
allowed_types = ("png", "jpg", "pdf")
upload_allowed = (file_size_mb <= max_size_mb) and (file_type in allowed_types)

# 23. Free shipping rule
order_total = 85
free_shipping_membership = True
eligible_for_free_shipping = (order_total >= 100) or free_shipping_membership

# 24. Smart-home AC rule
temperature = 29
house_occupied = False
auto_mode = True
turn_on_ac = (temperature >= 28) and (house_occupied or auto_mode)

# 25. Fraud detection rule
amount = 6000
location = "USA"
user_location = "Mexico"
device_trust = False
flag_transaction = (amount > 5000) or ((location != user_location) and (not device_trust))
