"""
Mixins_Notes.py
Module 48 — Mixins
Author: Peyman Miyandashti
Year: 2025

This module explains mixins in Python.
Mixins are small classes that provide reusable behavior
to other classes through multiple inheritance.
"""

# ---------------------------------------------------------------------------
# 1. What Is a Mixin?
# ---------------------------------------------------------------------------
# A mixin is a class that:
# - provides specific behavior
# - is NOT meant to be instantiated alone
# - is used together with other classes
#
# Mixins usually:
# - have no __init__
# - focus on one responsibility


# ---------------------------------------------------------------------------
# 2. Simple Mixin Example
# ---------------------------------------------------------------------------

class LoggerMixin:
    def log(self, message: str) -> None:
        print(f"[LOG] {message}")


class Service(LoggerMixin):
    def run(self):
        self.log("Service started")


service = Service()
service.run()


# ---------------------------------------------------------------------------
# 3. Why Use Mixins?
# ---------------------------------------------------------------------------
# - Avoid code duplication
# - Keep classes small and focused
# - Add optional behavior
# - Avoid deep inheritance trees


# ---------------------------------------------------------------------------
# 4. Mixins vs Base Classes
# ---------------------------------------------------------------------------
# Base class:
# - represents an "is-a" relationship
#
# Mixin:
# - represents a "can-do" capability


# ---------------------------------------------------------------------------
# 5. Multiple Mixins
# ---------------------------------------------------------------------------

class JsonMixin:
    def to_json(self):
        return '{"status": "ok"}'


class ApiService(LoggerMixin, JsonMixin):
    def handle(self):
        self.log("Handling request")
        print(self.to_json())


api = ApiService()
api.handle()


# ---------------------------------------------------------------------------
# 6. Method Resolution Order (MRO)
# ---------------------------------------------------------------------------
# Python resolves methods left to right.
# MRO determines which method is called first.

print(ApiService.__mro__)


# ---------------------------------------------------------------------------
# 7. Common Rules for Mixins
# ---------------------------------------------------------------------------
# ✔ Keep mixins small
# ✔ One responsibility per mixin
# ✔ No state unless necessary
# ✔ No heavy __init__ logic


# ---------------------------------------------------------------------------
# 8. Common Mistakes
# ---------------------------------------------------------------------------
# - Using mixins as standalone classes
# - Adding too much logic
# - Deep mixin chains
# - Conflicting method names


# ---------------------------------------------------------------------------
# 9. Best Practices
# ---------------------------------------------------------------------------
# - Name mixins with the suffix "Mixin"
# - Document expected usage
# - Be careful with method name collisions
# - Prefer composition when inheritance is unclear


# ---------------------------------------------------------------------------
# Final Notes
# ---------------------------------------------------------------------------
# Mixins are a powerful design pattern
# when used intentionally and sparingly.
#
# Next Step:
# Continue with Mixins_Examples.py
