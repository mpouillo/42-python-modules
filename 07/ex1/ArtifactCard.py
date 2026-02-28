from ex0.Card import Card


class ArtifactCard(Card):
    def __init__(self,
                 name: str,
                 cost: int,
                 rarity: str,
                 durability: int,
                 effect: str) -> None:
        super().__init__(name, cost, rarity)
        self.durability = durability
        self.effect = effect
        self.__name__ = "Artifact"

    @property
    def durability(self) -> int:
        return self.__durability

    @durability.setter
    def durability(self, durability: int) -> None:
        self.__durability = max(0, durability)

    @property
    def effect(self) -> str:
        return self.__effect

    @effect.setter
    def effect(self, effect: str) -> None:
        self.__effect = effect

    def play(self, game_state: dict) -> dict:
        try:
            if self.is_playable(game_state.get("available_mana")):
                effect = self.activate_ability().get("effect")
                return {"card_played": self.name,
                        "mana_used": self.cost,
                        "effect": effect}
        except Exception:
            pass

    def activate_ability(self) -> dict:
        if self.durability > 0:
            self.durability -= 1
            return {"effect": self.effect,
                    "durability": self.durability}
