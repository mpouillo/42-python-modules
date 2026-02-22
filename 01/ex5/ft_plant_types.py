#!/usr/bin/env python3
"""Python Module 01 Exercise 5."""


class Plant:
    """Create a plant object."""

    def __init__(self,
                 name: str = "None",
                 height: int = 0,
                 age: int = 0):
        """
        Initialize plant object with name, height and age.

        Keyword arguments:
        name    -- name of the plant object
        height  -- height of the plant object, in cm
        age     -- age of the plant object, in days
        """
        self.set_name(name)
        self.set_height(height)
        self.set_age(age)

    def set_name(self, name: str) -> None:
        """Set plant name."""
        self.__name = name

    def set_height(self, height: int) -> None:
        """Securely set plant height."""
        if height < 0:
            print("Security: Negative height rejected")
        else:
            self.__height = height

    def set_age(self, age: int) -> None:
        """Securely set plant age."""
        if age < 0:
            print("Security: Negative age rejected")
        else:
            self.__age = age

    def get_name(self) -> str:
        """Return plant name."""
        return self.__name

    def get_height(self) -> int:
        """Return plant height."""
        return self.__height

    def get_age(self) -> int:
        """Return plant age."""
        return self.__age

    def get_info(self) -> str:
        """Return information (name, height, days) about the plant."""
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

    def set_color(self, color: str = "None") -> None:
        """Set flower color."""
        self._color = color

    def get_color(self) -> str:
        """Return flower color."""
        return (self._color)

    def bloom(self) -> None:
        """Print info about bloom status."""
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

    def set_trunk_diameter(self, diameter: int) -> None:
        """Set tree diameter."""
        self.__trunk_diameter = diameter

    def get_diameter(self) -> int:
        """Return tree diameter."""
        return (self.__trunk_diameter)

    def produce_shade(self) -> None:
        """Print information about the shade cast by the tree."""
        print(f"{self.get_name()} provides 78 square meters of shade")

    def get_info(self) -> str:
        """Return information (name, height, age, diameter) about the plant."""
        return f"{super().get_info()}, {self.get_diameter()}cm diameter"


class Vegetable(Plant):
    """Create a vegetable object."""

    def __init__(self, name: str, height: int, age: int,
                 season: str, nutritional_value: str = "None"):
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
        self.set_nutritional_value(nutritional_value)

    def set_harvest_season(self, season: str) -> None:
        """Set vegetable harvest season."""
        self.__harvest_season = season

    def get_harvest_season(self) -> str:
        """Return vegetable harvest season."""
        return (self.__harvest_season)

    def set_nutritional_value(self, value: str) -> None:
        """Set vegetable nutritional value."""
        self.__nutritional_value = value

    def get_nutritional_value(self) -> str:
        """Return vegetable nutritional value."""
        return (f"{self.get_name()} is rich in {self.__nutritional_value}")

    def get_info(self) -> str:
        """Return information (name, height, age, harvest season) \
        about the plant."""
        return f"{super().get_info()}, {self.get_harvest_season()} harvest"


if __name__ == "__main__":
    print("=== Garden Plant Types ===")

    flower = Flower("Rose", 25, 30, "red")

    print(f"{flower.get_info()}")
    flower.bloom()

    tree = Tree("Oak", 500, 1825, 50)

    print(f"\n{tree.get_info()}")
    tree.produce_shade()

    vegetable = Vegetable("Tomato", 80, 90, "summer", "vitamin C")

    print(f"\n{vegetable.get_info()}")
    print(vegetable.get_nutritional_value())
