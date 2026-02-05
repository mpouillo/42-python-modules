from ex0.Card import Card
from ex2.Combatable import Combatable
from ex2.Magical import Magical


class EliteCard(Card, Combatable, Magical):
    def __init__(self,
                 name: str,
                 cost: int,
                 rarity: str,
                 physical_attack: int,
                 magical_attack: int,
                 defense: int,
                 health: int,
                 spell_cost: int):
        super().__init__(name, cost, rarity)
        self.physical_attack = physical_attack
        self.magical_attack = magical_attack
        self.defense = defense
        self.health = health
        self.spell_cost = spell_cost

    # Card
    def play(self, game_state: dict) -> dict:
        return super().play(game_state)

    # Combatable
    def attack(self, target) -> dict:
        target.defend(self.physical_attack)
        return {"attacker": self.name,
                "target": target.name,
                "damage": self.physical_attack,
                "combat_type": "melee"}

    def defend(self, incoming_physical_attack: int) -> dict:
        self.health = max(
            0, self.health - (incoming_physical_attack - self.defense)
        )
        return {"defender": self.name,
                "damage_taken": incoming_physical_attack,
                "damage_blocked": self.defense,
                "still_alive": True if self.health > 0 else False}

    def get_combat_stats(self) -> dict:
        return {"physical attack": self.physical_attack,
                "defense": self.defense,
                "health": self.health}

    # Magical
    def cast_spell(self, spell_name: str, targets: list) -> dict:
        return {"caster": self.name,
                "spell": spell_name,
                "targets": [t.name for t in targets],
                "mana_used": self.spell_cost}

    def channel_mana(self, amount: int) -> dict:
        return {"channeled": amount,
                "total_mana": 4 + amount}

    def get_magic_stats(self) -> dict:
        return {"base_mana": 4,
                "magical attack": self.magical_attack}
