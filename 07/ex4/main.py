#!/usr/bin/env python3

from ex4.TournamentPlatform import TournamentPlatform
from ex4.TournamentCard import TournamentCard
from pprint import pprint

if __name__ == "__main__":
    print("=== DataDeck Tournament Platform ===")

    platform = TournamentPlatform()

    print("\nRegistering Tournament Cards...")

    card1 = TournamentCard("Fire Dragon", 5, "Legendary", 6, 2, 6)
    card1_id = platform.register_cards(card1)
    card2 = TournamentCard("Ice Wizard", 4, "Rare", 2, 3, 8)
    card2_id = platform.register_cards(card2)
    card3 = TournamentCard("Snake", 1, "Common", 1, 1, 1)
    card3_id = platform.register_cards(card3)
    card3.update_wins(10)

    print(f"\n{card1.name} (ID: {card1_id}):\n"
          "- Interfaces: [Card, Combatable, Rankable]\n"
          f"- Rating: {card1.calculate_rating()}\n"
          f"- Record: 0-0")

    print(f"\n{card2.name} (ID: {card2_id}):\n"
          "- Interfaces: [Card, Combatable, Rankable]\n"
          f"- Rating: {card2.calculate_rating()}\n"
          f"- Record: 0-0")

    print(f"\n{card3.name} (ID: {card3_id}):\n"
          "- Interfaces: [Card, Combatable, Rankable]\n"
          f"- Rating: {card3.calculate_rating()}\n"
          f"- Record: 0-0")

    print("\nCreating tournament match...")

    print("Match result:")
    pprint(platform.create_match(card1_id, card2_id), sort_dicts=False)

    print("\nTournament Leaderboard:")

    for i, card in enumerate(platform.get_leaderboard(), 1):
        print(f"{i}. {card.name} - Rating: {card.calculate_rating()} "
              f"({card.wins}-{card.losses})")

    print("\nPlatform Report:")

    pprint(platform.generate_tournament_report(), sort_dicts=False)

    print("\n=== Tournament Platform Successfully Deployed! ===")
    print("All abstract patterns working together harmoniously!")
