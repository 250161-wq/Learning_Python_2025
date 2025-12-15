"""
Typing_Advanced_Examples.py
Module 47 — Typing & Type Hints (Advanced)
Author: Peyman Miyandashti
Year: 2025

This file contains clear and practical examples
showing advanced typing usage in Python.
"""

from typing import (
    List, Dict, Tuple,
    Union, Optional, Literal,
    Callable, TypeVar, Generic,
    Protocol, TypedDict
)

# ---------------------------------------------------------------------------
# Example 1: Union and Optional
# ---------------------------------------------------------------------------

def to_int(value: Union[str, int]) -> int:
    return int(value)

def find_name(user_id: int) -> Optional[str]:
    if user_id == 1:
        return "Admin"
    return None

print(to_int("42"))
print(find_name(2))


# ---------------------------------------------------------------------------
# Example 2: Literal Types
# ---------------------------------------------------------------------------

def open_file(mode: Literal["r", "w", "a"]) -> None:
    print("Opening file in mode:", mode)

open_file("r")


# ---------------------------------------------------------------------------
# Example 3: Typed Collections
# ---------------------------------------------------------------------------

scores: List[int] = [80, 90, 100]
settings: Dict[str, bool] = {"debug": True}
point: Tuple[int, int] = (5, 10)

print(scores, settings, point)


# ---------------------------------------------------------------------------
# Example 4: Callable
# ---------------------------------------------------------------------------

def add(a: int, b: int) -> int:
    return a + b

def operate(func: Callable[[int, int], int], x: int, y: int) -> int:
    return func(x, y)

print(operate(add, 3, 4))


# ---------------------------------------------------------------------------
# Example 5: TypeVar in Functions
# ---------------------------------------------------------------------------

T = TypeVar("T")

def first(items: List[T]) -> T:
    return items[0]

print(first([1, 2, 3]))
print(first(["a", "b", "c"]))


# ---------------------------------------------------------------------------
# Example 6: Generic Class
# ---------------------------------------------------------------------------

class Container(Generic[T]):
    def __init__(self, value: T):
        self.value = value

    def get(self) -> T:
        return self.value

int_box = Container
str_box = Container[str]("Hello")

print(int_box.get())
print(str_box.get())


# ---------------------------------------------------------------------------
# Example 7: Protocol (Duck Typing)
# ---------------------------------------------------------------------------

class Greeter(Protocol):
    def greet(self) -> str:
        ...


class User:
    def greet(self) -> str:
        return "Hi"

def greet_entity(entity: Greeter) -> None:
    print(entity.greet())

greet_entity(User())


# ---------------------------------------------------------------------------
# Example 8: TypedDict
# ---------------------------------------------------------------------------

class UserInfo(TypedDict):
    name: str
    age: int

user: UserInfo = {"name": "Peyman", "age": 43}
print(user)


# ---------------------------------------------------------------------------
# Example 9: Optional vs Union
# ---------------------------------------------------------------------------

value: Optional[int] = None
value = 10
print(value)


# ---------------------------------------------------------------------------
# Final Notes
# ---------------------------------------------------------------------------
# These examples show how advanced typing:
# - clarifies intent
# - improves static analysis
# - documents APIs
#
# Next Step:
# Continue with Typing_Advanced_Tasks.py
