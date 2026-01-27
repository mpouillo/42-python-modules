#!/usr/bin/env python3

def check_plant_health(plant_name: str,
                       water_level: int,
                       sunlight_h: int) -> None:
    if plant_name in [None, ""]:
        raise ValueError("Plant name cannot be empty!")
    if water_level < 1:
        raise ValueError(f"Water level {water_level} is too low (min 1)")
    if water_level > 10:
        raise ValueError(f"Water level {water_level} is too high (max 10)")
    if sunlight_h < 2:
        raise ValueError(f"Sunlight hours {sunlight_h} is too low (min 2)")
    if sunlight_h > 12:
        raise ValueError(f"Sunlight hours {sunlight_h} is too high (max 12)")
    print(f"Plant \"{plant_name}\" is healthy!")


def test_plant_checks() -> None:
    print("=== Garden Plant Health Checker ===")
    print()
    print("Testing good values...")
    try:
        check_plant_health("tomato", 5, 5)
    except ValueError as e:
        print(f"Error: {e}")
    print()
    print("Testing empty plant name...")
    try:
        check_plant_health("", 5, 5)
    except ValueError as e:
        print(f"Error: {e}")
    print()
    print("Testing bad water levels...")
    try:
        check_plant_health("tomato", 0, 5)
    except ValueError as e:
        print(f"Error: {e}")
    try:
        check_plant_health("tomato", 20, 5)
    except ValueError as e:
        print(f"Error: {e}")
    print()
    print("Testing bad sunlight hours...")
    try:
        check_plant_health("tomato", 5, 0)
    except ValueError as e:
        print(f"Error: {e}")
    try:
        check_plant_health("tomato", 20, 0)
    except ValueError as e:
        print(f"Error: {e}")
    print()
    print("All error raising tests completed!")


if __name__ == "__main__":
    test_plant_checks()
