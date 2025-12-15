"""
Typing_Advanced_Tasks_Solutions.py
Module 47 — Typing & Type Hints (Advanced)
Author: Peyman Miyandashti
Year: 2025

This file contains clean and professional solutions
for the advanced typing exercises in this module.
"""

from typing import (
    List, Dict, Tuple,
    Union, Optional, Literal,
    Callable, TypeVar, Generic,
    Protocol, TypedDict
)

# ---------------------------------------------------------------------------
# Rank 1 — Beginner-Advanced
# ---------------------------------------------------------------------------

# Task 1 Solution
def to_string(value: Union[int, str]) -> str:
    return str(value)

print(to_string(10))
print(to_string("Python"))


# Task 2 Solution
def maybe_get_number(flag: bool) -> Optional[int]:
    if flag:
        return 42
    return None

print(maybe_get_number(True))
print(maybe_get_number(False))


# ---------------------------------------------------------------------------
# Rank 2 — Easy
# ---------------------------------------------------------------------------

# Task 3 Solution
def open_mode(mode: Literal["r", "w", "a"]) -> None:
    print("Opening in mode:", mode)

open_mode("r")


# Task 4 Solution
numbers: List[int] = [1, 2, 3]
ages: Dict[str, int] = {"Peyman": 43}
point: Tuple[int, int] = (10, 20)

print(numbers, ages, point)


# ---------------------------------------------------------------------------
# Rank 3 — Intermediate
# ---------------------------------------------------------------------------

# Task 5 Solution
T = TypeVar("T")

def last_item(items: List[T]) -> T:
    return items[-1]

print(last_item([1, 2, 3]))
print(last_item(["a", "b", "c"]))


# Task 6 Solution
class Holder(Generic[T]):
    def __init__(self, value: T):
        self._value = value

    def get(self) -> T:
        return self._value

int_holder = Holder
str_holder = Holder[str]("Hello")

print(int_holder.get())
print(str_holder.get())


# ---------------------------------------------------------------------------
# Rank 4 — Advanced
# ---------------------------------------------------------------------------

# Task 7 Solution
class Processor(Protocol):
    def process(self) -> str:
        ...


class DataProcessor:
    def process(self) -> str:
        return "Processed data"

def run_processor(p: Processor) -> None:
    print(p.process())

run_processor(DataProcessor())


# Task 8 Solution
class UserRecord(TypedDict):
    id: int
    name: str
    active: bool

user: UserRecord = {"id": 1, "name": "Peyman", "active": True}
print(user)


# ---------------------------------------------------------------------------
# Rank 5 — Professional
# ---------------------------------------------------------------------------

# Task 9 Solution
def apply_operation(
    func: Callable[[int, int], int],
    a: int,
    b: int
) -> int:
    return func(a, b)

def multiply(x: int, y: int) -> int:
    return x * y

print(apply_operation(multiply, 3, 4))


# Task 10 Solution
# Advanced typing improves code quality when:
# - APIs are public or shared across teams
# - projects are large and long-lived
# - refactoring safety matters
# - static analysis tools are used
#
# Advanced typing can be overkill when:
# - scripts are small or short-lived
# - logic is obvious and simple
# - type annotations reduce readability
#
# Typing should clarify intent, not obscure it.


# ---------------------------------------------------------------------------
# Final Notes
# ---------------------------------------------------------------------------
# These solutions demonstrate:
# - expressive and precise type annotations
# - correct use of generics and protocols
# - professional design of typed APIs
#
# Next Step:
# Move on to the next module when ready.
