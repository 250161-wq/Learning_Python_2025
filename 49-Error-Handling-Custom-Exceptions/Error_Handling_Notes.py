"""
Error_Handling_Notes.py
Module 49 — Error Handling & Custom Exceptions
Author: Peyman Miyandashti
Year: 2025

This module explains professional error handling
and custom exception design in Python.
"""

# ---------------------------------------------------------------------------
# 1. Errors Are Part of Normal Flow
# ---------------------------------------------------------------------------
# Errors should:
# - be expected
# - be meaningful
# - communicate what went wrong
#
# Errors should NOT:
# - hide bugs
# - be silently ignored
# - be used for normal logic


# ---------------------------------------------------------------------------
# 2. Raising Built-in Exceptions
# ---------------------------------------------------------------------------

def withdraw(balance: int, amount: int) -> int:
    if amount > balance:
        raise ValueError("Insufficient funds")
    return balance - amount


# ---------------------------------------------------------------------------
# 3. Catching vs Propagating
# ---------------------------------------------------------------------------
# Catch an exception only if you can:
# - handle it
# - add context
# Otherwise, let it propagate.


# ---------------------------------------------------------------------------
# 4. Custom Exceptions
# ---------------------------------------------------------------------------

class BankError(Exception):
    """Base exception for bank-related errors"""


class InsufficientFundsError(BankError):
    pass


class InvalidAccountError(BankError):
    pass


# ---------------------------------------------------------------------------
# 5. Using Custom Exceptions
# ---------------------------------------------------------------------------

def safe_withdraw(balance: int, amount: int) -> int:
    if amount < 0:
        raise InvalidAccountError("Invalid withdrawal amount")
    if amount > balance:
        raise InsufficientFundsError("Not enough balance")
    return balance - amount


# ---------------------------------------------------------------------------
# 6. Exception Chaining
# ---------------------------------------------------------------------------

def parse_number(value: str) -> int:
    try:
        return int(value)
    except ValueError as exc:
        raise ValueError("Invalid numeric input") from exc


# ---------------------------------------------------------------------------
# 7. finally Block
# ---------------------------------------------------------------------------
# Use finally for cleanup, not logic.

def open_resource():
    try:
        print("Resource opened")
        raise RuntimeError("Failure")
    finally:
        print("Resource closed")


# ---------------------------------------------------------------------------
# 8. Anti-Patterns
# ---------------------------------------------------------------------------
# - bare except
# - catching Exception everywhere
# - printing errors instead of raising
# - using exceptions as control flow


# ---------------------------------------------------------------------------
# 9. Best Practices
# ---------------------------------------------------------------------------
# - create meaningful exception names
# - inherit from Exception
# - document exceptions
# - fail early and clearly


# ---------------------------------------------------------------------------
# Final Notes
# ---------------------------------------------------------------------------
# Professional error handling improves:
# - reliability
# - debuggability
# - user experience
#
# Next Step:
# Continue with Error_Handling_Examples.py
