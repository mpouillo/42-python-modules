#!/usr/bin/env python3

from pprint import pprint


def artifact_sorter(artifacts: list[dict]) -> list[dict]:
    return sorted(artifacts, key=lambda item: item['power'], reverse=True)


def power_filter(mages: list[dict], min_power: int) -> list[dict]:
    return list(filter(lambda m: m['power'] >= min_power, mages))


def spell_transformer(spells: list[str]) -> list[str]:
    return list(map(lambda spell: "* " + spell + " *", spells))


def mage_stats(mages: list[dict]) -> dict:
    max_power = max([(lambda m: m['power'])(m) for m in mages])
    min_power = min([(lambda m: m['power'])(m) for m in mages])
    avg_power = round(sum([(lambda m: m['power'])(m) for m in mages])
                      / sum([(lambda _: 1)(m) for m in mages]), 2)
    return {
        "max_power": max_power,
        "min_power": min_power,
        "avg_power": avg_power
    }


if __name__ == "__main__":
    artifacts = [
        {'name': 'Ice Wand', 'power': 91, 'type': 'relic'},
        {'name': 'Wind Cloak', 'power': 115, 'type': 'accessory'},
        {'name': 'Earth Shield', 'power': 101, 'type': 'relic'},
        {'name': 'Water Chalice', 'power': 85, 'type': 'focus'}
    ]

    mages = [
        {'name': 'Nova', 'power': 86, 'element': 'shadow'},
        {'name': 'Luna', 'power': 85, 'element': 'fire'},
        {'name': 'Ash', 'power': 50, 'element': 'lightning'},
        {'name': 'Kai', 'power': 61, 'element': 'ice'},
        {'name': 'Riley', 'power': 100, 'element': 'fire'}
    ]

    spells = ['fireball', 'meteor', 'tsunami', 'lightning']

    print("Testing artifact sorter...")
    print("Before:")
    pprint(artifacts)
    print("After:")
    pprint(artifact_sorter(artifacts))

    print("\nTesting power filter (with value 80)...")
    print("Before:")
    pprint(mages)
    print("After:")
    pprint(power_filter(mages, 80))

    print("\nTesting spell transformer...")
    print("Before:")
    pprint(spells)
    print("After:")
    pprint(spell_transformer(spells))

    print("\nTesting mage stats...")
    print("Before:")
    pprint(mages)
    print("After:")
    pprint(mage_stats(mages))
