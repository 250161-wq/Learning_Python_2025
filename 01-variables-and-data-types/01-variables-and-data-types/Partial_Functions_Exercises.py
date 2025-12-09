"""
Module 32 — Partial Functions: Practice Exercises
Comprehensive practice with functools.partial, from beginner to
more professional, production-style usage.

In this module I:
- Practice how to use partial functions to "pre-fill" arguments.
- See how partials can simplify repetitive function calls.
- Move from small numeric examples to more realistic use-cases.

Ranking system:
- Rank 1  -> Beginner: create simple partial functions.
- Rank 2  -> Easy: partial with built-in functions and formatting.
- Rank 3  -> Intermediate: partial to configure behavior (logging, math).
- Rank 4  -> Advanced: partial for configuration-style helpers.
- Rank 5  -> Professional: use partial in small, realistic workflows.

Author: Peyman Miyandashti
Date of Birth: 11/11/1983
ID Number: 250161
Year: 2025
"""

from functools import partial
from typing import Callable, Any, Dict, List

# ===========================================================
# Rank 1 — Beginner
# Simple numeric examples with functools.partial
# ===========================================================

print("Rank 1 — Beginner")


def multiply(a: int, b: int) -> int:
    return a * b


times_2 = partial(multiply, 2)  # 'a' is fixed to 2
times_5 = partial(multiply, 5)  # 'a' is fixed to 5

print("2 * 10 =", times_2(10))
print("2 * 7  =", times_2(7))
print("5 * 3  =", times_5(3))
print("5 * 11 =", times_5(11))
print("-" * 50)


# ===========================================================
# Rank 2 — Easy
# Partial with built-ins and reusable text formatters
# ===========================================================

print("Rank 2 — Easy")

# Using partial with the built-in pow() function
square = partial(pow, exp=2)  # type: ignore[call-arg]
cube = partial(pow, exp=3)  # type: ignore[call-arg]

print("Square of 4:", square(4))
print("Cube of 3:", cube(3))

# Partial to create a pre-configured f-string-like template
def build_message(template: str, name: str, score: float) -> str:
    return template.format(name=name, score=score)


exam_template = "Student {name} has a score of {score:.1f}"

default_exam_message = partial(build_message, exam_template)

print(default_exam_message(name="Peyman", score=96.5))
print(default_exam_message(name="Ana", score=88.3))
print("-" * 50)


# ===========================================================
# Rank 3 — Intermediate
# Partial for simple logging and configuration-style helpers
# ===========================================================

print("Rank 3 — Intermediate")


def log(level: str, component: str, message: str) -> None:
    """
    Very simple logger function. In a real project, this might write to
    a file, database, or logging framework.
    """
    print(f"[{level}] [{component}] {message}")


# Create partials for different log levels and components
info_math = partial(log, "INFO", "MATH")
error_math = partial(log, "ERROR", "MATH")
info_auth = partial(log, "INFO", "AUTH")

# Use these partials like specialized logger functions.
info_math("Starting math calculation...")
error_math("Division by zero encountered!")
info_auth("User Peyman logged in successfully.")

print("-" * 50)


# ===========================================================
# Rank 4 — Advanced
# Partial for configuring functions for specific use-cases
# ===========================================================

print("Rank 4 — Advanced")


def send_notification(channel: str, prefix: str, user: str, text: str) -> None:
    """
    Fake notification sender.

    channel: "email", "sms", "push", etc.
    prefix: a tag like "[INFO]", "[ALERT]", etc.
    user:   user name or id
    text:   message body
    """
    full_message = f"{prefix} To {user}: {text}"
    print(f"Sending via {channel.upper()}: {full_message}")


# Create pre-configured notifiers using partial
send_email_info = partial(send_notification, "email", "[INFO]")
send_email_alert = partial(send_notification, "email", "[ALERT]")
send_sms_alert = partial(send_notification, "sms", "[ALERT]")

send_email_info("Peyman", "Your Python progress has been saved.")
send_email_alert("Peyman", "Unusual login activity detected.")
send_sms_alert("Ana", "Your class starts in 15 minutes.")

print("-" * 50)


# ===========================================================
# Rank 5 — Professional
# Small "pipeline" using partial to pre-configure processing steps
# ===========================================================

print("Rank 5 — Professional")


def apply_tax(price: float, tax_rate: float) -> float:
    return price * (1 + tax_rate)


def apply_discount(price: float, discount_rate: float) -> float:
    return price * (1 - discount_rate)


def format_price(currency_symbol: str, price: float) -> str:
    return f"{currency_symbol}{price:,.2f}"


# Create partials that pre-configure the tax, discount, and currency.
apply_mx_tax = partial(apply_tax, tax_rate=0.16)  # Mexico ~16% VAT
apply_student_discount = partial(apply_discount, discount_rate=0.10)
format_mx_price = partial(format_price, "$")  # dollar symbol for simplicity


def build_price_pipeline() -> List[Callable[[Any], Any]]:
    """
    A small pipeline of functions to process prices:
    1. Apply tax.
    2. Apply student discount.
    3. Format with currency symbol.
    """
    # Note: pipeline functions must each accept and return a single value.
    return [
        lambda price: apply_mx_tax(price),
        lambda price: apply_student_discount(price),
        lambda price: format_mx_price(price),
    ]


def process_prices(prices: List[float]) -> List[str]:
    pipeline = build_price_pipeline()
    result: List[str] = []

    for original_price in prices:
        value: Any = original_price
        for step in pipeline:
            value = step(value)
        result.append(value)

    return result


original_prices = [120.0, 250.0, 399.99]
final_prices = process_prices(original_prices)

print("Original prices:", original_prices)
print("Final prices (tax + student discount + formatted):")
for original, final in zip(original_prices, final_prices):
    print(f"  Original: {original:7.2f}  ->  Final: {final}")

print("-" * 50)
