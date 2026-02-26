#!/usr/bin/env python3

import sys

if __name__ == "__main__":
    print("=== Command Quest ===")

    if len(sys.argv) == 1:
        print("No arguments provided!")

    print("Program name:", sys.argv[0])

    for i, arg in enumerate(sys.argv[1:], 1):
        print(f"Argument {i}: {arg}")

    print(f"Total arguments: {len(sys.argv[1:]) + 1}")
