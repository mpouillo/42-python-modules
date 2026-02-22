#!/usr/bin/env python3

class GardenError(Exception):
    pass


class SunlightError(GardenError):
    def __init__(self, name: str = "Plant", message: str | None = None):
        if message is None:
            message = f"Sunlight too high or low, {name} is wilting!"
        super().__init__(message)


class WaterHighError(GardenError):
    def __init__(self, message: str | None = None):
        if message is None:
            message = "Too much water in tank"
        super().__init__(message)


class WaterLowError(GardenError):
    def __init__(self, message: str | None = None):
        if message is None:
            message = "Not enough water in tank"
        super().__init__(message)


class EmptyPlantName(GardenError):
    def __init__(self, message: str | None = None):
        if message is None:
            message = "Plant name cannot be empty!"
        super().__init__(message)


class GardenManager:
    def __init__(self) -> None:
        self.plant_list = []

    @property
    def plant_list(self) -> list['Plant']:
        return self._plant_list

    @plant_list.setter
    def plant_list(self, plant_list: list['Plant']) -> None:
        if type(plant_list) is not list:
            raise ValueError
        else:
            self._plant_list = plant_list

    class Plant:
        def __init__(self,
                     name: str,
                     water: int = 10,
                     sunlight: int = 10):
            self.name = name
            self.sunlight = sunlight
            self.water = water

        @property
        def name(self) -> str:
            return self._name

        @name.setter
        def name(self, name: str) -> None:
            if name in [None, ""]:
                raise EmptyPlantName
            else:
                self._name = name

        @property
        def sunlight(self) -> int:
            return self._sunlight

        @sunlight.setter
        def sunlight(self, value: int) -> None:
            self._sunlight = max(0, value)
            if self.sunlight > 10:
                raise SunlightError(self.name)
            if self.sunlight < 1:
                raise SunlightError(self.name)

        @property
        def water(self) -> int:
            return self._water

        @water.setter
        def water(self, value: int) -> None:
            self._water = max(0, value)
            if self.water < 1:
                raise WaterLowError
            if self.water > 10:
                raise WaterHighError

    def add_plant(self,
                  name: str,
                  sunlight: int = 10,
                  water: int = 10) -> None:
        try:
            plant = GardenManager.Plant(name, sunlight, water)
            self.plant_list.append(plant)
            print(f"Added {plant.name} successfully")
        except GardenError as e:
            print(f"Error adding plant: {e}")

    def water_plants(self, value: int = 1) -> None:
        print("Opening watering system")
        try:
            for plant in self.plant_list:
                plant.water += value
                print(f"Watering {plant.name} - Success")
        except ValueError as e:
            print(f"Error: {e}")
        except GardenError as e:
            print(f"Watering {plant.name} - {e}")
        finally:
            print("Closing watering system (cleanup)")

    def check_health(self) -> None:
        for plant in self.plant_list:
            try:
                if plant.water > 10:
                    raise WaterHighError(
                        f"Error checking {plant.name}: "
                        f"Water level {plant.water} is too high (max 10)"
                        )
                elif plant.water < 1:
                    raise WaterLowError(
                        f"Error checking {plant.name}: "
                        f"Water level {plant.water} is too low (min 1)"
                        )
                elif plant.sunlight < 1:
                    raise SunlightError(
                        f"Error checking {plant.name}: "
                        f"Sun level {plant.sunlight} is too low (min 1)"
                        )
                print(
                    f"{plant.name}: healthy "
                    f"(water: {plant.water}, sun: {plant.sunlight})"
                    )
            except GardenError as e:
                print(e)


if __name__ == "__main__":
    print("=== Garden Management System ===")

    gm = GardenManager()

    print("\nAdding plants to garden...")
    gm.add_plant("tomato", 4, 8)
    gm.add_plant("lettuce", 10, 10)
    gm.add_plant("")

    print("\nWatering plants...")
    gm.water_plants()

    print("\nChecking plant health...")
    gm.check_health()

    print("\nTesting error recovery...")
    try:
        raise WaterLowError
    except GardenError as e:
        print(f"Caught GardenError: {e}")
        print("System recovered and continuing...")

    print("\nGarden mangement system test complete!")
