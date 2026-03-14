#!/usr/bin/env python3

from typing import Any, Callable


def mage_counter() -> Callable:
    _count = 0

    def counter() -> int:
        nonlocal _count
        _count += 1
        return _count

    return counter


def spell_accumulator(initial_power: int) -> Callable:
    _power = initial_power

    def accumulator(additional_power: int = 0) -> int:
        nonlocal _power
        _power += additional_power
        return _power

    return accumulator


def enchantment_factory(enchantment_type: str) -> Callable:
    def enchanter(item_name: str) -> str:
        nonlocal enchantment_type
        return f"{enchantment_type} {item_name}"
    return enchanter


def memory_vault(*args, **kwargs) -> dict[str, Callable]:
    _storage: dict[str, Callable] = {}

    def store(key: str, value: Any) -> None:
        _storage[key] = value

    def recall(key: str) -> Any:
        nonlocal _storage
        return _storage.get(key, "Memory not found")

    return {"store": store, "recall": recall}


if __name__ == "__main__":
    print("Testing mage counter...")
    counter = mage_counter()
    for i in range(3):
        print(f"Call {i + 1}:", counter())

    print("\nTesting spell accumulator...")
    accumulator = spell_accumulator(5)
    print("Starting with 5")
    for i in range(3):
        print(f"Adding {i + 1}:", accumulator(i + 1))

    print("\nTesting enchantment factory...")
    enchanter = enchantment_factory("Flaming")
    print(enchanter("Sword"))
    print(enchanter("Shield"))

    print("\nTesting memory vault...")
    vault = memory_vault()
    print("Adding {\"test_key\": \"test_value\"}...")
    vault['store']("test_key", "test_value")
    print("Retrieving test_key:", vault['recall']("test_key"))
    print("Retrieving missing_key:", vault['recall']("missing_key"))
