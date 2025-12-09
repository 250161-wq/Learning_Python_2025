"""
Module 42 — Callable Objects: Practice Exercises
Comprehensive practice with Python callable objects, from beginner
to more professional, production-style usage.

In this module I:
- Use the built-in callable() function to test whether something is callable.
- Implement classes with a __call__ method so instances behave like functions.
- Build stateful callable objects that remember previous calls.
- Compare closures (inner functions) with callable classes.
- Use callable objects for simple decorators and small "action" systems.

Ranking system:
- Rank 1  -> Beginner: basic callable() checks and __call__.
- Rank 2  -> Easy: simple stateful callable objects.
- Rank 3  -> Intermediate: comparing closures vs callable classes.
- Rank 4  -> Advanced: callable objects as configurable processors/decorators.
- Rank 5  -> Professional: mini "command" system using callable objects.

Author: Peyman Miyandashti
Date of Birth: 11/11/1983
ID Number: 250161
Year: 2025
"""

from __future__ import annotations
from typing import Any, Callable, Dict, List


# ===========================================================
# Rank 1 — Beginner
# callable() and simple __call__ implementation
# ===========================================================

print("Rank 1 — Beginner")


def add(a: int, b: int) -> int:
    return a + b


class Greeter:
    """
    A simple callable class: instances behave like "greet" functions.
    """

    def __init__(self, greeting: str) -> None:
        self.greeting = greeting

    def __call__(self, name: str) -> str:
        return f"{self.greeting}, {name}!"


greet_hello = Greeter("Hello")
greet_buenos = Greeter("Buenos días")

items = [42, "text", add, greet_hello, Greeter]

for item in items:
    print(f"{item!r:>25} -> callable? {callable(item)}")

print("Calling add(2, 3):", add(2, 3))
print("Calling greet_hello('Peyman'):", greet_hello("Peyman"))
print("Calling greet_buenos('Ana'):", greet_buenos("Ana"))
print("-" * 50)


# ===========================================================
# Rank 2 — Easy
# Stateful callable objects (remembering how many times they were called)
# ===========================================================

print("Rank 2 — Easy")


class CallCounter:
    """
    A callable object that counts how many times it was called.
    """

    def __init__(self, label: str = "counter") -> None:
        self.label = label
        self.calls = 0

    def __call__(self) -> int:
        self.calls += 1
        print(f"{self.label!r} has been called {self.calls} times")
        return self.calls


class Adder:
    """
    A callable object that adds a fixed value and tracks total usage.
    """

    def __init__(self, increment: int) -> None:
        self.increment = increment
        self.calls = 0

    def __call__(self, value: int) -> int:
        self.calls += 1
        result = value + self.increment
        print(
            f"Adder(+{self.increment}) call #{self.calls}: "
            f"{value} -> {result}"
        )
        return result


click_counter = CallCounter("button_clicks")
click_counter()
click_counter()
click_counter()

adder_5 = Adder(5)
adder_5(10)
adder_5(20)
adder_5(100)
print("-" * 50)


# ===========================================================
# Rank 3 — Intermediate
# Closures vs callable classes
# ===========================================================

print("Rank 3 — Intermediate")


def make_multiplier_closure(factor: int) -> Callable[[int], int]:
    """
    Returns a function (closure) that multiplies by factor.
    """

    def multiplier(x: int) -> int:
        return x * factor

    return multiplier


class MultiplierCallable:
    """
    Callable class version of a multiplier.
    """

    def __init__(self, factor: int) -> None:
        self.factor = factor

    def __call__(self, x: int) -> int:
        return x * self.factor

    def __repr__(self) -> str:
        return f"MultiplierCallable(factor={self.factor})"


times2_closure = make_multiplier_closure(2)
times3_closure = make_multiplier_closure(3)

times2_callable = MultiplierCallable(2)
times3_callable = MultiplierCallable(3)

values = [1, 5, 10]

print("Using closures:")
for v in values:
    print(f"  {v} * 2 = {times2_closure(v)}, {v} * 3 = {times3_closure(v)}")

print("Using callable classes:")
for v in values:
    print(f"  {v} * 2 = {times2_callable(v)}, {v} * 3 = {times3_callable(v)}")

# Extra: we can inspect attributes on the callable class
print("times2_callable.factor:", times2_callable.factor)
print("times3_callable.factor:", times3_callable.factor)

# For closures, factor is in the __closure__ cell variables (more hidden)
print("times2_closure is a function:", callable(times2_closure))
print("-" * 50)


# ===========================================================
# Rank 4 — Advanced
# Callable objects as configurable processors / decorators
# ===========================================================

print("Rank 4 — Advanced")


class TextProcessor:
    """
    A configurable text processor.

    Options:
    - strip: remove leading/trailing whitespace
    - to_lower: convert to lowercase
    - to_upper: convert to uppercase
    - prefix/suffix: add text around the input
    """

    def __init__(
        self,
        strip: bool = True,
        to_lower: bool = False,
        to_upper: bool = False,
        prefix: str = "",
        suffix: str = "",
    ) -> None:
        self.strip = strip
        self.to_lower = to_lower
        self.to_upper = to_upper
        self.prefix = prefix
        self.suffix = suffix

    def __call__(self, text: str) -> str:
        original = text
        if self.strip:
            text = text.strip()
        if self.to_lower and not self.to_upper:
            text = text.lower()
        if self.to_upper and not self.to_lower:
            text = text.upper()
        # If both flags are True, leave case unchanged (or you could decide one)
        text = f"{self.prefix}{text}{self.suffix}"
        print(f"Processed {original!r} -> {text!r}")
        return text


processor_title = TextProcessor(strip=True, to_upper=True, prefix="*** ", suffix=" ***")
processor_name = TextProcessor(strip=True, to_lower=True)

title = processor_title("   Hello Python World   ")
name = processor_name("  PEYMAN MIYANDASHTI  ")

print("Final title:", title)
print("Final name:", name)


class LoggerDecorator:
    """
    Callable object used as a decorator that logs function calls.
    """

    def __init__(self, label: str) -> None:
        self.label = label

    def __call__(self, func: Callable[..., Any]) -> Callable[..., Any]:
        """
        When used as @LoggerDecorator("label"), this is called with the
        function being decorated, and must return a wrapper.
        """

        def wrapper(*args: Any, **kwargs: Any) -> Any:
            print(f"[{self.label}] Calling {func.__name__} with args={args}, kwargs={kwargs}")
            result = func(*args, **kwargs)
            print(f"[{self.label}] {func.__name__} returned {result!r}")
            return result

        return wrapper


@LoggerDecorator("MATH")
def multiply(a: int, b: int) -> int:
    return a * b


multiply(3, 7)
multiply(10, 5)
print("-" * 50)


# ===========================================================
# Rank 5 — Professional
# Mini "command" system using callable objects
# ===========================================================

print("Rank 5 — Professional")


class Command:
    """
    Base class for commands. Each command is a callable object
    that receives a context dictionary and may modify it.
    """

    name: str = "base"

    def __call__(self, context: Dict[str, Any]) -> None:
        raise NotImplementedError


class AddStudent(Command):
    name = "add_student"

    def __init__(self, student_name: str) -> None:
        self.student_name = student_name

    def __call__(self, context: Dict[str, Any]) -> None:
        students: List[str] = context.setdefault("students", [])
        if self.student_name not in students:
            students.append(self.student_name)
            print(f"[AddStudent] Added {self.student_name!r}")
        else:
            print(f"[AddStudent] {self.student_name!r} already in list")


class RecordGrade(Command):
    name = "record_grade"

    def __init__(self, student_name: str, grade: float) -> None:
        self.student_name = student_name
        self.grade = grade

    def __call__(self, context: Dict[str, Any]) -> None:
        grades: Dict[str, List[float]] = context.setdefault("grades", {})
        student_grades = grades.setdefault(self.student_name, [])
        student_grades.append(self.grade)
        print(f"[RecordGrade] {self.student_name!r} + grade {self.grade}")


class PrintReport(Command):
    name = "print_report"

    def __call__(self, context: Dict[str, Any]) -> None:
        students: List[str] = context.get("students", [])
        grades: Dict[str, List[float]] = context.get("grades", {})
        print("\n[PrintReport] Students report:")
        if not students:
            print("  No students.")
            return
        for student in students:
            student_grades = grades.get(student, [])
            if student_grades:
                avg = sum(student_grades) / len(student_grades)
                print(f"  {student:10s} | grades={student_grades} | avg={avg:.1f}")
            else:
                print(f"  {student:10s} | no grades recorded")


class CommandRunner:
    """
    Runs a sequence of command objects on a shared context.
    """

    def __init__(self) -> None:
        self.commands: List[Command] = []

    def add_command(self, command: Command) -> None:
        self.commands.append(command)

    def run(self, context: Dict[str, Any]) -> None:
        print("[CommandRunner] Starting commands...")
        for cmd in self.commands:
            print(f"[CommandRunner] Executing command: {cmd.__class__.__name__}")
            cmd(context)
        print("[CommandRunner] Finished commands.")


context: Dict[str, Any] = {}

runner = CommandRunner()
runner.add_command(AddStudent("Peyman"))
runner.add_command(AddStudent("Ana"))
runner.add_command(RecordGrade("Peyman", 95))
runner.add_command(RecordGrade("Peyman", 88))
runner.add_command(RecordGrade("Ana", 92))
runner.add_command(PrintReport())

runner.run(context)

print("\nFinal context:", context)
print("-" * 50)
