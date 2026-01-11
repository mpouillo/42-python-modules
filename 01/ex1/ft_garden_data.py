#!/usr/bin/env python3
"""Python Module 01 Exercise 1."""


class Plant:
    """Create a plant object."""

    def __init__(self,
                 name: str = "Unknown",
                 height: int = 0,
                 age: int = 0):
        """
        Initialize plant object with name, height and age.

        Keyword arguments:
        name    -- name of the plant object
        height  -- height of the plant object
        age     -- age of the plant object
        """
        self.name = name
        self.height = height
        self.age = age


if __name__ == "__main__":
    rose = Plant("Rose", 25, 30)
    sunflower = Plant("Sunflower", 80, 45)
    cactus = Plant("Cactus", 15, 120)

    print("=== Garden Plant Registry ===")

    print(f"{rose.name}: {rose.height}cm, {rose.age} days old")
    print(f"{sunflower.name}: {sunflower.height}cm, {sunflower.age} days old")
    print(f"{cactus.name}: {cactus.height}cm, {cactus.age} days old")
