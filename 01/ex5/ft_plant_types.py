#!/usr/bin/env python3

class Plant:
    def __init__(
            self,
            name: str = "None",
            height: int = 0,
            age: int = 0
            ):
        self.set_name(name)
        self.set_height(height)
        self.set_age(age)

    def set_name(self, name: str):
        self._name = name

    def set_height(self, height: int):
        if height < 0:
            print(f"Invalid operation attempted: height {height}cm [REJECTED]")
            print("Security: Negative height rejected")
        else:
            self._height = height

    def set_age(self, age: int):
        if age < 0:
            print(
                "Invalid operation attempted: age "
                f"{age} day{'s' if age != -1 else ''} [REJECTED]"
                )
            print("Security: Negative age rejected")
        else:
            self._age = age

    def get_name(self):
        return (self._name)

    def get_height(self):
        return (self._height)

    def get_age(self):
        return (self._age)

    def get_info(self):
        return (
            f"{self.get_name()} ({type(self).__name__}): "
            f"{self.get_height()}cm, {self.get_age()} "
            f"day{'s' if self.get_age() != 1 else ''}")


class Flower(Plant):
    def __init__(self, name, height, age, color):
        super().__init__(name, height, age)
        self._color = None
        self.set_color(color)
        self._bloom = False

    def set_color(self, color):
        self._color = color

    def get_color(self):
        return (self._color)

    def bloom(self):
        self._bloom = True
        print(f"{self.get_name()} is blooming.")

    def get_info(self):
        return f"{super().get_info()}, {self.get_color()}"


class Tree(Plant):
    def __init__(self, name, height, age, trunk_diameter):
        super().__init__(name, height, age)
        self.set_trunk_diameter(trunk_diameter)
        self._shade = False

    def set_trunk_diameter(self, diameter: int):
        self._trunk_diameter = diameter

    def get_diameter(self):
        return (self._trunk_diameter)

    def produce_shade(self):
        self._shade = True
        print("The tree casts a shadow.")

    def get_info(self):
        return f"{super().get_info()}, {self.get_diameter()}cm wide trunk"


class Vegetable(Plant):
    def __init__(self, name, height, age, season):
        super().__init__(name, height, age)
        self.set_harvest_season(season)
        self._nutritional_value: list = []

    def set_harvest_season(self, season: str):
        self._harvest_season = season

    def get_harvest_season(self):
        return (self._harvest_season)

    def set_nutritional_value(self, value: int, unit: str, type: str):
        self._nutritional_value.append(f"{type}: {value} {unit}")

    def get_nutritional_value(self):
        return (self._nutritional_value)

    def get_info(self):
        return f"{super().get_info()}, {self.get_harvest_season()}"


def ft_plant_types():
    flower = Flower("Begonia", 30, 60, "Pink")
    print(f"{flower.get_info()}")
    flower.set_height(-10)
    flower.bloom()
    print("")
    tree = Tree("Weeping Willow", 1500, 10950, 300)
    print(f"{tree.get_info()}")
    tree.produce_shade()
    print("")
    vegetable = Vegetable("Sweet potato", 20, 10, "Autumn")
    print(f"{vegetable.get_info()}")
    vegetable.set_nutritional_value("86", "kilocalories", "energy")
    vegetable.set_nutritional_value("20", "grams", "carbs")
    print(
        f"{vegetable.get_name()}'s nutritional values: "
        f"{vegetable.get_nutritional_value()}"
        )


if __name__ == "__main__":
    ft_plant_types()
