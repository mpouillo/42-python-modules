from ex0.Card import Card
from ex0.CreatureCard import CreatureCard
from ex1.SpellCard import SpellCard
from ex1.ArtifactCard import ArtifactCard
import random


class Deck():
    def __init__(self, cards: list = []):
        self.cards = cards

    @property
    def cards(self) -> list:
        return self.__cards

    @cards.setter
    def cards(self, cards) -> None:
        self.__cards = cards

    def add_card(self, card: Card) -> None:
        self.cards.append(card)

    def remove_card(self, card_name: str) -> None:
        self.cards.remove(card_name)

    def shuffle(self) -> None:
        random.shuffle(self.cards)

    def draw_card(self) -> Card:
        self.shuffle()
        card = next(iter(self.cards), None)
        if card is not None:
            self.cards.remove(card)
            return card

    def get_deck_stats(self) -> dict:
        return {
            "total_cards": len(self.cards),
            "creatures": sum(
                1 for card in self.cards if type(card) is CreatureCard
            ),
            "spells": sum(
                1 for card in self.cards if type(card) is SpellCard
            ),
            "artifacts": sum(
                1 for card in self.cards if type(card) is ArtifactCard
            ),
            "avg_cost": round(sum(
                card.cost for card in self.cards) / len(self.cards),
                1)
        }
