#!/usr/bin/env python3

def check_temperature(temp_str: int) -> int | None:
    min, max = 0, 40
    print(f"Testing temperature: {temp_str}")
    try:
        temp_int = int(temp_str)
        if temp_int < min:
            print(f"Error: {temp_int}°C is too cold for plants (min {min}°C)")
            return None
        elif temp_int > max:
            print(f"Error: {temp_int}°C is too hot for plants (max {max}°C)")
            return None
        else:
            return temp_int
    except ValueError:
        print(f"Error: '{temp_str}' is not a valid number")
        return None


def test_temperature_input() -> None:
    for value in [25, "abc", 100, -50]:
        temp = check_temperature(value)
        if temp:
            print(f"Temperature {temp}°C is perfect for plants!")
        print()


if __name__ == "__main__":
    print("=== Garden Temperature Checker ===\n")
    test_temperature_input()
    print("All tests completed - program didn't crash!")
