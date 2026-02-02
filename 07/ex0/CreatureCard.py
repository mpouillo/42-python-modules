from ex0.Card import Card


class CreatureCard(Card):
    def __init__(self,
                 name: str,
                 cost: int,
                 rarity: str,
                 attack: int,
                 health: int):
        super().__init__(name, cost, rarity)
        self.attack = attack
        self.health = health
        self.__name__ = "Creature"

    @property
    def attack(self) -> int:
        return self.__attack

    @attack.setter
    def attack(self, attack: int) -> None:
        self.__attack = max(0, attack)

    @property
    def health(self) -> int:
        return self.__health

    @health.setter
    def health(self, health: int) -> None:
        self.__health = max(0, health)

    def play(self, game_state: dict) -> dict:
        try:
            if self.is_playable(game_state.get("available_mana")):
                return {"card_played": self.name,
                        "mana_used": self.cost,
                        "effect": "Creature summoned to battlefield"}
        except Exception:
            pass

    def attack_target(self, target) -> dict:
        target.health -= self.attack
        return {
            "attacker": self.name,
            "target": target.name,
            "damage_dealt": self.attack,
            "combat_resolved": True if target.health == 0 else False
        }

    def get_card_info(self):
        info = super().get_card_info()
        info["type"] = "Creature"
        info["attack"] = self.attack
        info["health"] = self.health
        return info
