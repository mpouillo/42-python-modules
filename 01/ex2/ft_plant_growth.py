#!/usr/bin/env python3
"""Python Module 01 Exercise 2."""


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

    def grow(self, size: int = 1) -> None:
        """Increase plant size by 'size'."""
        self.height += size

    def age(self, days: int = 1) -> None:
        """Increase plant days by 'days'."""
        self.days += days

    def get_info(self) -> str:
        """Return information (name, height, days) about the plant."""
        return (f"{self.name}: {self.height}cm, "
                f"{self.days} day{'s' if self.days > 1 else ''} old")


if __name__ == "__main__":
    start_height = 25
    plant = Plant("Rose", start_height, 30)

    day = 1
    print(f"=== Day {day} ===")
    print(f"{plant.get_info()}")

    time_elapsed = 6
    day += time_elapsed
    plant.grow(time_elapsed)
    plant.age(time_elapsed)

    print(f"=== Day {day} ===")
    print(f"{plant.get_info()}")

    print(f"Growth this week: +{plant.height - start_height}")
