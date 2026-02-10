from ex0.Card import Card
from ex0.CreatureCard import CreatureCard


class SpellCard(Card):
    def __init__(self,
                 name: str,
                 cost: int,
                 rarity: str,
                 effect_type: str):
        super().__init__(name, cost, rarity)
        self.effect_type = effect_type
        self.__name__ = "Spell"

    @property
    def effect_type(self) -> str:
        return self.__effect_type

    @effect_type.setter
    def effect_type(self, effect_type: str) -> None:
        self.__effect_type = effect_type

    def play(self, game_state: dict) -> dict:
        try:
            if self.is_playable(game_state.get("available_mana")):
                return {"card_played": self.name,
                        "mana_used": self.cost,
                        "effect": self.resolve_effect(
                            game_state.get("target")
                        )}
        except Exception:
            pass

    def resolve_effect(self, targets: list) -> dict:
        output = {}
        for target in targets:
            if type(target) is CreatureCard:
                if "damage" in self.effect_type.lower():
                    damage = 3
                    target.health -= damage
                    output.update({
                        "effect": f"Deal {damage} damage to target",
                        "damage": damage,
                        "heal": 0
                    })
                elif "heal" in self.effect_type.lower():
                    heal = 3
                    target.health += heal
                    output.update({
                        "effect": f"Heal {heal} health to target",
                        "damage": 0,
                        "heal": heal
                    })
                else:
                    output.update({
                        "effect": "Nothing happens",
                        "damage": 0,
                        "heal": 0
                    })
        return output
