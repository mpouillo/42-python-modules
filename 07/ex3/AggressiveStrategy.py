from ex0.CreatureCard import CreatureCard
from ex1.SpellCard import SpellCard
from ex3.GameStrategy import GameStrategy


class AggressiveStrategy(GameStrategy):
    def execute_turn(self, hand: list, battlefield: list) -> dict:
        cards_played = []
        targets_attacked = set()
        mana_used = 0
        damage_dealt = 0

        battlefield = self.prioritize_targets(battlefield)

        for card in hand:
            if isinstance(card, SpellCard):
                cards_played.append(card.name)
                mana_used += card.cost
                effect = card.resolve_effect(battlefield)
                damage_dealt += effect.get("damage")
                target = effect.get("target")
                if target:
                    targets_attacked.add(target)
            elif isinstance(card, CreatureCard):
                target = None
                for b in battlefield:
                    if isinstance(b, CreatureCard):
                        target = b
                        break
                if target is not None:
                    mana_used += card.cost
                    cards_played.append(card.name)
                    result = card.attack_target(target)
                    damage_dealt += result.get("damage_dealt")
                    targets_attacked.add(result.get("target"))
        return {
            "cards_played": cards_played,
            "mana_used": mana_used,
            "targets_attacked": [*targets_attacked],
            "damage_dealt": damage_dealt
        }

    def get_strategy_name(self) -> str:
        return "AggressiveStrategy"

    def prioritize_targets(self, available_targets: list) -> list:
        return [card for card in available_targets
                if isinstance(card, CreatureCard) and card.health > 2]
