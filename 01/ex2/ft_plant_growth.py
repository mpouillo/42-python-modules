#!/usr/bin/env python3
"""Python Module 01 Exercise 2."""


class Plant:
    """Create a plant object."""

    def __init__(self,
                 name: str = "None",
                 height: int = 0,
                 lifetime: int = 0):
        """
        Initialize plant object with name, height and lifetime.

        Keyword arguments:
        name        -- name of the plant object
        height      -- height of the plant object
        lifetime    -- age of the plant object
        """
        self.name: str = name
        self.height: int = height
        self.lifetime: int = lifetime

    def grow(self, size: int = 1) -> None:
        """Increase plant size by 'size'."""
        self.height += size

    def age(self, days: int = 1) -> None:
        """Increase plant lifetime by 'days'."""
        self.lifetime += days

    def get_info(self) -> str:
        """Return information (name, height, lifetime) about the plant."""
        return f"{self.name}: {self.height}cm, {self.lifetime} days old"


if __name__ == "__main__":
    start_height = 25
    plant = Plant("Rose", start_height, 30)

    day = 1
    print(f"=== Day {day} ===")
    print(f"{plant.get_info()}")

    day += 6
    plant.grow(6)
    plant.age(6)

    print(f"=== Day {day} ===")
    print(f"{plant.get_info()}")

    print(f"Growth this week: +{plant.height - start_height}")
