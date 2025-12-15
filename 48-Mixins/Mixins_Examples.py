"""
Mixins_Examples.py
Module 48 — Mixins
Author: Peyman Miyandashti
Year: 2025

This file contains clear and practical examples
showing how mixins are used in Python.
"""

# ---------------------------------------------------------------------------
# Example 1: Basic Mixin
# ---------------------------------------------------------------------------

class TimestampMixin:
    def timestamp(self) -> str:
        return "2025-01-01"


class Event(TimestampMixin):
    def info(self) -> None:
        print("Event at", self.timestamp())


event = Event()
event.info()


# ---------------------------------------------------------------------------
# Example 2: Logging Mixin
# ---------------------------------------------------------------------------

class LoggingMixin:
    def log(self, message: str) -> None:
        print(f"[LOG]: {message}")


class Task(LoggingMixin):
    def execute(self) -> None:
        self.log("Task started")
        self.log("Task finished")


task = Task()
task.execute()


# ---------------------------------------------------------------------------
# Example 3: Multiple Mixins
# ---------------------------------------------------------------------------

class JsonMixin:
    def to_json(self) -> str:
        return '{"status": "ok"}'


class XmlMixin:
    def to_xml(self) -> str:
        return "<status>ok</status>"


class ApiResponse(JsonMixin, XmlMixin):
    pass


response = ApiResponse()
print(response.to_json())
print(response.to_xml())


# ---------------------------------------------------------------------------
# Example 4: Mixins with Business Classes
# ---------------------------------------------------------------------------

class SaveMixin:
    def save(self) -> None:
        print("Saved successfully")


class User(SaveMixin, LoggingMixin):
    def create(self) -> None:
        self.log("Creating user")
        self.save()


user = User()
user.create()


# ---------------------------------------------------------------------------
# Example 5: Method Resolution Order (MRO)
# ---------------------------------------------------------------------------

class A:
    def action(self):
        print("Action from A")


class B(A):
    def action(self):
        print("Action from B")


class C(B, A):
    pass


print(C.__mro__)
c = C()
c.action()


# ---------------------------------------------------------------------------
# Example 6: Avoiding State in Mixins
# ---------------------------------------------------------------------------

class DisplayMixin:
    def display(self, text: str) -> None:
        print(text)


class Screen(DisplayMixin):
    pass


screen = Screen()
screen.display("Hello Mixins")


# ---------------------------------------------------------------------------
# Final Notes
# ---------------------------------------------------------------------------
# These examples demonstrate:
# - reusable behavior through mixins
# - multiple inheritance usage
# - safe and clean design patterns
#
# Next Step:
# Continue with Mixins_Tasks.py
