#!/usr/bin/env python3

from typing import Any


def water_plants(plant_list: list[Any]) -> None:
    print("Opening watering system")
    success = 0
    try:
        for plant in plant_list:
            if type(plant) is str:
                print(f"Watering {plant}")
            else:
                raise ValueError
        success = 1
    except ValueError:
        print(f"Error: Cannot water {plant} - invalid plant!")
    finally:
        print("Closing watering system (cleanup)")
    if success == 1:
        print("Watering completed successfully!")


def test_watering_system() -> None:
    print("=== Garden Watering System ===\n")

    print("Testing normal watering...")
    water_plants(["tomato", "lettuce", "carrots"])

    print("\nTesting with error...")
    water_plants(["tomato", None, "carrots"])

    print("\nCleanup always happens, even with errors!")


if __name__ == "__main__":
    test_watering_system()
