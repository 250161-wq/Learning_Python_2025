"""
Module 17 — Integers: Practice Task Solutions
---------------------------------------------

This file contains clean, professional solutions to all integer exercises
from Integer_Tasks.py. Many tasks have multiple valid approaches; these
solutions focus on clarity and correctness.

IMPORTANT:
Only read these solutions AFTER attempting the tasks yourself!
"""


# ---------------------------------------------------------------------------
# Rank 1 — Beginner
# ---------------------------------------------------------------------------

# Task 1.1
birth_year = 1981
current_year = 2025
age = current_year - birth_year
print("I am", age, "years old.")


# Task 1.2
a = 8
b = 3
c = 2
print("a + b =", a + b)
print("a - b =", a - b)
print("a * c =", a * c)


# Task 1.3
number_text = "42"
value = int(number_text)
print("The number is", value, "and its double is", value * 2)


# Task 1.4
# Example behavior — only works when input is allowed:
# user_number = int(input("Type a number: "))
# print("You typed:", user_number)
print("Input version skipped in solutions (interactive).")


# ---------------------------------------------------------------------------
# Rank 2 — Easy
# ---------------------------------------------------------------------------

# Task 2.1
morning_temp = 18
afternoon_temp = 27
difference = afternoon_temp - morning_temp
print("The temperature changed by", difference, "degrees.")


# Task 2.2
# user_minutes = int(input("Minutes: "))
# seconds = user_minutes * 60
# print(f"{user_minutes} minutes = {seconds} seconds")
print("Input version skipped in solutions (interactive).")


# Task 2.3
candies = 23
children = 4
per_child = candies // children
remainder = candies % children
print("Each child gets", per_child, "candies.")
print("Candies left over:", remainder)


# Task 2.4
counter = 0
counter += 1
counter += 5
counter -= 2
print("Final counter value:", counter)


# ---------------------------------------------------------------------------
# Rank 3 — Intermediate
# ---------------------------------------------------------------------------

# Task 3.1
# Example implementation:
# a = int(input("Enter a: "))
# b = int(input("Enter b: "))
# print("Sum:", a + b)
# print("Difference:", a - b)
# print("Product:", a * b)
# if b != 0:
#     print("Integer division:", a // b)
print("Task 3.1 interactive example skipped.")


# Task 3.2
# number = int(input("Enter a number: "))
# if number % 2 == 0:
#     print(number, "is even.")
# else:
#     print(number, "is odd.")
print("Task 3.2 interactive example skipped.")


# Task 3.3
# level_1 = int(input("Score for level 1: "))
# level_2 = int(input("Score for level 2: "))
# level_3 = int(input("Score for level 3: "))
# total = level_1 + level_2 + level_3
# print("Total score:", total)
print("Task 3.3 interactive example skipped.")


# Task 3.4
# value = int(input("Enter a number 0–100: "))
# if value < 0:
#     value = 0
# elif value > 100:
#     value = 100
# print("Clamped value:", value)
print("Task 3.4 interactive example skipped.")


# ---------------------------------------------------------------------------
# Rank 4 — Advanced
# ---------------------------------------------------------------------------

# Task 4.1
numbers = [10, 4, 7, 0, -3, 15]

smallest = numbers[0]
largest = numbers[0]
total_sum = 0

for n in numbers:
    if n < smallest:
        smallest = n
    if n > largest:
        largest = n
    total_sum += n

print("Smallest:", smallest)
print("Largest:", largest)
print("Sum:", total_sum)


# Task 4.2
count_pos = 0
count_neg = 0
count_zero = 0

for n in numbers:
    if n > 0:
        count_pos += 1
    elif n < 0:
        count_neg += 1
    else:
        count_zero += 1

print("Positives:", count_pos)
print("Negatives:", count_neg)
print("Zeros:", count_zero)


# Task 4.3
# scores_count = int(input("How many scores? "))
# total = 0
# for _ in range(scores_count):
#     score = int(input("Score: "))
#     total += score
# average = total // scores_count
# print("Average score:", average)
print("Task 4.3 interactive example skipped.")


# Task 4.4
steps = [3500, 5000, 4200, 6000, 7100, 3000, 8000]

total_steps = sum(steps)
average_steps = total_steps // len(steps)

print("Total steps:", total_steps)
print("Average steps:", average_steps)


# ---------------------------------------------------------------------------
# Rank 5 — Professional
# ---------------------------------------------------------------------------

# Task 5.1
def percentage_of(part, whole):
    if whole == 0:
        return 0
    return part * 100 // whole

print("percentage_of(25, 100) =", percentage_of(25, 100))
print("percentage_of(1, 3)    =", percentage_of(1, 3))


# Task 5.2
def days_to_weeks_days(total_days):
    weeks = total_days // 7
    days = total_days % 7
    return (weeks, days)

print("days_to_weeks_days(10) =", days_to_weeks_days(10))
print("days_to_weeks_days(21) =", days_to_weeks_days(21))


# Task 5.3
def clamp(value, minimum, maximum):
    if value < minimum:
        return minimum
    if value > maximum:
        return maximum
    return value

print("clamp(150, 0, 100) =", clamp(150, 0, 100))
print("clamp(-5, 0, 100)  =", clamp(-5, 0, 100))
print("clamp(50, 0, 100)  =", clamp(50, 0, 100))


# Task 5.4
def next_even(n):
    if n % 2 == 0:
        return n
    else:
        return n + 1

print("next_even(4)  =", next_even(4))
print("next_even(5)  =", next_even(5))
print("next_even(10) =", next_even(10))


# End of Solutions
