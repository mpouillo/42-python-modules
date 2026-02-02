#!/usr/bin/env python3

from ex0.CreatureCard import CreatureCard
from pprint import pprint

if __name__ == "__main__":
    print("=== DataDeck Card Foundation ===")

    print("\nTesting Abstract Class Design:")
    card_name = "Fire Dragon"
    card_cost = 5
    dragon = CreatureCard(card_name, card_cost, "Legendary", 7, 5)
    goblin = CreatureCard("Goblin Warrior", 2, "Common", 5, 3)
    mana = 6

    print("\nCreatureCard Info:")
    pprint(dragon.get_card_info(), sort_dicts=False)

    print(f"\nPlaying {dragon.name} with {mana} mana available:")
    print("Playable:", dragon.is_playable(6))
    print("Play result:")
    pprint(dragon.play({"available_mana": mana}), sort_dicts=False)

    print(f"\n{dragon.name} attacks {goblin.name}:")
    print("Attack result:")
    pprint(dragon.attack_target(goblin), sort_dicts=False)

    mana = 3
    print(f"\nTesting insufficient mana ({mana} available):")
    print("Playable:", dragon.is_playable(mana))

    print("\nAbstract pattern successfully demonstrated!")
