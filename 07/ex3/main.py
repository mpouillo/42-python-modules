#!/usr/bin/env python3
from ex3.FantasyCardFactory import FantasyCardFactory
from ex3.AggressiveStrategy import AggressiveStrategy
from ex3.GameEngine import GameEngine
from pprint import pprint, pformat

if __name__ == "__main__":
    print("=== DataDeck Game Engine ===")

    factory = FantasyCardFactory()
    strategy = AggressiveStrategy()
    hand = factory.create_themed_deck(3)
    enemy = factory.create_themed_deck(3)

    print("\nConfiguring Fantasy Card Game...")
    print("Factory: FantasyCardFactory")
    print("Strategy:", strategy.get_strategy_name())
    print("Available types:", pformat(factory.get_supported_types()))

    print("\nSimulating aggressive turn...")
    cards = [f"{card.name} ({card.cost})" for card in hand.values()]
    print("Hand:", f"[{', '.join(cards)}]")

    print("\nTurn execution:")
    print("Strategy:", strategy.get_strategy_name())
    print("Actions:")
    pprint(strategy.execute_turn([card for card in hand.values()],
                                 [card for card in enemy.values()]),
           sort_dicts=False)

    game_engine = GameEngine()
    game_engine.configure_engine(factory, strategy)

    print("\nGame Report:")
    pprint(game_engine.simulate_turn())

    print("\nAbstract Factory + Strategy Pattern: "
          "Maximum flexibility achieved!")
