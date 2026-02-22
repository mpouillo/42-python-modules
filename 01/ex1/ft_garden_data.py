#!/usr/bin/env python3
"""Python Module 01 Exercise 1."""


class Plant:
    """Create a plant object."""

    def __init__(self,
                 name: str = "None",
                 height: int = 0,
                 days: int = 0):
        """
        Initialize plant object with name, height and days.

        Keyword arguments:
        name        name of the plant object
        height      height of the plant object, in cm
        days        age of the plant object, in days
        """
        self.name: str = name
        self.height: int = height
        self.days: int = days


if __name__ == "__main__":
    rose = Plant("Rose", 25, 30)
    sunflower = Plant("Sunflower", 80, 45)
    cactus = Plant("Cactus", 15, 120)

    print("=== Garden Plant Registry ===")

    print(f"{rose.name}: {rose.height}cm, "
          f"{rose.days} day{'s' if rose.days > 1 else ''} old")
    print(f"{sunflower.name}: {sunflower.height}cm, "
          f"{sunflower.days} day{'s' if sunflower.days > 1 else ''} old")
    print(f"{cactus.name}: {cactus.height}cm, "
          f"{cactus.days} day{'s' if cactus.days > 1 else ''} old")
