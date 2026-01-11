#! /usr/bin/env python3
"""Python Module 01 Exercise 3."""


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


def ft_plant_factory(plants: list[tuple[str, int, int]]) -> None:
    """Easily create plants from a list of tuples."""
    print("=== Plant Factory Output ===")

    count = 0
    for plant in plants:
        print(f"Created: {Plant(*plant).get_info()}")
        count += 1

    print(f"\nTotal plants created: {count}")


if __name__ == "__main__":
    plants = [("Lily of the Valley", 15, 10),
              ("Begonia", 30, 60),
              ("Spider Lily", 60, 200),
              ("Clover", 5, 1),
              ("Weeping Willow", 1500, 10950)]
    ft_plant_factory(plants)
