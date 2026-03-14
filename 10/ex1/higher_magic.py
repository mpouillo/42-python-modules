#!/usr/bin/env python3

from typing import Any, Callable


def spell_combiner(spell1: Callable, spell2: Callable) -> Callable:
    def combined(*args, **kwargs) -> tuple[Any, Any]:
        res1 = spell1(*args, **kwargs)
        res2 = spell2(*args, **kwargs)
        return (res1, res2)
    return combined


def power_amplifier(base_spell: Callable, multiplier: int) -> Callable:
    def amplified(*args, **kwargs):
        return base_spell(*args, **kwargs) * multiplier
    return amplified


def conditional_caster(condition: Callable, spell: Callable) -> Callable:
    def cast(*args, **kwargs) -> str:
        if condition(*args, **kwargs):
            return spell(*args, **kwargs)
        else:
            return "Spell fizzled"
    return cast


def spell_sequence(spells: list[Callable]) -> Callable:
    def sequence(*args, **kwargs) -> list[str | None]:
        res: list[str | None] = []
        for spell in spells:
            res.append(spell(*args, **kwargs))
        return res
    return sequence


if __name__ == "__main__":
    print("Testing spell combiner...")
    combined = spell_combiner(
        lambda target: f"Fireball hits {target}",
        lambda target: f"Heals {target}"
    )
    print("Combined spell result:", combined("Dragon"))

    print("\nTesting power amplifier...")
    original = (lambda target: 10)
    amplified = power_amplifier(original, 3)
    print("Original:", original("spell"), ", Amplified:", amplified(3))

    print("\nTesting conditional caster...")
    cast = conditional_caster(
        lambda spell: True if spell else False,
        lambda spell: "Fireball hits dragon" if spell is True else ""
    )
    print("Conditional casting result:", cast(False))

    print("\nTesting spell sequence...")
    sequence = spell_sequence([
        lambda target: f"Fireball hits {target}",
        lambda target: f"Heals {target}",
        lambda target: f"Fireball hits {target}",
        lambda target: f"Heals {target}"
    ])
    print("Spell sequence result:", sequence("Dragon"))
