from ex0.Card import Card
from ex2.Combatable import Combatable
from ex4.Rankable import Rankable


class TournamentCard(Card, Combatable, Rankable):
    def __init__(self,
                 name: str,
                 cost: int,
                 rarity: str,
                 physical_attack: int,
                 defense: int,
                 health: int):
        super().__init__(name, cost, rarity)
        self.physical_attack = physical_attack
        self.defense = defense
        self.health = health
        self.wins = 0
        self.losses = 0

    def play(self, game_state: dict) -> dict:
        try:
            if self.is_playable(game_state.get("available_mana")):
                return {"card_played": self.name,
                        "mana_used": self.cost,
                        "effect": "Card played"}
        except Exception:
            pass

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
        return {"wins": self.wins,
                "losses": self.losses}

    def calculate_rating(self) -> int:
        return 1200 + (16 * (self.wins - self.losses))

    def update_wins(self, wins: int) -> None:
        if wins > 0:
            self.wins += wins

    def update_losses(self, losses: int) -> None:
        if losses > 0:
            self.losses += losses

    def get_rank_info(self) -> dict:
        return "idk bro"
