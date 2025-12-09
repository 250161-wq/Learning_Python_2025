"""
Module 13 — Ranges
Practice Task Solutions

This file contains clean, professional solutions to all exercises found in
Ranges_Tasks.py. Multiple solutions are possible; these represent clear and
recommended approaches for learning and practice.

Only open this file after attempting the tasks on your own.
"""

# ---------------------------------------------------------------------------
# Rank 1 — Beginner
# ---------------------------------------------------------------------------

# Task 1.1
print(list(range(5)))  # [0, 1, 2, 3, 4]

# Task 1.2
for i in range(3, 7):
    print(i)

# Task 1.3
for i in range(10, 15):
    print(i)


# ---------------------------------------------------------------------------
# Rank 2 — Easy
# ---------------------------------------------------------------------------

# Task 2.1
for i in range(0, 21, 2):
    print(i)

# Task 2.2
for i in range(5, 18, 3):
    print(i)

# Task 2.3
for i in range(10, 0, -1):
    print(i)


# ---------------------------------------------------------------------------
# Rank 3 — Intermediate
# ---------------------------------------------------------------------------

# Task 3.1
names = ["Ana", "Luis", "Pablo"]
for i in range(len(names)):
    print(f"Index {i} → {names[i]}")

# Task 3.2
nums = list(range(1, 21))
for i in range(0, len(nums), 2):
    print(nums[i])

# Task 3.3
reversed_list = list(range(10, 0, -1))
print(reversed_list)


# ---------------------------------------------------------------------------
# Rank 4 — Advanced
# ---------------------------------------------------------------------------

# Task 4.1
data = list(range(1, 17))
batch_size = 4
for start in range(0, len(data), batch_size):
    end = start + batch_size
    batch = data[start:end]
    print("Batch:", batch)

# Task 4.2
print(list(range(50, -1, -5)))

# Task 4.3
print(75 in range(0, 101))   # True
print(200 in range(0, 101))  # False


# ---------------------------------------------------------------------------
# Rank 5 — Professional
# ---------------------------------------------------------------------------

# Task 5.1
data = list(range(1, 51))
page_size = 10

page_number = 1
for start in range(0, len(data), page_size):
    end = start + page_size
    page = data[start:end]
    print(f"Page {page_number}: {page}")
    page_number += 1

# Task 5.2
multiples_of_7 = list(range(0, 501, 7))
print(multiples_of_7)

# Task 5.3
for i in range(5, 0, -1):
    print(i)
print("Lift off!")


# End of Solutions
