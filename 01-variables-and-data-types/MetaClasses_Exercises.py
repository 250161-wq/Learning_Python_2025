"""
Module 44 — Metaclasses: Practice Exercises
Comprehensive practice with Python metaclasses (type.__new__/__init__),
from beginner to more professional usage.

In this module I:
- See how a basic metaclass is called when creating classes.
- Use a metaclass to auto-add attributes to classes.
- Automatically register subclasses in a central registry.
- Enforce simple "interfaces" by checking for required methods.
- Build a mini plugin system using metaclasses.

Ranking system:
- Rank 1  -> Beginner: basic logging metaclass.
- Rank 2  -> Easy: auto-adding attributes on class creation.
- Rank 3  -> Intermediate: subclass registry with metaclass.
- Rank 4  -> Advanced: interface enforcement.
- Rank 5  -> Professional: mini plugin system.

Author: Peyman Miyandashti
Date of Birth: 11/11/1983
ID Number: 250161
Year: 2025
"""

from __future__ import annotations
from typing import Any, Dict, Type


# ===========================================================
# Rank 1 — Beginner
# Basic logging metaclass
# ===========================================================

print("Rank 1 — Beginner")


class LoggingMeta(type):
    def __new__(mcls, name: str, bases: tuple[type, ...], namespace: dict[str, Any]):
        print(f"[LoggingMeta] Creating class {name!r}")
        return super().__new__(mcls, name, bases, namespace)


class Example(metaclass=LoggingMeta):
    pass


e = Example()
print("Instance of Example created:", e)
print("-" * 50)


# ===========================================================
# Rank 2 — Easy
# Auto-adding attributes on class creation
# ===========================================================

print("Rank 2 — Easy")


class AutoDocMeta(type):
    """
    Metaclass that automatically adds a __doc__ if missing
    and a class-level 'created_by' attribute.
    """

    def __new__(mcls, name: str, bases: tuple[type, ...], namespace: dict[str, Any]):
        if "__doc__" not in namespace or namespace["__doc__"] is None:
            namespace["__doc__"] = f"Auto-generated docstring for {name}"
        namespace.setdefault("created_by", "AutoDocMeta")
        cls = super().__new__(mcls, name, bases, namespace)
        return cls


class AutoDocumented(metaclass=AutoDocMeta):
    pass


print("AutoDocumented.__doc__:", AutoDocumented.__doc__)
print("AutoDocumented.created_by:", AutoDocumented.created_by)
print("-" * 50)


# ===========================================================
# Rank 3 — Intermediate
# Subclass registry via metaclass
# ===========================================================

print("Rank 3 — Intermediate")


class RegisteredMeta(type):
    """
    Metaclass that keeps a registry of subclasses by name.
    """

    registry: Dict[str, Type[Any]] = {}

    def __new__(mcls, name: str, bases: tuple[type, ...], namespace: dict[str, Any]):
        cls = super().__new__(mcls, name, bases, namespace)
        if name != "BaseRegistered":  # avoid registering the base class
            RegisteredMeta.registry[name] = cls
        return cls


class BaseRegistered(metaclass=RegisteredMeta):
    pass


class A(BaseRegistered):
    pass


class B(BaseRegistered):
    pass


print("Registered classes:", RegisteredMeta.registry)
print("-" * 50)


# ===========================================================
# Rank 4 — Advanced
# Interface enforcement with metaclasses
# ===========================================================

print("Rank 4 — Advanced")


class InterfaceMeta(type):
    """
    Metaclass that enforces that certain methods exist on the class.
    Subclasses can define a class attribute __required_methods__.
    """

    def __new__(mcls, name: str, bases: tuple[type, ...], namespace: dict[str, Any]):
        required = namespace.get("__required_methods__", ())
        cls = super().__new__(mcls, name, bases, namespace)

        # Collect methods from base classes too
        all_attributes = set(namespace)
        for base in bases:
            all_attributes.update(dir(base))

        missing = [m for m in required if m not in all_attributes]
        if missing:
            raise TypeError(
                f"Class {name!r} is missing required methods: {', '.join(missing)}"
            )
        return cls


class ServiceBase(metaclass=InterfaceMeta):
    __required_methods__ = ("start", "stop")


class MyService(ServiceBase):
    def start(self) -> None:
        print("Service started")

    def stop(self) -> None:
        print("Service stopped")


service = MyService()
service.start()
service.stop()

# Uncomment to see a failure:
# class BadService(ServiceBase):
#     def start(self): ...
print("-" * 50)


# ===========================================================
# Rank 5 — Professional
# Mini plugin system using metaclasses
# ===========================================================

print("Rank 5 — Professional")


class PluginMeta(type):
    """
    Metaclass that registers plugin classes by a plugin_name attribute.
    """

    plugins: Dict[str, Type[Any]] = {}

    def __new__(mcls, name: str, bases: tuple[type, ...], namespace: dict[str, Any]):
        cls = super().__new__(mcls, name, bases, namespace)
        plugin_name = namespace.get("plugin_name")
        if plugin_name:
            if plugin_name in PluginMeta.plugins:
                raise ValueError(f"Plugin name {plugin_name!r} already registered")
            PluginMeta.plugins[plugin_name] = cls
        return cls

    @classmethod
    def get_plugin(mcls, name: str) -> Type[Any]:
        if name not in PluginMeta.plugins:
            raise KeyError(f"No plugin named {name!r}")
        return PluginMeta.plugins[name]


class PluginBase(metaclass=PluginMeta):
    plugin_name: str | None = None

    def run(self, data: Any) -> Any:
        raise NotImplementedError


class UpperCasePlugin(PluginBase):
    plugin_name = "upper"

    def run(self, data: str) -> str:
        return data.upper()


class ReversePlugin(PluginBase):
    plugin_name = "reverse"

    def run(self, data: str) -> str:
        return data[::-1]


def execute_plugin(plugin_name: str, data: str) -> str:
    plugin_cls = PluginMeta.get_plugin(plugin_name)
    plugin = plugin_cls()
    print(f"Running plugin {plugin_name!r} with data={data!r}")
    return plugin.run(data)


print("Available plugins:", list(PluginMeta.plugins.keys()))

text = "Nova and Peyman learning metaclasses"
print("Upper plugin result:", execute_plugin("upper", text))
print("Reverse plugin result:", execute_plugin("reverse", text))
print("-" * 50)
