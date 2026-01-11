#!/usr/bin/env python3
"""Python Module 01 Exercise 6."""

from typing import Any


class Plant:
    """Create a plant object."""

    def __init__(
            self,
            name: str = "None",
            height: int = 0,
            age: int = 0
            ):
        """
        Initialize plant object.

        Keyword arguments:
        name    -- name of the plant object
        height  -- height of the plant object
        age     -- age of the plant object
        """
        self.name = name
        self.height = height
        self.age = age
        self.total_growth = 0

    def __str__(self) -> str:
        """Return information about the plant object."""
        return f"{self.name}: {self.height}cm"

    @property
    def name(self) -> str:
        """Update plant name."""
        return self._name

    @name.setter
    def name(self, name: str) -> None:
        self._name = name

    @property
    def height(self) -> int:
        """Update plant height."""
        return self._height

    @height.setter
    def height(self, height: int) -> None:
        if height < 0:
            raise ValueError(
                f"Invalid operation attempted: height {height}cm [REJECTED]"
                )
        else:
            self._height = height

    @property
    def age(self) -> int:
        """Update plant age."""
        return self._age

    @age.setter
    def age(self, age: int) -> None:
        if age < 0:
            raise ValueError(
                f"Invalid operation attempted: "
                f"age {age} day{'s' if age != -1 else ''} "
                f"[REJECTED]"
                )
        else:
            self._age = age

    @property
    def total_growth(self) -> int:
        """Update total plant growth."""
        return self._total_growth

    @total_growth.setter
    def total_growth(self, growth: int) -> None:
        self._total_growth = growth

    def grow(self, growth: int) -> None:
        """Increase plant height by 'growth'."""
        self.height += growth
        self.total_growth += growth

    def time_passes(self, time: int) -> None:
        """Increase plant age by 'time'."""
        self.age += time


class FloweringPlant(Plant):
    """Create a flowering plant object."""

    def __init__(
            self,
            name: str = "None",
            height: int = 0,
            age: int = 0,
            color: str = "unspecified color",
            bloom: bool = False
            ):
        """
        Initialize flowering plant object.

        Keyword arguments:
        name    -- name of the flowering plant object
        height  -- height of the flowering plant object
        age     -- age of the flowering plant object
        color   -- color of the flowering plant object
        bloom   -- blooming status of the flowering plant object
        """
        super().__init__(name, height, age)
        self.color = color
        self.bloom = bloom

    def __str__(self) -> str:
        """Return information about the flowering plant object."""
        string = super().__str__()
        string += f", {self.color} flowers"
        string += f"{' (blooming)' if self.bloom is True else ''}"
        return string

    @property
    def color(self) -> str:
        """Update flowering plant color."""
        return self._color

    @color.setter
    def color(self, color: str) -> None:
        self._color = color

    @property
    def bloom(self) -> bool:
        """Update flowering plant bloom status."""
        return self._bloom

    @bloom.setter
    def bloom(self, status: bool) -> None:
        self._bloom = status


class PrizeFlower(FloweringPlant):
    """Create a prize flower object."""

    def __init__(
            self,
            name: str = "None",
            height: int = 0,
            age: int = 0,
            color: str = "unspecified color",
            bloom: bool = False,
            prize: int = 0
            ):
        """
        Initialize prize flower object.

        Keyword arguments:
        name    -- name of the prize flower object
        height  -- height of the prize flower object
        age     -- age of the prize flower object
        color   -- color of the prize flower object
        bloom   -- blooming status of the prize flower object
        prize   -- prize value of the prize flower object
        """
        super().__init__(name, height, age, color, bloom)
        self.prize_value = prize

    def __str__(self) -> str:
        """Return information about the flowering plant object."""
        string = super().__str__()
        string += f", Prize points: {self.prize_value}"
        return string

    @property
    def prize_value(self) -> int:
        """Update prize flower prize value."""
        return self._prize_value

    @prize_value.setter
    def prize_value(self, prize_value: int) -> None:
        self._prize_value = prize_value


class GardenManager:
    """Manage multiple gardens containing plant objects."""

    def __init__(self) -> None:
        """Initialize GardenManager object."""
        self.gardens: dict[Any, Any] = {}

    @property
    def garden_count(self) -> int:
        """Return number of gardens managed."""
        return len(self.gardens)

    def validate_owner(self, owner: str) -> None:
        """Add owner to gardens list if it doesn't exist."""
        if owner not in self.gardens:
            self.gardens[owner] = []

    def add_plant(self, owner: str, plant: Plant) -> None:
        """Add plant object to owner's garden."""
        self.validate_owner(owner)
        self.gardens[owner].append(plant)
        print(f"Added {plant.name} to {owner}'s garden")

    def del_plant(self, owner: str, plant: Plant) -> None:
        """Remove plant object from owner's garden."""
        self.validate_owner(owner)
        self.gardens[owner].remove(plant)
        print(f"Removed {plant.name} from {owner}'s garden")

    def grow_plants(self, owner: str, growth: int = 1) -> None:
        """Grow all plant objects in owner's garden."""
        if owner in self.gardens:
            print(f"{owner} is helping all plants grow...")
            for plant in self.gardens[owner]:
                plant.grow(growth)
                print(f"{plant.name} grew {growth}cm")

    def age_plants(self, owner: str, time: int) -> None:
        """Age all plant objects in owner's garden."""
        for plant in self.gardens[owner]:
            plant.time_passes(time)

    @classmethod
    def create_garden_network(cls) -> Any:
        """Create and return an instance of GardenManager."""
        network = cls()
        return network

    def garden_report(self, owner: str) -> str:
        """Return a string containing information on owner's garden."""
        if owner in self.gardens:
            owned_plants = self.gardens.get(owner, [])
            regular, flowering, prize = 0, 0, 0
            growth = self.GardenStats.calculate_total_growth(owned_plants)
            string = f"=== {owner}'s Garden Report ===\n"
            string += "Plants in garden:\n"
            for plant in self.gardens[owner]:
                string += f"- {plant}\n"
                if isinstance(plant, PrizeFlower):
                    prize += 1
                elif isinstance(plant, FloweringPlant):
                    flowering += 1
                else:
                    regular += 1
            string += f"\nPlants added: {len(owned_plants)}"
            string += f", Total growth: {growth}cm"
            string += "\nPlant types: "
            string += f"{regular} regular, "
            string += f"{flowering} flowering, "
            string += f"{prize} prize flowers"
            return string
        else:
            return f"{owner} not found in the Garden Manager"

    class GardenStats:
        """Calculate garden statistics."""

        @staticmethod
        def calculate_score(plants: list[Plant]) -> int:
            """Return score value for a list of plant objects."""
            score = 0
            for p in plants:
                score += p.height
                score += p.total_growth
                if isinstance(p, PrizeFlower):
                    score += p.prize_value
            return score

        @staticmethod
        def calculate_total_growth(plants: list[Plant]) -> int:
            """Return total growth for a list of plant objects."""
            total_growth = 0
            for p in plants:
                total_growth += p.total_growth
            return total_growth

    def get_garden_score(self, owner: str) -> int:
        """Return garden score for owner."""
        plants = self.gardens.get(owner, [])
        return self.GardenStats.calculate_score(plants)

    def print_garden_scores(self) -> None:
        """Format and print garden score."""
        print("Garden scores - ", end="")
        string = ""
        for garden in self.gardens:
            string += f"{'' if string == '' else ', '}"
            string += f"{garden}: {self.get_garden_score(garden)}"
        print(string)

    def validate_height(self) -> None:
        """Check height for all plants in all managed gardens."""
        status = True
        for garden in self.gardens:
            for plant in self.gardens.get(garden, []):
                if plant.height > 400:
                    status = False
                    break
        print(f"Height validation test: {status}")


if __name__ == "__main__":
    print("=== Garden Management System Demo ===\n")

    gm = GardenManager.create_garden_network()
    gm.add_plant("Alice", Plant("Pine Tree", 358, 1500))
    gm.add_plant("Alice", FloweringPlant("Wisteria", 87, 10, "purple", True))
    gm.add_plant("Alice", PrizeFlower("Begonia", 33, 30, "pink", False, 10))
    gm.add_plant("Bob", FloweringPlant("Cosmos", 30, 5, "purple", False))
    gm.add_plant("Bob", PrizeFlower("Spider Lily", 40, 20, "red", True, 20))
    print("")

    gm.grow_plants("Alice", 1)
    print("")

    print(gm.garden_report("Alice"))
    print("")

    gm.validate_height()
    gm.print_garden_scores()
    print(f"Total gardens managed: {gm.garden_count}")
