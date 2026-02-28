from abc import ABC, abstractmethod


class Card(ABC):
    def __init__(self, name: str, cost: int, rarity: str) -> None:
        self.name = name
        self.cost = cost
        self.rarity = rarity

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str) -> None:
        if name is None:
            name = "None"
        self.__name = name

    @property
    def cost(self) -> int:
        return self.__cost

    @cost.setter
    def cost(self, cost: int) -> None:
        self.__cost = max(0, cost)

    @property
    def rarity(self) -> str:
        return self.__rarity

    @rarity.setter
    def rarity(self, rarity: str) -> None:
        if rarity is None:
            rarity = "Undefined"
        self.__rarity = rarity

    @abstractmethod
    def play(self, game_state: dict) -> dict:
        return game_state

    def get_card_info(self) -> dict:
        return {
            "name": self.name,
            "cost": self.cost,
            "rarity": self.rarity,
        }

    def is_playable(self, available_mana: int) -> bool:
        return available_mana > self.cost
