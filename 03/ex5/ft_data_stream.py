#!/usr/bin/env python3

from typing import Iterator, Any, Generator
from collections.abc import Callable
import time
import random


ACTIONS = {
    "login": "logged in",
    "level_up": "leveled up",
    "death": "died",
    "kill": "killed monster",
    "logout": "logged out",
    "item_found": "found treasure"
}


def fibonacci_gen() -> Iterator[int]:
    a, b = 0, 1
    while True:
        yield a
        temp = a
        a = b
        b = temp + b


def prime_gen() -> Iterator[int]:
    a = 2
    while True:
        is_prime = True
        for b in range(2, a):
            if a % b == 0:
                is_prime = False
                break
        if is_prime:
            yield a
        a += 1


def time_wrapper(func: Callable[[Any], Any]) -> Callable[[Any], Any]:
    def wrapper(*args: Any, **kwargs: Any) -> Any:
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print("\nMemory usage: Constant (streaming)")
        print("Processing time:", "{:.5f}".format(end - start), "seconds")
        return result
    return wrapper


def event_generator() -> Generator[dict[str, str | int], None, None]:
    event_id = 0
    names = ["alice", "bob", "charlie", "diana", "eve", "frank"]
    event_types = [k for k in ACTIONS.keys()]
    while True:
        event_id += 1

        yield {
            'id': event_id,
            'player': random.choice(names),
            'level': random.randint(1, 50),
            'event_type': random.choice(event_types),
        }


if __name__ == "__main__":
    print("=== Game Data Stream Processor ===\n")

    print("Processing 1000 game events...\n")

    event_gen = event_generator()

    total_events = 0
    high_level = 0
    treasure = 0
    level_up = 0

    start_t = time.time()

    for _ in range(1000):
        event = next(event_gen)

        total_events += 1
        high_level += 1 if int(event['level']) >= 10 else 0
        treasure += 1 if event['event_type'] == "item_found" else 0
        level_up += 1 if event['event_type'] == "level_up" else 0

        if total_events <= 3:
            print(f"Event {event['id']}: "
                  f"Player {event['player']} (level {event['level']}): "
                  f"{ACTIONS[str(event['event_type'])]}")
        if total_events == 4:
            print("...")

    end_t = time.time()

    print("\n=== Stream Analytics ===")
    print("Total events processed:", total_events)
    print("High-level players (10+)", high_level)
    print("Treasure events:", treasure)
    print("Level-up events:", level_up)

    print("\nMemory usage: Constant (streaming)")
    print(f"Processing time: {round(end_t - start_t, 5)} seconds")

    print("\n=== Generator Demonstration ===")

    fib = fibonacci_gen()
    prime = prime_gen()

    print("Fibonacci sequence (first 10):",
          ", ".join(str(next(fib)) for _ in range(10)))
    print("Prime numbers (first 5):",
          ", ".join(str(next(prime)) for _ in range(5)))
