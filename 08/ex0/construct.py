#!/usr/bin/env python3

import sys
import os
import site


def base_output() -> None:
    print("MATRIX STATUS: You're still plugged in")

    print("\nCurrent python:", sys.executable)
    print("Virtual environment: None detected")

    print("\nWARNING: You're still in the global environment!")
    print("The machines can see everything you install.")

    print("\nTo enter the construct, run:")
    print("python -m venv matrix_env")
    print("source matrix_env/bin/activate    # On Unix")
    print("matrix_env")
    print("Scripts")
    print("activate    # On windows")

    print("\nThen run this program again.")


def venv_output() -> None:
    print("MATRIX STATUS: Welcome to the construct")

    print("\nCurrent python:", sys.executable)
    print("Virtual environment:", os.path.basename(sys.prefix))
    print("Environment Path:", sys.prefix)

    print("\nSUCCESS: You're in an isolated environment!")
    print("Safe to install package without affecting the global system")

    print("Package installation path:")
    print(site.getsitepackages()[0])


if __name__ == "__main__":
    if sys.prefix == sys.base_prefix:
        base_output()
    else:
        venv_output()
