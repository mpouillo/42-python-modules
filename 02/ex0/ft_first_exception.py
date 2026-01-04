#!/usr/bin/env python3

def check_temperature(temp_str):
    min, max = 0, 40
    print(f"Testing temperature: {temp_str}")
    try:
        temp_int = int(temp_str)
    except ValueError:
        print(f"Error: '{temp_str}' is not a valid number")
        return

    if temp_int < min:
        print(f"Error: {temp_int}°C is too cold for plants (min {min}°C)")
    elif temp_int > max:
        print(f"Error: {temp_int}°C is too hot for plants (max {max}°C)")
    else:
        print(f"Temperature {temp_int}°C is perfect for plants!")
        return temp_int


def test_temperature_input():
    values = [25, "abc", 100, -50]
    for val in values:
        check_temperature(val)


if __name__ == "__main__":
    test_temperature_input()
