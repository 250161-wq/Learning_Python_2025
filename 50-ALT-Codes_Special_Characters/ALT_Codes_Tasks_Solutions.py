"""
ALT_Codes_Tasks_Solutions.py
Module 50 — ALT Codes (Special Characters)
Author: Peyman Miyandashti
Year: 2025

Clean and professional solutions for Module 50.
"""

# ---------------------------------------------------------------------------
# Rank 1 — Beginner
# ---------------------------------------------------------------------------

print("─", "➤", "█")


print("─" * 30)


# ---------------------------------------------------------------------------
# Rank 2 — Easy
# ---------------------------------------------------------------------------

print("╔══════╗")
print("║ Box  ║")
print("╚══════╝")

print("➤ Option A")
print("➤ Option B")


# ---------------------------------------------------------------------------
# Rank 3 — Intermediate
# ---------------------------------------------------------------------------

print("╔════════╦════════╗")
print("║ Name   ║ Age    ║")
print("╠════════╬════════╣")
print("║ Peyman ║ 43     ║")
print("╚════════╩════════╝")

print("░░░░▒▒▒▒▓▓▓▓████")


# ---------------------------------------------------------------------------
# Rank 4 — Advanced
# ---------------------------------------------------------------------------

def print_box(message: str) -> None:
    width = len(message) + 4
    print("╔" + "═" * width + "╗")
    print(f"║  {message}  ║")
    print("╚" + "═" * width + "╝")

print_box("Hello ALT Codes")


def print_menu(options):
    for opt in options:
        print("➤", opt)

print_menu(["Start", "Settings", "Exit"])


# ---------------------------------------------------------------------------
# Rank 5 — Professional
# ---------------------------------------------------------------------------

# ALT characters improve UX when:
# - building console interfaces
# - visual separation is needed
# - output must be readable
#
# They should be avoided when:
# - terminal compatibility is unknown
# - plain text is required
# - accessibility is a concern
