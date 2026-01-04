#!/usr/bin/env python3

class GardenError(Exception):
    pass


class PlantError(GardenError):
    def __init__(self, name: str):
        message = f"The {name} plant is wilting!"
        super().__init__(message)


class WaterError(GardenError):
    def __init__(self):
        message = "Not enough water in the tank!"
        super().__init__(message)


class Plant:
    def __init__(self,
                 name: str,
                 health: int = 10,
                 water: int = 10):
        self.name = name
        self.health = health
        self.water = water

    @property
    def health(self):
        return self._health

    @health.setter
    def health(self, value: int):
        self._health = value
        if (self.health <= 0):
            raise PlantError(self.name)

    @property
    def water(self):
        return self._water

    @water.setter
    def water(self, value: int):
        self._water = value
        if (self.water <= 0):
            raise WaterError

    def wilt(self, damage: int = 1):
        self.health -= damage

    def dry_up(self, dryness: int = 1):
        self.water -= dryness


def test_custom_errors():
    print("=== Custon Garden Errors Demo ===")
    tomato = Plant("tomato")

    print("\nTesting PlantError...")
    try:
        tomato.wilt(10)
    except PlantError as e:
        print(f"Caught PlantError: {e}")

    print("\nTesting WaterError...")
    try:
        tomato.dry_up(10)
    except WaterError as e:
        print(f"Caught WaterError: {e}")

    print("\nTesting catching all garden errors")
    try:
        tomato.wilt(1)
    except GardenError as e:
        print(f"Caught PlantError: {e}")
    try:
        tomato.dry_up(1)
    except GardenError as e:
        print(f"Caught WaterError: {e}")

    print("\nAll custom error types work correctly!")


if __name__ == "__main__":
    test_custom_errors()
