"""
Module 3 — Functions: Practical Examples
----------------------------------------

This file contains small, focused examples demonstrating how to define,
call, and structure Python functions in a professional way.

Concepts covered:
- Basic function definitions
- Parameters and arguments
- Default parameters
- Return values
- Pure functions
- Multiple return values
- *args and **kwargs
- Realistic patterns used in production code
"""


# ---------------------------------------------------------------------------
# Rank 1 — Beginner Examples
# ---------------------------------------------------------------------------

def example_1_basic_greeting() -> None:
    """Print a simple greeting. No parameters, no return."""
    print("Hello from a basic function!")


def example_2_greet_person(name: str) -> None:
    """Greet a specific person using a parameter."""
    print(f"Hello, {name}!")


def example_3_add_two_numbers(a: int, b: int) -> None:
    """Add two numbers and print the result."""
    print(f"{a} + {b} = {a + b}")


# ---------------------------------------------------------------------------
# Rank 2 — Easy Examples
# ---------------------------------------------------------------------------

def example_4_multiply(a: float, b: float) -> float:
    """Return the product of two values."""
    return a * b


def example_5_welcome_user(username: str = "Guest") -> None:
    """Use a default parameter when no username is provided."""
    print(f"Welcome, {username}!")


def example_6_format_full_name(first: str, last: str) -> str:
    """Return a formatted full name."""
    return f"{first} {last}"


# ---------------------------------------------------------------------------
# Rank 3 — Intermediate Examples
# ---------------------------------------------------------------------------

def example_7_average(values: list[float]) -> float:
    """
    Return the average of a list of values.
    Demonstrates return statements and simple validation.
    """
    if not values:
        return 0.0

    total = 0.0
    for v in values:
        total += v
    return total / len(values)


def example_8_divmod_custom(x: int, y: int) -> tuple[int, int]:
    """Return quotient and remainder as multiple return values."""
    quotient = x // y
    remainder = x % y
    return quotient, remainder


def example_9_is_even(n: int) -> bool:
    """Return True if the number is even."""
    return n % 2 == 0


# ---------------------------------------------------------------------------
# Rank 4 — Advanced Examples
# ---------------------------------------------------------------------------

def example_10_collect_positive_numbers(numbers: list[int]) -> list[int]:
    """
    Return a new list containing only positive numbers.
    Demonstrates transforming data using a loop inside a function.
    """
    result = []
    for n in numbers:
        if n > 0:
            result.append(n)
    return result


def example_11_build_user_profile(name: str, age: int, country: str = "Unknown") -> dict:
    """
    Return a user profile as a dictionary.

    This pattern appears in real applications where functions prepare
    structured data.
    """
    return {
        "name": name,
        "age": age,
        "country": country,
    }


def example_12_power_of_all(values: list[int], power: int) -> list[int]:
    """
    Raise each number in the list to a specified power.
    Demonstrates transformation and return of computed results.
    """
    result = []
    for v in values:
        result.append(v ** power)
    return result


# ---------------------------------------------------------------------------
# Rank 5 — Professional Examples
# ---------------------------------------------------------------------------

def example_13_sum_all(*args: float) -> float:
    """
    Accept any number of numeric arguments and return their total.
    Demonstrates the use of *args.
    """
    total = 0
    for num in args:
        total += num
    return total


def example_14_debug_message(**kwargs) -> None:
    """
    Demonstrates **kwargs for flexible keyword arguments.

    Example:
        example_14_debug_message(event="login", user="Peyman")
    """
    print("Debug Info:")
    for key, value in kwargs.items():
        print(f"  {key}: {value}")


def example_15_filter_users(users: list[dict], *, active_only: bool = True) -> list[dict]:
    """
    Return only active users from a list of user dictionaries.

    This example demonstrates:
    - Keyword-only parameters (*)
    - Filtering with clear business logic
    """

    result = []
    for user in users:
        if active_only and not user.get("active", False):
            continue
        result.append(user)

    return result


# ---------------------------------------------------------------------------
# Demonstration Section (manual execution)
# ---------------------------------------------------------------------------

def main():
    print("\n--- Rank 1 Examples ---")
    example_1_basic_greeting()
    example_2_greet_person("Peyman")
    example_3_add_two_numbers(3, 7)

    print("\n--- Rank 2 Examples ---")
    print("Multiply:", example_4_multiply(3, 4))
    example_5_welcome_user()
    print(example_6_format_full_name("Arlette", "Chong"))

    print("\n--- Rank 3 Examples ---")
    print("Average:", example_7_average([10, 20, 30]))
    print("divmod:", example_8_divmod_custom(17, 5))
    print("Is 8 even?", example_9_is_even(8))

    print("\n--- Rank 4 Examples ---")
    print(example_10_collect_positive_numbers([-3, 2, 7, -1, 4]))
    print(example_11_build_user_profile("Peyman", 43, "Mexico"))

    print("\n--- Rank 5 Examples ---")
    print("Sum all:", example_13_sum_all(1, 2, 3, 4, 5))
    example_14_debug_message(event="login", user="Nova")
    print(example_15_filter_users(
        [
            {"name": "Alex", "active": True},
            {"name": "Sara", "active": False},
            {"name": "Peyman", "active": True},
        ],
        active_only=True
    ))


if __name__ == "__main__":
    main()
