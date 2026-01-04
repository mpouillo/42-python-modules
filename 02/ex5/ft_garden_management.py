#!/usr/bin/env python3

class GardenError(Exception):
    pass


class SunlightError(GardenError):
    def __init__(self, name: str, message: str = None):
        if message is None:
            message = f"Insufficient sunlight, {name} is wilting!"
        super().__init__(message)


class WaterHighError(GardenError):
    def __init__(self, message: str = None):
        if message is None:
            message = "Too much water in tank"
        super().__init__(message)


class WaterLowError(GardenError):
    def __init__(self, message: str = None):
        if message is None:
            message = "Not enough water in tank"
        super().__init__(message)


class EmptyPlantName(GardenError):
    def __init__(self, message: str = None):
        if message is None:
            message = "Plant name cannot be empty!"
        super().__init__(message)


class GardenManager:
    def __init__(self):
        self.plant_list = []

    @property
    def plant_list(self):
        return self._plant_list

    @plant_list.setter
    def plant_list(self, plant_list: list):
        if type(plant_list) is not list:
            raise ValueError
        else:
            self._plant_list = plant_list

    class Plant:
        def __init__(self,
                     name: str,
                     sunlight: int = 10,
                     water: int = 10):
            self.name = name
            self.sunlight = sunlight
            self.water = water

        @property
        def name(self):
            return self._name

        @name.setter
        def name(self, name):
            if name in [None, ""]:
                raise EmptyPlantName
            else:
                self._name = name

        @property
        def sunlight(self):
            return self._sunlight

        @sunlight.setter
        def sunlight(self, value: int):
            self._sunlight = value
            if self.sunlight > 10:
                self._sunlight = 10
            if self.sunlight < 1:
                raise SunlightError(self.name)

        @property
        def water(self):
            return self._water

        @water.setter
        def water(self, value: int):
            self._water = value
            if self.water < 1:
                raise WaterLowError
            if self.water > 10:
                raise WaterHighError

    def add_plant(self, name: str, sunlight: int = 10, water: int = 10):
        try:
            plant = GardenManager.Plant(name, sunlight, water)
            self.plant_list.append(plant)
            print(f"Added {plant.name} successfully")
        except GardenError as e:
            print(f"Error adding plant: {e}")

    def water_plants(self, value: int = 1):
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

    def check_health(self):
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
    gm.add_plant("tomato", 8, 1)
    gm.add_plant("lettuce", 10, 10)
    gm.add_plant("")

    print("\nWatering plants...")
    gm.water_plants(5)

    print("\nChecking plant health...")
    gm.check_health()

    print("\nTesting error recovery...")
    try:
        raise WaterLowError
    except GardenError as e:
        print(f"Caught GardenError: {e}")
        print("System recovered and continuing...")

    print("\nGarden mangement system test complete!")
