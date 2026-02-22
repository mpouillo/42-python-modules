#!/usr/bin/env python3
"""Python Module 01 Exercise 4."""


class SecurePlant:
    """Create a secure plant object."""

    def __init__(self,
                 name: str = "None",
                 height: int = 0,
                 age: int = 0):
        """
        Initialize plant object with name, height and age.

        Keyword arguments:
        name    -- name of the plant object
        height  -- height of the plant object, in cm
        age     -- age of the plant object, in days
        """
        self.set_name(name)
        self.set_height(height)
        self.set_age(age)

    def set_name(self, name: str) -> None:
        """Set plant name."""
        self.__name = name

    def set_height(self, height: int) -> None:
        """Securely set plant height."""
        if height < 0:
            print("Security: Negative height rejected")
        else:
            self.__height = height

    def set_age(self, age: int) -> None:
        """Securely set plant age."""
        if age < 0:
            print("Security: Negative age rejected")
        else:
            self.__age = age

    def get_name(self) -> str:
        """Return plant name."""
        return self.__name

    def get_height(self) -> int:
        """Return plant height."""
        return self.__height

    def get_age(self) -> int:
        """Return plant age."""
        return self.__age

    def get_info(self) -> str:
        """Return information (name, height, days) about the plant."""
        return (f"{self.get_name()} ({self.get_height()}cm, "
                f"{self.get_age()} day{'s' if self.get_age() > 1 else ''})")


if __name__ == "__main__":
    plant = SecurePlant("Rose", 1, 1)
    print(f"Plant created: {plant.get_name()}")
    plant.set_height(25)
    print(f"Height updated: {plant.get_height()}cm [OK]")
    plant.set_age(30)
    print(f"Age updated:    {plant.get_age()}cm [OK]")

    print("\nInvalid operation attempted: height -5cm [REJECTED]")
    plant.set_height(-5)

    print(f"\nCurrent plant: {plant.get_info()}")
