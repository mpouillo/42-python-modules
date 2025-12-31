#!/usr/bin/env python3

class Plant:
    def __init__(self, name: str="None", height: int=0, lifetime: int=0):
        self.name: str = name
        self.height: int = height
        self.lifetime: int = lifetime

    def grow(self, size=1):
        self.height += size

    def age(self, days=1):
        self.lifetime += days

    def get_info(self):
        print(f"{self.name}: {self.height}cm, {self.lifetime} days old")


def ft_plant_growth():
    start_height: int = 25
    plant: Plant = Plant("Rose", start_height, 30)
    day: int = 1
    print(f"=== Day {day} ===")
    plant.get_info()
    for _ in range (1, 7):
        day += 1
        plant.grow(1)
    print(f"=== Day {day} ===")
    plant.get_info()
    print(f"Growth this week: +{plant.height - start_height}")


if __name__ == "__main__":
    ft_plant_growth()
