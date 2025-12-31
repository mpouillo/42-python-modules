#! /usr/bin/env python3

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


def ft_plant_factory():
    print("=== Plant Factory Output ===")
    plants = [Plant("Lily of the Valley", 15, 10),
              Plant("Begonia", 30, 60),
              Plant("Spider Lily", 60, 200),
              Plant("Clover", 5, 1),
              Plant("Weeping Willow", 1500, 10950)]

    for plant in plants:
        print("Created: ", end="")
        plant.get_info()
    print(f"\nTotal plants created: {len(plants)}")

if __name__ == "__main__":
    ft_plant_factory()
