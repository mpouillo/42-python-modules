from ex0.CreatureCard import CreatureCard
from ex1.SpellCard import SpellCard
from ex3.GameStrategy import GameStrategy


class AggressiveStrategy(GameStrategy):
    def execute_turn(self, hand: list, battlefield: list) -> dict:
        cards_played = []
        mana_used = 0
        targets_attacked = []
        damage_dealt = 0
        for card in hand:
            if type(card) is SpellCard:
                cards_played.append(card.name)
                mana_used += card.cost
                damage_dealt += (
                    card.resolve_effect(battlefield).get("damage", 0)
                )
            elif type(card) is CreatureCard:
                target = next(iter(battlefield), None)
                mana_used += card.cost
                if target:
                    cards_played.append(card.name)
                    result = card.attack_target(target)
                    damage_dealt += result.get("damage_dealt", 0)
                    if result.get("target") is not None:
                        targets_attacked.append(result.get("target"))
        return {
            "cards_played": cards_played,
            "mana_used": mana_used,
            "targets_attacked": targets_attacked,
            "damage_dealt": damage_dealt
        }

    def get_strategy_name(self) -> str:
        return "AggressiveStrategy"

    def prioritize_targets(self, available_targets: list) -> list:
        return available_targets
