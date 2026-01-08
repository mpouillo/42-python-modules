#! /usr/bin/env python3

class Plant:
    def __init__(
            self,
            name: str = "None",
            height: int = 0,
            age: int = 0
            ):
        self.name = name
        self.height = height
        self.age = age
        self.total_growth = 0

    def __str__(self):
        string = f"{self.get_name()} ({type(self).__name__}):"
        string += f"{self.height}cm, "
        string += f"{self.get_age()} day{'s' if self.age != 1 else ''}"
        return string

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name: str):
        self._name = name

    @property
    def height(self):
        return self._height

    @height.setter
    def height(self, height: int):
        if height < 0:
            raise ValueError(
                f"Invalid operation attempted: height {height}cm [REJECTED]"
                )
        else:
            self._height = height

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, age: int):
        if age < 0:
            raise ValueError(
                f"Invalid operation attempted: "
                f"age {age} day{'s' if age != -1 else ''} "
                f"[REJECTED]"
                )
        else:
            self._age = age

    @property
    def total_growth(self):
        return self._total_growth

    @total_growth.setter
    def total_growth(self, growth):
        self._total_growth = growth

    def grow(self, growth):
        self.height += growth
        self.total_growth += growth

    def time_passes(self, time):
        self.age += time


class FloweringPlant(Plant):
    def __init__(
            self,
            name: str = "None",
            height: int = 0,
            age: int = 0,
            color: str = "unspecified color",
            bloom: bool = False
            ):
        super().__init__(name, height, age)
        self.color = color
        self.bloom = bloom

    def __str__(self):
        string = super().__str__()
        string += f"{self.color} flowers"
        string += f"{' (blooming)' if self.bloom is True else ''}"
        return string

    @property
    def color(self):
        return self._color

    @color.setter
    def color(self, color: str):
        self._color = color

    @property
    def bloom(self):
        return self._bloom

    @bloom.setter
    def bloom(self, status: bool):
        self._bloom = status


class PrizeFlower(FloweringPlant):
    def __init__(
            self,
            name: str = "None",
            height: int = 0,
            age: int = 0,
            color: str = "unspecified color",
            bloom: bool = False,
            prize: int = 0
            ):
        super().__init__(name, height, age, color, bloom)
        self.prize_value = prize

    def __str__(self):
        string = super().__str__()
        string += f", Prize points: {self.prize_value}"
        return string

    @property
    def prize_value(self):
        return self._prize_value

    @prize_value.setter
    def prize_value(self, prize_value):
        self._prize_value = prize_value


class GardenManager:
    def __init__(self):
        self.gardens = {}

    @property
    def garden_count(self):
        return len(self.gardens)

    def validate_owner(self, owner):
        if owner not in self.gardens:
            self.gardens[owner] = []

    def add_plant(self, owner: str, plant: Plant):
        self.validate_owner(owner)
        self.gardens[owner].append(plant)
        print(f"Added {plant.name} to {owner}'s garden")

    def del_plant(self, owner: str, plant: Plant):
        self.validate_owner(owner)
        self.gardens[owner].remove(plant)
        print(f"Removed {plant.name} from {owner}'s garden")

    def grow_plants(self, owner: str, growth: int = 1):
        if owner in self.gardens:
            print(f"{owner} is helping all plants grow...")
            for plant in self.gardens[owner]:
                plant.grow(growth)
                print(f"{plant.name} grew {growth}cm")

    def age_plants(self, owner: str, time: int):
        for plant in self.gardens[owner]:
            plant.time_passes(time)

    @classmethod
    def create_garden_network(cls):
        network = cls()
        return network

    def garden_report(self, owner):
        if owner in self.gardens:
            owned_plants = self.gardens.get(owner, [])
            regular, flowering, prize = 0, 0, 0
            growth = self.GardenStats.calculate_total_growth(owned_plants)
            string = f"=== {owner}'s Garden Report ===\n"
            string += "Plants in garden:\n"
            for plant in self.gardens[owner]:
                string += f"- {plant.name}: {plant.height}cm"
                if isinstance(plant, PrizeFlower):
                    string += f", Prize points: {plant.prize_value}"
                    prize += 1
                elif isinstance(plant, FloweringPlant):
                    string += f", {plant.color}"
                    string += f"{' (blooming)' if plant.bloom is True else ''}"
                    flowering += 1
                else:
                    regular += 1
                string += "\n"
            string += f"\nPlants added: {len(owned_plants)}"
            string += f", Total growth: {growth}cm"
            string += "\nPlant types: "
            string += f"{regular} regular, "
            string += f"{flowering} flowering, "
            string += f"{prize} prize flowers"
            print(f"{string}")

    class GardenStats:
        @staticmethod
        def calculate_score(plants):
            score = 0
            for p in plants:
                score += p.height
                score += p.total_growth
                if isinstance(p, PrizeFlower):
                    score += p.prize_value
            return score

        def calculate_total_growth(plants):
            total_growth = 0
            for p in plants:
                total_growth += p.total_growth
            return total_growth

    def get_garden_score(self, owner):
        plants = self.gardens.get(owner, [])
        return self.GardenStats.calculate_score(plants)

    def print_garden_scores(self):
        print("Garden scores - ", end="")
        string = ""
        for garden in self.gardens:
            string += f"{'' if string == '' else ', '}"
            string += f"{garden}: {self.get_garden_score(garden)}"
        print(string)

    def validate_height(self):
        status = True
        for garden in self.gardens:
            for plant in self.gardens.get(garden, []):
                if plant.height > 400:
                    status = False
                    break
        print(f"Height validation test: {status}")


def ft_garden_analytics():
    print("=== Garden Management System Demo ===\n")

    gm = GardenManager.create_garden_network()
    gm.add_plant("Alice", Plant("Pine Tree", 358, 1500))
    gm.add_plant("Alice", FloweringPlant("Wisteria", 87, 10, "purple", True))
    gm.add_plant("Alice", PrizeFlower("Begonia", 33, 30, "pink", False, 10))
    print("")

    gm.grow_plants("Alice", 1)
    print("")

    gm.garden_report("Alice")
    print("")

    gm.validate_height()
    print("")

    gm.grow_plants("Alice", 50)
    print("")

    gm.garden_report("Alice")
    print("")

    gm.validate_height()
    print("")

    gm.add_plant("Bob", FloweringPlant("Cosmos", 30, 5, "purple", False))
    gm.add_plant("Bob", PrizeFlower("Spider Lily", 40, 20, "red", True, 20))
    print("")

    gm.print_garden_scores()
    print(f"Total gardens managed: {gm.garden_count}")


if __name__ == "__main__":
    ft_garden_analytics()
