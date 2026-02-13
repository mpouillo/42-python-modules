#!/usr/bin/env python3
from ex3.FantasyCardFactory import FantasyCardFactory
from ex3.AggressiveStrategy import AggressiveStrategy
from ex3.GameEngine import GameEngine
from pprint import pprint, pformat

if __name__ == "__main__":
    print("=== DataDeck Game Engine ===")

    print("\nConfiguring Fantasy Card Game...")

    factory = FantasyCardFactory()
    strategy = AggressiveStrategy()

    print("Factory:", factory.__class__.__name__)
    print("Strategy:", strategy.get_strategy_name())
    print("Available types:",
          pformat(factory.get_supported_types(), sort_dicts=False))

    print("\nSimulating aggressive turn...")

    hand = factory.create_themed_deck(3)
    enemy = factory.create_themed_deck(3)
    cards = [f"{card.name} ({card.cost})" for card in hand.values()]
    e_cards = [f"{card.name} ({card.cost})" for card in enemy.values()]

    print("Hand:", f"[{', '.join(cards)}]")
    print("Enemy hand:", f"[{', '.join(e_cards)}]")

    print("\nTurn execution:")

    print("Strategy:", strategy.get_strategy_name())
    print("Actions:")
    pprint(strategy.execute_turn([card for card in hand.values()],
                                 [card for card in enemy.values()]),
           sort_dicts=False)

    print("\nGame Report:")

    game_engine = GameEngine()
    game_engine.configure_engine(factory, strategy)
    game_engine.simulate_turn()
    pprint(game_engine.get_engine_status(), sort_dicts=False)
    game_engine.simulate_turn()
    pprint(game_engine.get_engine_status(), sort_dicts=False)

    print("\nAbstract Factory + Strategy Pattern: "
          "Maximum flexibility achieved!")
