"""
Module 33 — Decorators: Practice Exercises
Comprehensive practice with Python decorators, from beginner to
more professional, production-style usage.

In this module I:
- Practice how to create and apply function decorators.
- Learn how to use @syntax, *args/**kwargs, and decorator arguments.
- Combine multiple decorators for logging, validation, and timing.
- See realistic mini-workflows that decorators can simplify.

Ranking system:
- Rank 1  -> Beginner: basic decorator structure and @syntax.
- Rank 2  -> Easy: decorators with *args/**kwargs and metadata.
- Rank 3  -> Intermediate: decorators with configuration/arguments.
- Rank 4  -> Advanced: stacking decorators and class-based decorators.
- Rank 5  -> Professional: realistic decorator-based "workflow" patterns.

Author: Peyman Miyandashti
Date of Birth: 11/11/1983
ID Number: 250161
Year: 2025
"""

from __future__ import annotations

from functools import wraps, lru_cache
from typing import Any, Callable, Dict, List, Optional, Tuple
import time

# Type alias for decorator that wraps a callable
Decorator = Callable[[Callable[..., Any]], Callable[..., Any]]


# ===========================================================
# Rank 1 — Beginner
# Basic decorator structure and @syntax
# ===========================================================

print("Rank 1 — Beginner")


def simple_logger(func: Callable[[], Any]) -> Callable[[], Any]:
    """
    Very basic decorator:
    - Prints a message before and after the function call.
    - Only works with functions that take NO arguments.
    """

    def wrapper() -> Any:
        print(f"[simple_logger] About to call: {func.__name__}")
        result = func()
        print(f"[simple_logger] Finished calling: {func.__name__}")
        return result

    return wrapper


@simple_logger
def say_hello() -> None:
    print("Hello from a decorated function!")


@simple_logger
def say_goodbye() -> None:
    print("Goodbye from a decorated function!")


say_hello()
say_goodbye()
print("-" * 50)


# ===========================================================
# Rank 2 — Easy
# Decorators with *args/**kwargs and preserving metadata
# ===========================================================

print("Rank 2 — Easy")


def debug(func: Callable[..., Any]) -> Callable[..., Any]:
    """
    Slightly more advanced decorator:
    - Works with any arguments using *args and **kwargs.
    - Prints the function name, arguments, and return value.
    - Uses functools.wraps to preserve __name__ and __doc__.
    """

    @wraps(func)
    def wrapper(*args: Any, **kwargs: Any) -> Any:
        print(f"[debug] Calling {func.__name__}(" f"args={args}, kwargs={kwargs})")
        result = func(*args, **kwargs)
        print(f"[debug] {func.__name__} returned: {result!r}")
        return result

    return wrapper


@debug
def add(a: int, b: int) -> int:
    """Add two integers."""
    return a + b


@debug
def format_student(name: str, grade: float, passed: bool = True) -> str:
    """Return a simple formatted string about a student."""
    status = "PASSED" if passed else "FAILED"
    return f"Student {name} got {grade:.1f} and {status}."


add(10, 20)
format_student("Peyman", 9.5)
format_student("Ana", 7.2, passed=False)
print(f"Function name preserved by @wraps: {format_student.__name__}")
print("-" * 50)


# ===========================================================
# Rank 3 — Intermediate
# Decorators with configuration / arguments
# ===========================================================

print("Rank 3 — Intermediate")


def log_with_level(level: str) -> Decorator:
    """
    Decorator FACTORY (decorator with arguments).

    Usage:
        @log_with_level("INFO")
        def my_func(...):
            ...
    """

    def decorator(func: Callable[..., Any]) -> Callable[..., Any]:
        @wraps(func)
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            print(f"[{level}] {func.__name__} called with args={args}, kwargs={kwargs}")
            result = func(*args, **kwargs)
            print(f"[{level}] {func.__name__} returned {result!r}")
            return result

        return wrapper

    return decorator


@log_with_level("INFO")
def multiply(a: int, b: int) -> int:
    return a * b


@log_with_level("WARNING")
def divide(a: float, b: float) -> float:
    if b == 0:
        print("[WARNING] Division by zero encountered!")
        return float("inf")
    return a / b


# Registry example: decorator used to register functions
COMMAND_REGISTRY: Dict[str, Callable[..., Any]] = {}


def register_command(name: str) -> Decorator:
    """
    Decorator that registers functions in a global COMMAND_REGISTRY.
    """

    def decorator(func: Callable[..., Any]) -> Callable[..., Any]:
        COMMAND_REGISTRY[name] = func
        print(f"[register_command] Registered '{name}' -> {func.__name__}")
        return func

    return decorator


@register_command("greet")
def command_greet(user: str) -> str:
    return f"Hello, {user}!"


@register_command("square")
def command_square(x: int) -> int:
    return x * x


# Use the decorated functions
multiply(6, 7)
divide(10, 2)
divide(10, 0)

print("[Rank 3] Available commands in registry:")
for command_name, command_func in COMMAND_REGISTRY.items():
    print(f"  - {command_name}: {command_func.__name__}")

print("-" * 50)


# ===========================================================
# Rank 4 — Advanced
# Stacking decorators and class-based decorators
# ===========================================================

print("Rank 4 — Advanced")


def timing(func: Callable[..., Any]) -> Callable[..., Any]:
    """
    Decorator that measures how long a function takes to run.
    """

    @wraps(func)
    def wrapper(*args: Any, **kwargs: Any) -> Any:
        start = time.perf_counter()
        result = func(*args, **kwargs)
        end = time.perf_counter()
        elapsed_ms = (end - start) * 1000
        print(f"[timing] {func.__name__} took {elapsed_ms:.2f} ms")
        return result

    return wrapper


def require_positive_arguments(func: Callable[..., Any]) -> Callable[..., Any]:
    """
    Decorator that ensures all numeric arguments are positive.
    If a negative number is found, it raises a ValueError.
    """

    @wraps(func)
    def wrapper(*args: Any, **kwargs: Any) -> Any:
        for value in list(args) + list(kwargs.values()):
            if isinstance(value, (int, float)) and value < 0:
                raise ValueError(
                    f"[require_positive_arguments] Negative value: {value!r}"
                )
        return func(*args, **kwargs)

    return wrapper


@timing
@require_positive_arguments
def slow_sum(numbers: List[int]) -> int:
    """
    Sum a list of positive integers with a tiny artificial delay
    to make the timing decorator easier to see.
    """
    total = 0
    for n in numbers:
        time.sleep(0.01)  # simulate a slow operation
        total += n
    return total


# Class-based decorator example
class call_counter:
    """
    Class-based decorator that counts how many times a function is called.
    """

    def __init__(self, func: Callable[..., Any]) -> None:
        wraps(func)(self)
        self.func = func
        self.count = 0

    def __call__(self, *args: Any, **kwargs: Any) -> Any:
        self.count += 1
        print(f"[call_counter] {self.func.__name__} has been called {self.count} times")
        return self.func(*args, **kwargs)


@call_counter
def greet_user(user: str) -> None:
    print(f"Welcome, {user}!")


# Use stacked and class-based decorators
total_sum = slow_sum([1, 2, 3, 4, 5])
print("slow_sum result:", total_sum)

greet_user("Peyman")
greet_user("Ana")
greet_user("Luis")

print("-" * 50)


# ===========================================================
# Rank 5 — Professional
# Realistic decorator-based workflow (validation, caching, timing)
# ===========================================================

print("Rank 5 — Professional")


def validate_student_data(func: Callable[..., Any]) -> Callable[..., Any]:
    """
    Decorator to validate student data before saving or processing.
    Expects:
        - name: non-empty string
        - score: 0 <= score <= 100
    """

    @wraps(func)
    def wrapper(name: str, score: float, **kwargs: Any) -> Any:
        if not isinstance(name, str) or not name.strip():
            raise ValueError("[validate_student_data] Invalid name.")
        if not (0.0 <= score <= 100.0):
            raise ValueError("[validate_student_data] Score must be 0–100.")
        return func(name, score, **kwargs)

    return wrapper


def audit(action: str) -> Decorator:
    """
    Decorator factory to add simple audit logging.
    """

    def decorator(func: Callable[..., Any]) -> Callable[..., Any]:
        @wraps(func)
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            print(f"[audit:{action}] About to call {func.__name__}")
            result = func(*args, **kwargs)
            print(f"[audit:{action}] Finished calling {func.__name__}")
            return result

        return wrapper

    return decorator


@audit("save_student")
@validate_student_data
def save_student_record(
    name: str,
    score: float,
    storage: Dict[str, float],
) -> None:
    """
    Save or update a student's score in the storage dictionary.
    """
    storage[name] = score
    print(f"Saved record -> {name}: {score}")


@timing
@lru_cache(maxsize=128)
def compute_class_average(scores: Tuple[float, ...]) -> float:
    """
    Compute the average of a sequence of scores.
    Uses lru_cache to avoid recomputation for the same inputs.
    """
    # Simulate an expensive computation
    time.sleep(0.05)
    return sum(scores) / len(scores) if scores else 0.0


def run_student_workflow() -> None:
    """
    Mini-workflow:

    1. Save some student records (with validation + audit).
    2. Compute an average score (with timing + cache).
    3. Re-compute to show that caching is working.
    """
    storage: Dict[str, float] = {}

    # Step 1 — Save records
    save_student_record("Peyman", 96.0, storage=storage)
    save_student_record("Ana", 88.5, storage=storage)
    save_student_record("Luis", 73.0, storage=storage)

    print("[workflow] Current storage:", storage)

    # Step 2 — Compute class average
    scores_tuple = tuple(storage.values())
    avg1 = compute_class_average(scores_tuple)
    print("[workflow] First average computation:", avg1)

    # Step 3 — Compute again to hit the cache
    avg2 = compute_class_average(scores_tuple)
    print("[workflow] Second average computation (cached):", avg2)


run_student_workflow()

print("-" * 50)
