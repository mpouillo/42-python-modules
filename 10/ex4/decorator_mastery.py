#!/usr/bin/env python3

import time
import inspect
from functools import wraps
from typing import Any, Callable


def spell_timer(func: Callable) -> Callable:
    @wraps(func)
    def timer(*args, **kwargs) -> Any:
        start = time.time()
        print(f"Casting {func.__name__}...")
        res = func(*args, **kwargs)
        end = time.time()
        print("Function completed in {:f} seconds".format(end - start))
        return res
    return timer


def power_validator(min_power: int) -> Callable:
    def decorator(func: Callable) -> Callable:
        @wraps(func)
        def wrapper(*args, **kwargs) -> Any:
            sig = inspect.signature(func)
            bound_args = sig.bind(*args, **kwargs)
            power = bound_args.arguments.get('power', -1)
            if power >= min_power:
                return func(*args, **kwargs)
            else:
                return "Insufficient power for this spell"
        return wrapper
    return decorator


def retry_spell(max_attempts: int) -> Callable:
    def decorator(func: Callable) -> Callable:
        @wraps(func)
        def wrapper(*args, **kwargs) -> Any:
            for attempt in range(1, max_attempts + 1):
                try:
                    return func(*args, **kwargs)
                except Exception:
                    print("Spell failed, retrying..."
                          f"(attempt {attempt}/{max_attempts})")
            return f"Spell casting failed after {attempt} attempts"
        return wrapper
    return decorator


class MageGuild:
    @staticmethod
    def validate_mage_name(name: str) -> bool:
        if len(name) < 3:
            return False
        for c in name:
            if not c.isalpha() and not c.isspace():
                return False
        return True

    @power_validator(min_power=10)
    def cast_spell(self, spell_name: str, power: int) -> str:
        return f"Successfully cast {spell_name} with power {power}"


if __name__ == "__main__":
    print("Testing spell timer...")

    @spell_timer
    def cast_spell(spell: str) -> str:
        return f"{spell.capitalize()} cast!"

    print("Result:", cast_spell("fireball"))

# ========================================== #

    print("\nTesting power validator...")

    @power_validator(min_power=50)
    def cast_fireball(power: int) -> str:
        return f"Fireball cast with {power} power"

    print("Result:", cast_fireball(50))
    print("Result:", cast_fireball(49))

# ========================================== #

    print("\nTesting retry spell...")
    power = 0

    @retry_spell(max_attempts=3)
    def cast_unstable_spell() -> str:
        import random
        if random.random() < 0.7:
            raise ValueError("Spell failed")
        return "Spell cast successfully"

    print(cast_unstable_spell())

# ========================================== #

    print("\nTesting MageGuild...")
    guild = MageGuild()
    print(guild.validate_mage_name("John Doe"))
    print(guild.validate_mage_name("johndoe727"))
    print(guild.cast_spell("Lightning", 15))
    print(guild.cast_spell("Fireball", 5))
