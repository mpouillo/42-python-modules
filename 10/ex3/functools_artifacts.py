#!/usr/bin/env python3

import operator
import time
from functools import reduce, partial, lru_cache, singledispatch
from typing import Any, Callable


def spell_reducer(spells: list[int], operation: str) -> int:
    match operation:
        case "add":
            return reduce(operator.add, spells)
        case "multiply":
            return reduce(operator.mul, spells)
        case "max":
            return reduce(max, spells)
        case "min":
            return reduce(min, spells)
        case _:
            return 0


def partial_enchanter(base_enchantment: Callable) -> dict[str, Callable]:
    return {
        "fire_enchant": partial(base_enchantment, 50, "fire"),
        "ice_enchant": partial(base_enchantment, 50, "ice"),
        "lightning_enchant": partial(base_enchantment, 50, "lightning")
    }


@lru_cache(maxsize=128)
def memoized_fibonacci(n: int) -> int:
    if n < 2:
        return n
    return memoized_fibonacci(n - 1) + memoized_fibonacci(n - 2)


def spell_dispatcher() -> Callable:

    @singledispatch
    def dispatcher(spell: Any):
        return f"Using {spell}"

    @dispatcher.register
    def _(spell: int):
        return f"Dealt {spell} damage"

    @dispatcher.register
    def _(spell: str):
        return f"Enchanted {spell}"

    @dispatcher.register
    def _(spell: list):
        output = []
        for s in spell:
            output.append(f"Cast {s}!")
        return output

    return dispatcher


if __name__ == "__main__":
    print("Testing spell reducer...")
    spells = [i * i for i in range(1, 6, 1)]
    print("List:", spells)
    print("Sum:", spell_reducer(spells, "add"))
    print("Product:", spell_reducer(spells, "multiply"))
    print("Max:", spell_reducer(spells, "max"))
    print("Min:", spell_reducer(spells, "min"))

    print("\nTesting partial enchanter...")
    func = (lambda power, element, target: (
        f"Enchanting {target} with lv{power} {element} element"
    ))
    enchanter = partial_enchanter(func)
    print(enchanter["fire_enchant"]("Sword"))
    print(enchanter["ice_enchant"]("Shield"))

    print("\nTesting memoized fibonacci...")
    for _ in range(3):
        start = time.time()
        print("Fib(10):", memoized_fibonacci(123))
        end = time.time()
        print("Execution time:", "{:f}".format(end - start))

    print("\nTesting spell dispatcher...")
    dispatcher = spell_dispatcher()
    print("Testing with '10':", dispatcher(10))
    print("Testing with 'sword':", dispatcher("sword"))
    print("Testing with ['fireball', 'lightning bolt']:",
          dispatcher(["fireball", "lightning bolt"]))
