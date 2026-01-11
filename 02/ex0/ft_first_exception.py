#!/usr/bin/env python3

from typing import Any


def check_temperature(temp: Any) -> Any:
    min, max = 0, 40
    print(f"Testing temperature: {temp}")
    try:
        temp_int = int(temp)
        if temp_int < min:
            print(f"Error: {temp_int}°C is too cold for plants (min {min}°C)")
        elif temp_int > max:
            print(f"Error: {temp_int}°C is too hot for plants (max {max}°C)")
        else:
            print(f"Temperature {temp_int}°C is perfect for plants!")
        return temp_int
    except ValueError:
        print(f"Error: '{temp}' is not a valid number")


def test_temperature_input() -> None:
    values = [25, "abc", 100, -50]
    for val in values:
        check_temperature(val)


if __name__ == "__main__":
    test_temperature_input()
