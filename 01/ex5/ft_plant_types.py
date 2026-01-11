#!/usr/bin/env python3
"""Python Module 01 Exercise 5."""


class Plant:
    """Create a plant object."""

    def __init__(self, name: str = "None", height: int = 0, age: int = 0):
        """
        Initialize plant object.

        Keyword arguments:
        name    -- name of the plant object
        height  -- height of the plant object
        age     -- age of the plant object
        """
        self.set_name(name)
        self.set_height(height)
        self.set_age(age)

    def set_name(self, name: str) -> None:
        """Set plant name."""
        self._name = name

    def set_height(self, height: int) -> None:
        """Set plant height."""
        if height < 0:
            print(f"Invalid operation attempted: height {height}cm [REJECTED]")
            print("Security: Negative height rejected")
        else:
            self._height = height

    def set_age(self, age: int) -> None:
        """Set plant age."""
        if age < 0:
            print(
                "Invalid operation attempted: age "
                f"{age} day{'s' if age != -1 else ''} [REJECTED]"
                )
            print("Security: Negative age rejected")
        else:
            self._age = age

    def get_name(self) -> str:
        """Return plant name."""
        return (self._name)

    def get_height(self) -> int:
        """Return plant height."""
        return (self._height)

    def get_age(self) -> int:
        """Return plant age."""
        return (self._age)

    def get_info(self) -> str:
        """Return information (name, height, age) about the plant."""
        return (
            f"{self.get_name()} ({type(self).__name__}): "
            f"{self.get_height()}cm, {self.get_age()} "
            f"day{'s' if self.get_age() != 1 else ''}")


class Flower(Plant):
    """Create a flower object."""

    def __init__(self, name: str, height: int, age: int, color: str):
        """
        Initialize flower object.

        Keyword arguments:
        name    -- name of the flower object
        height  -- height of the flower object
        age     -- age of the flower object
        color   -- color of the flower object
        """
        super().__init__(name, height, age)
        self.set_color(color)
        self._bloom = False

    def set_color(self, color: str = "None") -> None:
        """Set flower color."""
        self._color = color

    def get_color(self) -> str:
        """Return flower color."""
        return (self._color)

    def bloom(self) -> None:
        """Set bloom to True and print info."""
        self._bloom = True
        print(f"{self.get_name()} is blooming beautifully!")

    def get_info(self) -> str:
        """Return information (name, height, age, color) about the plant."""
        return f"{super().get_info()}, {self.get_color()} color"


class Tree(Plant):
    """Create a tree object."""

    def __init__(self, name: str, height: int, age: int, trunk_diameter: int):
        """
        Initialize tree object.

        Keyword arguments:
        name            -- name of the tree object
        height          -- height of the tree object
        age             -- age of the tree object
        trunk_diameter  -- diameter of the tree object
        """
        super().__init__(name, height, age)
        self.set_trunk_diameter(trunk_diameter)
        self._shade = 67

    def set_trunk_diameter(self, diameter: int) -> None:
        """Set tree diameter."""
        self._trunk_diameter = diameter

    def get_diameter(self) -> int:
        """Return tree diameter."""
        return (self._trunk_diameter)

    def produce_shade(self) -> None:
        """Print information about the shade cast by the tree."""
        print(f"{self.get_name()} provides "
              f"{self._shade} square meters of shade")

    def get_info(self) -> str:
        """Return information (name, height, age, diameter) about the plant."""
        return f"{super().get_info()}, {self.get_diameter()}cm diameter"


class Vegetable(Plant):
    """Create a vegetable object."""

    def __init__(self, name: str, height: int, age: int, season: str):
        """
        Initialize vegetable object.

        Keyword arguments:
        name    -- name of the vegetable object
        height  -- height of the vegetable object
        age     -- age of the vegetable object
        season  -- optimal harvest season
        """
        super().__init__(name, height, age)
        self.set_harvest_season(season)

    def set_harvest_season(self, season: str) -> None:
        """Set vegetable harvest season."""
        self._harvest_season = season

    def get_harvest_season(self) -> str:
        """Return vegetable harvest season."""
        return (self._harvest_season)

    def set_nutritional_value(self, value: str) -> None:
        """Set vegetable nutritional value."""
        self._nutritional_value = value

    def get_nutritional_value(self) -> str:
        """Return vegetable nutritional value."""
        return (f"{self.get_name()} is rich in {self._nutritional_value}")

    def get_info(self) -> str:
        """Return information (name, height, age, harvest season) \
        about the plant."""
        return f"{super().get_info()}, {self.get_harvest_season()}"


if __name__ == "__main__":
    print("=== Garden Plant Types ===")

    flower = Flower("Begonia", 30, 60, "pink")
    print(f"{flower.get_info()}")
    flower.bloom()

    tree = Tree("Weeping Willow", 1500, 10950, 300)
    print(f"\n{tree.get_info()}")
    tree.produce_shade()

    vegetable = Vegetable("Sweet potato", 20, 10, "Autumn")
    vegetable.set_nutritional_value("vitamin A")
    print(f"\n{vegetable.get_info()}")
    print(vegetable.get_nutritional_value())
