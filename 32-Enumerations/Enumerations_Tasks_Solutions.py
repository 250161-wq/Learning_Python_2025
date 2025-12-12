"""
Enumerations_Tasks_Solutions.py
Module 32 — Enumerations
Author: Peyman Miyandashti
Year: 2025

This file contains clean and professional solutions
for the enumeration exercises in this module.
"""

from enum import Enum, IntEnum, auto

# ---------------------------------------------------------------------------
# Rank 1 — Beginner
# ---------------------------------------------------------------------------

# Task 1 Solution
class Day(Enum):
    MONDAY = 1
    TUESDAY = 2
    WEDNESDAY = 3
    THURSDAY = 4
    FRIDAY = 5


# Task 2 Solution
print(Day.MONDAY.name)
print(Day.MONDAY.value)


# ---------------------------------------------------------------------------
# Rank 2 — Easy
# ---------------------------------------------------------------------------

# Task 3 Solution
for day in Day:
    print(day)


# Task 4 Solution
today = Day.FRIDAY

if today == Day.FRIDAY:
    print("Today is Friday")


# ---------------------------------------------------------------------------
# Rank 3 — Intermediate
# ---------------------------------------------------------------------------

# Task 5 Solution
class OrderStatus(Enum):
    PENDING = auto()
    SHIPPED = auto()
    DELIVERED = auto()


# Task 6 Solution
def handle_order(status: OrderStatus):
    if status == OrderStatus.PENDING:
        print("Order is pending")
    elif status == OrderStatus.SHIPPED:
        print("Order has been shipped")
    elif status == OrderStatus.DELIVERED:
        print("Order delivered")


handle_order(OrderStatus.SHIPPED)


# ---------------------------------------------------------------------------
# Rank 4 — Advanced
# ---------------------------------------------------------------------------

# Task 7 Solution
class Level(IntEnum):
    LOW = 1
    MEDIUM = 2
    HIGH = 3


print(Level.HIGH > Level.MEDIUM)


# Task 8 Solution
try:
    level = Level(2)
    print(level)
except ValueError:
    print("Invalid level")


# ---------------------------------------------------------------------------
# Rank 5 — Professional
# ---------------------------------------------------------------------------

# Task 9 Solution
class UserRole(Enum):
    ADMIN = auto()
    EDITOR = auto()
    VIEWER = auto()


def access_control(role: UserRole):
    if role == UserRole.ADMIN:
        print("Full access")
    elif role == UserRole.EDITOR:
        print("Edit access")
    else:
        print("Read-only access")


access_control(UserRole.ADMIN)


# Task 10 Solution
class AppMode(Enum):
    DEVELOPMENT = "dev"
    TESTING = "test"
    PRODUCTION = "prod"


def start_app(mode: AppMode):
    if mode == AppMode.DEVELOPMENT:
        print("Starting in development mode")
    elif mode == AppMode.TESTING:
        print("Starting in testing mode")
    elif mode == AppMode.PRODUCTION:
        print("Starting in production mode")


start_app(AppMode.PRODUCTION)


# ---------------------------------------------------------------------------
# Final Notes
# ---------------------------------------------------------------------------
# These solutions show how enums replace magic values,
# improve readability, and make code safer.
#
# Next Step:
# Move on to the next module when ready.
