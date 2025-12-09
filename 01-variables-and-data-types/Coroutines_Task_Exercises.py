"""
Module 24 — Coroutines (async/await): Practice Exercises
Comprehensive practice with Python coroutines, from beginner to
more professional, production-style usage.

In this module I:
- Learn how to define and run async coroutines with async/await.
- See the difference between sequential and concurrent async tasks.
- Use asyncio tools like gather(), sleep(), and wait_for().
- Practice with realistic scenarios from Peyman's life.

Ranking system:
- Rank 1  -> Beginner: very basic async syntax and single coroutine.
- Rank 2  -> Easy: calling and awaiting multiple coroutines.
- Rank 3  -> Intermediate: running tasks concurrently with asyncio.gather.
- Rank 4  -> Advanced: small "simulated" async workflow.
- Rank 5  -> Professional: reusable coroutine utilities and patterns.

Author: Peyman Miyandashti
Date of Birth: 11/11/1983
ID Number: 250161
Year: 2025
"""

import asyncio
import time

# Simple constants with Peyman's info (used in async examples)
PEYMAN_NAME = "Peyman Miyandashti"
PEYMAN_AGE = 43
WIFE_NAME = "Arlette Chong"
UNIVERSITY = "Polytechnic Baja California University (UPBC)"
CITY = "Mexicali"
GAME = "World of Warcraft"


# ===========================================================
# Rank 1 — Beginner
# First coroutine + basic async/await
# ===========================================================

async def greet_student():
    """
    Very first coroutine:
    - Waits a bit.
    - Prints a short greeting using Peyman's info.
    """
    print("Rank 1 — Beginner")
    print("Defining and running a simple coroutine...")
    await asyncio.sleep(0.5)  # simulate a small delay
    print(f"Hello {PEYMAN_NAME}, welcome to async coroutines! 🧠")
    print(f"You are {PEYMAN_AGE} years old and studying at {UNIVERSITY} in {CITY}.")
    print("-" * 50)


def run_rank_1():
    asyncio.run(greet_student())


# ===========================================================
# Rank 2 — Easy
# Multiple coroutines, awaiting them in sequence
# ===========================================================

async def load_profile():
    """Simulate loading Peyman's profile from a database."""
    await asyncio.sleep(0.5)
    print("Profile loaded:")
    print(f"- Name: {PEYMAN_NAME}")
    print(f"- Age: {PEYMAN_AGE}")
    print(f"- From: Tabriz, Iran -> Now in {CITY}, Mexico")
    print(f"- Favorite game: {GAME}")


async def load_family_info():
    """Simulate loading family information."""
    await asyncio.sleep(0.5)
    print("Family info loaded:")
    print(f"- Wife: {WIFE_NAME}")
    print("- Status: Married ❤️")


async def rank_2_coroutines():
    print("Rank 2 — Easy")
    print("Running multiple coroutines sequentially...")
    await load_profile()
    await load_family_info()
    print("-" * 50)


def run_rank_2():
    asyncio.run(rank_2_coroutines())


# ===========================================================
# Rank 3 — Intermediate
# Running coroutines concurrently with asyncio.gather
# ===========================================================

async def simulate_study_session(module_name: str, duration: float):
    """Simulate studying a module for some seconds."""
    print(f"Started studying {module_name} for {duration} seconds...")
    await asyncio.sleep(duration)
    print(f"Finished studying {module_name}.")


async def simulate_game_session(game_name: str, duration: float):
    """Simulate playing a game for some seconds."""
    print(f"Started playing {game_name} for {duration} seconds...")
    await asyncio.sleep(duration)
    print(f"Finished playing {game_name}.")


async def rank_3_coroutines():
    print("Rank 3 — Intermediate")
    print("Running study + game sessions concurrently with asyncio.gather...")

    start = time.perf_counter()

    # Run 3 coroutines concurrently
    await asyncio.gather(
        simulate_study_session("Module 24 — Coroutines", 2),
        simulate_study_session("Module 23 — Generators", 3),
        simulate_game_session(GAME, 4),
    )

    end = time.perf_counter()
    total_time = end - start
    print(f"Total elapsed time (approx): {total_time:.2f} seconds")
    print("Notice it's less than 2 + 3 + 4 because they ran concurrently.")
    print("-" * 50)


def run_rank_3():
    asyncio.run(rank_3_coroutines())


# ===========================================================
# Rank 4 — Advanced
# Small async "workflow": tasks + asyncio.create_task()
# ===========================================================

async def fetch_assignment_from_upbc(module_number: int):
    """
    Simulate fetching an assignment description from UPBC.
    """
    await asyncio.sleep(1)
    print(f"[UPBC] Assignment for Module {module_number} downloaded.")
    return {
        "module": module_number,
        "title": f"Module {module_number} — Async Practice",
        "required_hours": 3,
    }


async def fetch_world_of_warcraft_daily_quests():
    """
    Simulate fetching daily quests from World of Warcraft.
    """
    await asyncio.sleep(1.5)
    print("[WoW] Daily quests fetched.")
    return ["Defeat dungeon boss", "Collect 20 items", "Complete 3 battlegrounds"]


async def rank_4_workflow():
    print("Rank 4 — Advanced")
    print("Building a small concurrent workflow with asyncio.create_task...")

    # Start both tasks at the same time
    upbc_task = asyncio.create_task(fetch_assignment_from_upbc(24))
    wow_task = asyncio.create_task(fetch_world_of_warcraft_daily_quests())

    # Wait for both to finish
    assignment, quests = await asyncio.gather(upbc_task, wow_task)

    print("\nSummary of async results:")
    print(f"- UPBC assignment title: {assignment['title']}")
    print(f"- Required study hours: {assignment['required_hours']}")
    print(f"- Number of WoW quests today: {len(quests)}")
    print("-" * 50)


def run_rank_4():
    asyncio.run(rank_4_workflow())


# ===========================================================
# Rank 5 — Professional
# Reusable async utilities and timeout handling
# ===========================================================

async def simulate_slow_network_call(name: str, delay: float):
    """
    Simulate a slow network call with a given delay.
    """
    print(f"[{name}] Starting network call (delay={delay}s)...")
    await asyncio.sleep(delay)
    print(f"[{name}] Network call finished.")
    return f"Result from {name}"


async def run_with_timeout(coro, timeout: float):
    """
    Run a coroutine with a timeout.
    - If it finishes in time, return the result.
    - If it times out, return None and log a message.
    """
    try:
        result = await asyncio.wait_for(coro, timeout=timeout)
        return result
    except asyncio.TimeoutError:
        print(f"⚠️ Coroutine timed out after {timeout} seconds.")
        return None


async def rank_5_professional():
    print("Rank 5 — Professional")
    print("Using a reusable timeout helper with coroutines...")

    # Fast enough to finish
    fast_result = await run_with_timeout(
        simulate_slow_network_call("UPBC-API", 1.0),
        timeout=2.0,
    )

    # Too slow: will timeout
    slow_result = await run_with_timeout(
        simulate_slow_network_call("Game-Stats-API", 3.0),
        timeout=1.0,
    )

    print("\nCollected results:")
    print(f"- Fast result: {fast_result}")
    print(f"- Slow result (should be None): {slow_result}")
    print("-" * 50)


def run_rank_5():
    asyncio.run(rank_5_professional())


# ===========================================================
# Main entry point
# Run all ranks in order when executed as a script
# ===========================================================

if __name__ == "__main__":
    run_rank_1()
    run_rank_2()
    run_rank_3()
    run_rank_4()
    run_rank_5()
