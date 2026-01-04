#!/usr/bin/env python3

class Plant:
    def __init__(self,
                 name: str = "None",
                 height: int = 0,
                 age: int = 0):
        self.name = name
        self.height = height
        self.age = age


def ft_garden_data():
    plants = [Plant("Rose", 25, 30),
              Plant("Sunflower", 80, 45),
              Plant("Cactus", 15, 120)]
    print("=== Garden Plant Registry ===")
    for plant in plants:
        print(f"{plant.name}: {plant.height}cm, {plant.age} days old")


if __name__ == "__main__":
    ft_garden_data()
