"""
Mixins_Tasks_Solutions.py
Module 48 — Mixins
Author: Peyman Miyandashti
Year: 2025

This file contains clean and professional solutions
for the mixins exercises in this module.
"""

# ---------------------------------------------------------------------------
# Rank 1 — Beginner-Advanced
# ---------------------------------------------------------------------------

# Task 1 Solution
class PrintMixin:
    def print_message(self, message: str) -> None:
        print(message)


# Task 2 Solution
class Printer(PrintMixin):
    pass

printer = Printer()
printer.print_message("Hello from PrintMixin")


# ---------------------------------------------------------------------------
# Rank 2 — Easy
# ---------------------------------------------------------------------------

# Task 3 Solution
class TimestampMixin:
    def timestamp(self) -> str:
        return "2025-01-01"


class Event(TimestampMixin):
    def show(self) -> None:
        print("Event at", self.timestamp())


event = Event()
event.show()


# Task 4 Solution
# Mixins usually do not need __init__ because:
# - they do not manage object state
# - they only add behavior
# - initialization belongs to concrete classes


# ---------------------------------------------------------------------------
# Rank 3 — Intermediate
# ---------------------------------------------------------------------------

# Task 5 Solution
class LoggerMixin:
    def log(self, message: str) -> None:
        print(f"[LOG] {message}")


class SerializerMixin:
    def serialize(self) -> str:
        return '{"status": "ok"}'


class Service(LoggerMixin, SerializerMixin):
    pass


# Task 6 Solution
service = Service()
service.log("Service running")
print(service.serialize())


# ---------------------------------------------------------------------------
# Rank 4 — Advanced
# ---------------------------------------------------------------------------

# Task 7 Solution
class MixinA:
    def action(self):
        print("Action from MixinA")


class MixinB:
    def action(self):
        print("Action from MixinB")


class Combined(MixinA, MixinB):
    pass


combined = Combined()
combined.action()


# Task 8 Solution
print(Combined.__mro__)

# Method Resolution Order (MRO) explanation:
# Python searches methods from left to right
# following the MRO tuple.
# MixinA.action is called before MixinB.action.


# ---------------------------------------------------------------------------
# Rank 5 — Professional
# ---------------------------------------------------------------------------

# Task 9 Solution
class ValidationMixin:
    def validate_not_empty(self, value: str) -> None:
        if not value:
            raise ValueError("Value cannot be empty")


class User(ValidationMixin):
    def create(self, name: str) -> None:
        self.validate_not_empty(name)
        print("User created:", name)


user = User()
user.create("Peyman")


# Task 10 Solution
# Mixins are a good choice when:
# - behavior is reusable across unrelated classes
# - functionality is optional
# - classes remain small and focused
#
# Composition is better when:
# - behavior requires complex state
# - inheritance becomes unclear
# - relationships are not behavioral


# ---------------------------------------------------------------------------
# Final Notes
# ---------------------------------------------------------------------------
# These solutions demonstrate:
# - clean mixin design
# - safe multiple inheritance
# - correct use of MRO
#
# Next Step:
# Move on to the next module when ready.
