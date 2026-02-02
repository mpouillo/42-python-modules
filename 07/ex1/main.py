#!/usr/bin/env python3

from ex0.CreatureCard import CreatureCard
from ex1.SpellCard import SpellCard
from ex1.ArtifactCard import ArtifactCard
from ex1.Deck import Deck
from pprint import pprint

if __name__ == "__main__":
    print("=== DataDeck Deck Builder ===")

    deck = Deck([
        CreatureCard("Fire Dragon", 5, "Legendary", 7, 5),
        SpellCard("Lighting Bolt", 3, "Uncommon", "Deal 3 damage to target"),
        ArtifactCard("Mana Crystal", 2, "Rare", 10,
                     "Permanent +1 mana per turn"),
    ])
    deck_stats = deck.get_deck_stats()

    print("\nBuilding deck with different card types...")
    print("Deck stats:")
    pprint(deck_stats, sort_dicts=False)

    print("\nDrawing and playing cards:")

    card = 1
    while card:
        card = deck.draw_card()
        if card is not None:
            print(f"\nDrew: {card.name} ({card.__name__})")
            print("Play result:")
            pprint(card.play({
                "available_mana": 999,
                "target": [
                    CreatureCard("Goblin", 2, "Common", 4, 3)
                ]}), sort_dicts=False)

    print("\nPolymorphism in action: "
          "Same interface, different card behaviors")
