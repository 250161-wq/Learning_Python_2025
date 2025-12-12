"""
NoneType_Tasks_Solutions.py
Module 21 — NoneType
Author: Peyman Miyandashti
Year: 2025

Solutions for all NoneType practice tasks.
Use this file only AFTER trying the tasks honestly.
"""


# ---------------------------------------------------------------------------
# ⭐ RANK 1 — BEGINNER
# ---------------------------------------------------------------------------

# 1.
result = None

# 2.
user_age = None
check_user_age = (user_age is None)

# 3.
def empty():
    pass

call_result = empty()
check_empty = (call_result is None)

# 4.
data = None
data_type = type(data)

# 5.
name = ""
check_name_none = (name is None)  # False


# ---------------------------------------------------------------------------
# ⭐ RANK 2 — EASY
# ---------------------------------------------------------------------------

# 6.
temperature = None
if temperature is None:
    print("No temperature data")
else:
    print(temperature)

# 7.
def get_level(user):
    if user == "guest":
        return None
    return "level-up"

guest_level = get_level("guest")
admin_level = get_level("admin")

guest_is_none = (guest_level is None)
admin_is_none = (admin_level is None)

# 8.
email = None
if email is None:
    print("Email missing")
else:
    print("Email provided")

# 9.
def test():
    return 10

def ignore():
    return None

t = test()
i = ignore()

test_is_none = (t is None)
ignore_is_none = (i is None)

# 10.
score = None
if score is None:
    print("No score yet")
else:
    print("Score available")


# ---------------------------------------------------------------------------
# ⭐ RANK 3 — INTERMEDIATE
# ---------------------------------------------------------------------------

# 11.
def find_price(item):
    if item == "apple":
        return 10.0
    return None

price_apple = find_price("apple")
price_banana = find_price("banana")

# 12.
user_status = None
if user_status is None:
    print("Status missing")
else:
    print("Status:", user_status)

# 13.
def search_list(numbers):
    for n in numbers:
        if n > 50:
            return n
    return None

result_1 = search_list([10, 20, 30])
result_2 = search_list([20, 70, 10])

# 14.
user_balance = None
balance_available = (user_balance is not None)

# 15.
def get_discount(level):
    if level == "vip":
        return 0.3
    elif level == "premium":
        return 0.1
    return None

discount = get_discount("regular")

if discount is None:
    print("No discount available")
else:
    print("Discount:", discount)


# ---------------------------------------------------------------------------
# ⭐ RANK 4 — ADVANCED
# ---------------------------------------------------------------------------

# 16.
def send_notification(msg, user=None):
    if user is None:
        print("Broadcast:", msg)
    else:
        print(f"To {user}: {msg}")

send_notification("Hello")
send_notification("Hello", "Peyman")

# 17.
def get_user(id):
    if id == 1:
        return {"name": "Peyman"}
    return None

user = get_user(1)
if user is None:
    print("User not found")
else:
    print("User found")

# 18.
location = None
if location is None:
    print("Location unavailable")
else:
    print(location)

# 19.
def fetch_age(database, key):
    return database.get(key, None)

age_result = fetch_age({"id": 10}, "age")

if age_result is None:
    print("Age not found")
else:
    print("Age:", age_result)

# 20.
def safe_divide(a, b):
    if b == 0:
        return None
    return a / b

division_1 = safe_divide(10, 0)
division_2 = safe_divide(10, 2)


# ---------------------------------------------------------------------------
# ⭐ RANK 5 — PROFESSIONAL
# ---------------------------------------------------------------------------

# 21.
def load_profile(username):
    if not username:
        return None
    return {"username": username, "role": "user"}

profile = load_profile("")
if profile is None:
    print("Profile load failed")
else:
    print("Profile loaded:", profile)

# 22.
def validate_payment(amount):
    if amount is None or amount <= 0:
        return None
    return True

payment_result = validate_payment(None)

if payment_result is True:
    print("Payment OK")
else:
    print("Payment invalid")

# 23.
def next_step(result):
    if result == "done":
        return "done"
    return None

step = next_step(None)

if step is None:
    print("Still processing")
else:
    print("Completed")

# 24.
shipping_cost = None
tax = 3.50

if shipping_cost is None:
    print("Waiting for shipping cost")
else:
    print("Total ready")

# 25.
def get_temperature(sensor):
    if sensor == "fail":
        return None
    return 22.5

temp = get_temperature("fail")

if temp is None:
    print("Sensor error")
else:
    print("Temperature:", temp)
