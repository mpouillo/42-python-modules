#!/usr/bin/env python3

def test_error_types():
    print("Testing ValueError...")
    try:
        int("abc")
    except ValueError as e:
        print(f"Caught ValueError: {e}\n")

    print("Testing ZeroDivisionError...")
    try:
        1 / 0
    except ZeroDivisionError as e:
        print(f"Caught ZeroDivisionError: {e}\n")

    print("Testing FileNotFoundError...")
    try:
        with open("missing.txt", "r") as f:
            f.read()
    except FileNotFoundError as e:
        print(f"Caught FileNotFoundError: {e}\n")

    print("Testing KeyError...")
    try:
        d = {}
        _ = d["missing key"]
    except KeyError as e:
        print(f"Caught KeyError: {e}\n")

    print("Testing multiple errors together...")
    try:
        int("bad data")
    except (ValueError, ZeroDivisionError):
        print("Caught an error, but program continues!\n")


def garden_operations():
    print("=== Garden Error Types Demo ===\n")
    test_error_types()
    print("All error types tested successfully!")


if __name__ == "__main__":
    garden_operations()
