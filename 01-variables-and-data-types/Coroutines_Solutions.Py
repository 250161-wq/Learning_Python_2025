"""
Module 24 — Coroutines (async/await): Solutions
Comprehensive practice with Python coroutines and async/await,
from beginner to more professional, production-style usage.

This file contains *solutions* for the coroutine practice tasks.

In this module I:
- Learn how to define and run async coroutines with `async def`.
- Use `await` with asyncio.sleep to simulate delays.
- Run multiple coroutines concurrently with `asyncio.gather`.
- Create a simple async iterator and a producer/consumer pipeline.

Ranking system:
- Rank 1  -> Beginner: very basic coroutines and awaiting.
- Rank 2  -> Easy: small async utilities, still simple.
- Rank 3  -> Intermediate: combining multiple async calls.
- Rank 4  -> Advanced: async iterators and queues.
- Rank 5  -> Professional: small, realistic async pipeline.

Author: Peyman Miyandashti
Date of Birth: 11/11/1983
ID Number: 250161
Year: 2025
"""

from __future__ import annotations

import asyncio
from typing import List, AsyncIterator


# ===========================================================
# Rank 1 — Beginner
# Simple coroutine: wait, then print a message
# ===========================================================

async def delay_print(message: str, delay_seconds: float) -> None:
    """
    Wait `delay_seconds` and then print `message`.

    This shows the most basic coroutine pattern:
    - async def
    - await asyncio.sleep(...)
    """
    await asyncio.sleep(delay_seconds)
    print(f"[delay_print] After {delay_seconds:.1f}s -> {message}")


async def rank1_demo() -> None:
    """
    Demo for Rank 1: call delay_print a few times.
    When run with asyncio, these will wait and print messages.
    """
    print("Rank 1 — Beginner (coroutines)")
    await delay_print("Hello from Peyman 👋", 0.5)
    await delay_print("I study at UPBC (IT & Digital Innovation).", 0.5)
    await delay_print("I love World of Warcraft!", 0.5)
    print("-" * 50)


# ===========================================================
# Rank 2 — Easy
# Small async utilities based on Peyman's data
# ===========================================================

async def compute_age_in_future(current_age: int, years_ahead: int) -> int:
    """
    Simulate a tiny delay, then return age in `years_ahead` years.
    """
    await asyncio.sleep(0.1)
    return current_age + years_ahead


async def wait_and_get_favorite_number(favorite_number: int) -> int:
    """
    Simulate fetching Peyman's favorite number from a remote service.
    """
    await asyncio.sleep(0.1)
    return favorite_number


async def rank2_demo() -> None:
    print("Rank 2 — Easy (coroutines)")
    peyman_age = 43
    favorite_number = 11

    age_in_5_years = await compute_age_in_future(peyman_age, 5)
    fav_number = await wait_and_get_favorite_number(favorite_number)

    print(f"Current age: {peyman_age}")
    print(f"Age in 5 years (async): {age_in_5_years}")
    print(f"Favorite number (async fetched): {fav_number}")
    print("-" * 50)


# ===========================================================
# Rank 3 — Intermediate
# Running multiple coroutines concurrently with asyncio.gather
# ===========================================================

async def simulate_game_match(player_name: str, duration_seconds: float) -> str:
    """
    Simulate a World of Warcraft match for `duration_seconds` and
    return a small summary string.
    """
    await asyncio.sleep(duration_seconds)
    return f"Player {player_name} finished a match in {duration_seconds:.1f} seconds."


async def run_multiple_matches(player_name: str, durations: List[float]) -> List[str]:
    """
    Run multiple game matches concurrently and collect results.
    """
    tasks = [
        asyncio.create_task(simulate_game_match(player_name, d))
        for d in durations
    ]
    results = await asyncio.gather(*tasks)
    return results


async def rank3_demo() -> None:
    print("Rank 3 — Intermediate (coroutines + concurrency)")
    player = "Peyman"
    durations = [0.5, 0.7, 0.3]

    print("Starting concurrent matches...")
    results = await run_multiple_matches(player, durations)
    for r in results:
        print(r)
    print("-" * 50)


# ===========================================================
# Rank 4 — Advanced
# Async iterator: countdown with delays
# ===========================================================

class AsyncCountdown:
    """
    Simple async iterator that counts down from `start` to 1,
    waiting `delay_seconds` between each number.

    Example:
        async for value in AsyncCountdown(3, 0.2):
            print(value)
    """

    def __init__(self, start: int, delay_seconds: float = 0.2) -> None:
        self.current = start
        self.delay_seconds = delay_seconds

    def __aiter__(self) -> AsyncIterator[int]:
        return self

    async def __anext__(self) -> int:
        if self.current <= 0:
            raise StopAsyncIteration
        await asyncio.sleep(self.delay_seconds)
        value = self.current
        self.current -= 1
        return value


async def rank4_demo() -> None:
    print("Rank 4 — Advanced (async iterator)")
    print("Countdown before starting a new async training session:")

    async for value in AsyncCountdown(5, 0.1):
        print("..", value)

    print("Go! Start studying Python coroutines 🚀")
    print("-" * 50)


# ===========================================================
# Rank 5 — Professional
# Small async producer/consumer pipeline
# ===========================================================

async def game_event_producer(queue: asyncio.Queue, total_events: int) -> None:
    """
    Produce `total_events` game events and put them into the queue.
    Pretend we are getting them from some external service.
    """
    for i in range(1, total_events + 1):
        await asyncio.sleep(0.1)  # simulate waiting for next event
        event = {
            "id": i,
            "player": "Peyman",
            "game": "World of Warcraft",
            "description": f"Event #{i} for player Peyman",
        }
        await queue.put(event)
        print(f"[producer] queued event {i}")

    # Signal the consumer that we are done
    await queue.put(None)  # type: ignore[arg-type]
    print("[producer] done, sent stop signal (None)")


async def game_event_consumer(queue: asyncio.Queue) -> List[dict]:
    """
    Consume events from the queue until it receives `None`.
    Return the list of processed events.
    """
    processed: List[dict] = []

    while True:
        event = await queue.get()
        if event is None:
            print("[consumer] received stop signal")
            break

        # Simulate some processing
        await asyncio.sleep(0.05)
        event["processed"] = True
        processed.append(event)
        print(f"[consumer] processed event {event['id']}")

    return processed


async def run_game_event_pipeline(total_events: int = 5) -> List[dict]:
    """
    Run the producer/consumer pipeline.
    """
    queue: asyncio.Queue = asyncio.Queue()

    producer_task = asyncio.create_task(game_event_producer(queue, total_events))
    consumer_task = asyncio.create_task(game_event_consumer(queue))

    # Wait for both producer and consumer to finish
    processed_events = await asyncio.gather(producer_task, consumer_task)

    # processed_events[0] is None (producer returns None)
    # processed_events[1] is the list from consumer
    return processed_events[1]  # type: ignore[return-value]


async def rank5_demo() -> None:
    print("Rank 5 — Professional (async pipeline)")
    events = await run_game_event_pipeline(total_events=5)
    print(f"Total events processed: {len(events)}")
    print("Example processed event:", events[0] if events else "None")
    print("-" * 50)


# ===========================================================
# Main demo runner
# ===========================================================

async def main_demo() -> None:
    """
    Run all rank demos in order.
    You can comment out any rank you don't want to run.
    """
    await rank1_demo()
    await rank2_demo()
    await rank3_demo()
    await rank4_demo()
    await rank5_demo()


if __name__ == "__main__":
    # Run all coroutine demos when this file is executed directly.
    asyncio.run(main_demo())
