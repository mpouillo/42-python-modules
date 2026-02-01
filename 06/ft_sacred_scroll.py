#!/usr/bin/env python3

import alchemy


if __name__ == "__main__":
    print("=== Sacred Scroll Mastery ===")

    print("\nTesting direct module access:")

    try:
        print("alchemy.elements.create_fire(): ", end="")
        print(alchemy.elements.create_fire())
    except AttributeError:
        print("AttributeError - not exposed")

    try:
        print("alchemy.elements.create_water(): ", end="")
        print(alchemy.elements.create_water())
    except AttributeError:
        print("AttributeError - not exposed")

    try:
        print("alchemy.elements.create_earth(): ", end="")
        print(alchemy.elements.create_earth())
    except AttributeError:
        print("AttributeError - not exposed")

    try:
        print("alchemy.elements.create_air(): ", end="")
        print(alchemy.elements.create_air())
    except AttributeError:
        print("AttributeError - not exposed")

    print("\nTesting package-level access (controlled by __init__.py):")

    try:
        print("alchemy.create_fire(): ", end="")
        print(alchemy.create_fire())
    except AttributeError:
        print("AttributeError - not exposed")

    try:
        print("alchemy.create_water(): ", end="")
        print(alchemy.create_water())
    except AttributeError:
        print("AttributeError - not exposed")

    try:
        print("alchemy.create_earth(): ", end="")
        print(alchemy.create_earth())
    except AttributeError:
        print("AttributeError - not exposed")

    try:
        print("alchemy.create_air(): ", end="")
        print(alchemy.create_air())
    except AttributeError:
        print("AttributeError - not exposed")

    print("\nPackage metadata:")
    print("Version:", alchemy.__version__)
    print("Author:", alchemy.__author__)
