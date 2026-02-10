from ex0.Card import Card
from ex0.CreatureCard import CreatureCard
from ex1.SpellCard import SpellCard
from ex1.ArtifactCard import ArtifactCard
from ex3.CardFactory import CardFactory
import random


class FantasyCardFactory(CardFactory):
    def create_creature(self, name_or_power: str | int | None = None) -> Card:
        match name_or_power:
            case "dragon":
                card = CreatureCard("Fire Dragon", 5, "Legendary", 5, 7)
            case "goblin":
                card = CreatureCard("Goblin", 3, "Uncommon", 2, 3)
            case 5:
                card = CreatureCard("Fire Dragon", 5, "Legendary", 5, 7)
            case 3:
                card = CreatureCard("Goblin", 3, "Uncommon", 2, 3)
            case _:
                pass
        return card

    def create_spell(self, name_or_power: str | int | None = None) -> Card:
        match name_or_power:
            case "fireball":
                card = SpellCard(
                    "Fireball", 2, "Uncommon", "Deal 3 damage to target"
                )
            case "lightning_bolt":
                card = SpellCard(
                    "Lighting Bolt", 3, "Rare", "Deal 5 damage to target"
                )
            case 3:
                card = SpellCard(
                    "Fireball", 2, "Uncommon", "Deal 3 damage to target"
                )
            case 5:
                card = SpellCard(
                    "Lighting Bolt", 3, "Rare", "Deal 5 damage to target"
                )
            case _:
                pass
        return card

    def create_artifact(self, name_or_power: str | int | None = None) -> Card:
        match name_or_power:
            case "mana_ring":
                card = ArtifactCard(
                    "Mana Ring", 2, "Uncommon", 10, "Permanent +3 mana"
                )
            case 2:
                card = ArtifactCard(
                    "Mana Ring", 2, "Uncommon", 10, "Permanent +3 mana"
                )
            case _:
                pass
        return card

    def create_themed_deck(self, size: int) -> dict:
        deck = {}
        i = 0
        while i < size:
            card = random.choice([
                self.create_creature(
                    random.choice(self.get_supported_types().get("creatures"))
                ),
                self.create_spell(
                    random.choice(self.get_supported_types().get("spells"))
                ),
                self.create_artifact(
                    random.choice(self.get_supported_types().get("artifacts"))
                )
            ])
            if card and (card.name not in deck.keys()):
                deck.update({card.name: card})
                i += 1
        return deck

    def get_supported_types(self) -> dict:
        return {
            "creatures": ["dragon", "goblin"],
            "spells": ["fireball", "lightning_bolt"],
            "artifacts": ["mana_ring"]
        }
