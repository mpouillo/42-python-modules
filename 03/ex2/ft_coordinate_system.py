#!/usr/bin/env python3

import math
import sys


def calculate_distance(tup1: tuple[int, int, int],
                       tup2: tuple[int, int, int]) -> None:
    try:
        x1, y1, z1 = tup1
        x2, y2, z2 = tup2
        distance = math.sqrt(
            (int(x2)-int(x1))**2
            + (int(y2)-int(y1))**2
            + (int(z2)-int(z1))**2
            )
        print(
            f"Distance between {(x1, y1, z1)} and {(x2, y2, z2)}: "
            f"{round(distance, 2)}"
            )
    except (ValueError, TypeError):
        pass


def str_to_coords(string: str) -> tuple[int, int, int]:
    try:
        coords = tuple([int(num) for num in string.split(',', 2)])
        print(f"Parsed position: {coords}")
        return coords
    except ValueError as e:
        print(f"Error parsing coordinates: {e}")
        print(f"Error details - Type: {type(e).__name__}, Args: (\"{e}\")")


def ft_coordinate_system():
    print("=== Game Coordinate System ===\n")

    if len(sys.argv) > 1:
        try:
            pos = tuple([int(sys.argv[1]),
                         int(sys.argv[2]),
                         int(sys.argv[3])])
        except (ValueError, IndexError):
            print("Invalid coordinates. Make sure to input 3 valid integers.\n"
                  f"Usage: python3 {sys.argv[0]} x y z")
            return
    else:
        pos = (10, 20, 5)

    print(f"Position created: {pos}")

    origin = (0, 0, 0)
    calculate_distance(origin, pos)
    print()

    valid_pos = "3,4,0"
    print(f"Parsing coordinates: \"{valid_pos}\"")
    calculate_distance(origin, str_to_coords(valid_pos))
    print()

    invalid_pos = "abc,def,ghi"
    print(f"Parsing invalid coordinates: \"{invalid_pos}\"")
    calculate_distance(origin, str_to_coords(invalid_pos))
    print()

    print("Unpacking demonstration:")
    pos = (3, 4, 0)
    print("Player at x={0}, y={1}, z={2}".format(*pos))
    print("Coordinates: X={0}, Y={1}, Z={2}".format(*pos))


if __name__ == "__main__":
    ft_coordinate_system()
