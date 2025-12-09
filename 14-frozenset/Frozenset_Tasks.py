"""
Module 14 — Frozenset
Practice Tasks

This file contains structured exercises to help you practice how frozensets
work, how they differ from sets, and where immutability matters.

Work through the tasks from Rank 1 to Rank 5.
Only open the solutions file after attempting each task honestly.
"""

# ============================================================
# Rank 1 — Beginner
# Basic frozenset creation and comparisons.
# ============================================================

# Task 1.1
# Create a frozenset containing the values: 1, 2, 3.
# Print the result.
#
# Write your code below:


# Task 1.2
# Convert the following list into a frozenset and print it:
# items = ["a", "b", "a", "c"]
#
# Write your code below:


# Task 1.3
# Given:
# fs = frozenset([10, 20, 30])
# Write code that checks if the number 20 is in the frozenset.
#
# Write your code below:


# ============================================================
# Rank 2 — Easy
# Allowed operations: union, intersection, difference.
# ============================================================

# Task 2.1
# Perform a union between:
#   a = frozenset([1, 2, 3])
#   b = frozenset([3, 4])
# Print the result.
#
# Write your code below:


# Task 2.2
# Compute the intersection of:
#   fs1 = frozenset([5, 6, 7])
#   fs2 = frozenset([7, 8, 9])
#
# Write your code below:


# Task 2.3
# Compute the difference: fsA - fsB
#   fsA = frozenset([1, 2, 3, 4])
#   fsB = frozenset([3, 4])
#
# Write your code below:


# ============================================================
# Rank 3 — Intermediate
# Hashability and using frozensets inside sets or dictionaries.
# ============================================================

# Task 3.1
# Create a dictionary where:
# Key: frozenset(["red", "blue"])
# Value: "primary mix"
#
# Then print the value using the frozenset key.
#
# Write your code below:


# Task 3.2
# Create a set that contains two frozensets:
#   frozenset([1, 2])
#   frozenset([3, 4])
#
# Print the resulting set.
#
# Write your code below:


# Task 3.3
# You are given three lists of ingredients:
#   item1 = ["sugar", "flour"]
#   item2 = ["flour", "sugar"]   # same combo!
#   item3 = ["milk", "chocolate"]
#
# Use frozenset to group unique combinations into a set.
# Print the resulting set.
#
# Write your code below:


# ============================================================
# Rank 4 — Advanced
# Immutability constraints and safe configuration structures.
# ============================================================

# Task 4.1
# Create a frozenset called allowed_settings with:
#   "dark_mode", "notifications", "auto_save"
#
# Then check if the variable:
#   setting = "auto_save"
# is allowed. Print a message.
#
# Write your code below:


# Task 4.2
# Demonstrate immutability:
# Create a frozenset fs = frozenset([1, 2, 3])
# Write a comment explaining why fs.add(4) would cause an error.
#
# Write your explanation below as a comment:


# Task 4.3
# Create two frozensets:
#   A = frozenset([1, 2, 3])
#   B = frozenset([2, 3, 4])
#
# Print:
# - their union
# - their symmetric difference
#
# Write your code below:


# ============================================================
# Rank 5 — Professional
# Realistic usage of frozensets in apps and algorithms.
# ============================================================

# Task 5.1
# Create a caching system using a dictionary:
#
# The key should be a frozenset of request parameters, for example:
#   frozenset(["page=1", "limit=20"])
#
# The value can be a simple message, like "Cached result".
#
# Then retrieve and print the value using the frozenset key.
#
# Write your code below:


# Task 5.2
# You have an app with allowed user roles:
# allowed_roles = frozenset(["admin", "teacher", "student"])
#
# Given:
# user_role = "teacher"
#
# Write a condition that prints:
# - "Access granted" if the role is allowed
# - "Access denied" otherwise
#
# Write your code below:


# Task 5.3
# Create a set of frozensets that represent all unique unordered
# pairs in this list:
# values = [1, 2, 3]
#
# Required unique pairs:
# frozenset([1,2]), frozenset([1,3]), frozenset([2,3])
#
# Print the resulting set.
#
# Write your code below:


# End of Tasks
