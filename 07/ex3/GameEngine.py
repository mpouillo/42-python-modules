from ex3.CardFactory import CardFactory
from ex3.GameStrategy import GameStrategy


class GameEngine:
    def configure_engine(self,
                         factory: CardFactory,
                         strategy: GameStrategy) -> None:
        self.factory = factory
        self.strategy = strategy
        self.turns = 0
        self.total_damage = 0
        self.total_cards_created = 0

    def simulate_turn(self) -> dict:
        deck_size = 3
        hand = self.factory.create_themed_deck(deck_size)
        enemy_hand = self.factory.create_themed_deck(deck_size)
        turn = self.strategy.execute_turn(
            [card for card in hand.values()],
            [card for card in enemy_hand.values()])
        self.turns += 1
        self.total_damage += turn.get("damage_dealt")
        self.total_cards_created += deck_size
        return turn

    def get_engine_status(self) -> dict:
        return {
            "turns_simulated": self.turns,
            "strategy_used": self.strategy.get_strategy_name(),
            "total_damage": self.total_damage,
            "cards_created": self.total_cards_created
        }
