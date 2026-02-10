from ex3.CardFactory import CardFactory
from ex3.GameStrategy import GameStrategy


class GameEngine:
    def configure_engine(self,
                         factory: CardFactory,
                         strategy: GameStrategy) -> None:
        self.factory = factory
        self.strategy = strategy
        self.turns = 0

    def simulate_turn(self) -> dict:
        self.turns += 1
        hand = self.factory.create_themed_deck(3)
        turn = self.strategy.execute_turn(
            hand,
            [self.factory.create_themed_deck(3).values()]
        )
        return {
            "turns_simulated": self.turns,
            "strategy_used": self.strategy.get_strategy_name(),
            "total_damage": turn.get("damage_dealt", 0),
            "cards_created": len(hand)
        }

    def get_engine_status(self) -> dict:
        pass
