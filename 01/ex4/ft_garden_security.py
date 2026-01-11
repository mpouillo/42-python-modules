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
        height  -- height of the plant object
        age     -- age of the plant object
        """
        self.set_name(name)
        self.set_height(height)
        self.set_age(age)

    def set_name(self, name: str) -> None:
        """Set plant name."""
        self._name = name
        print(f"Plant created: {self.get_name()}")

    def set_height(self, height: int) -> None:
        """Securely set plant height."""
        if height < 0:
            print(f"Invalid operation attempted: height {height}cm [REJECTED]")
            print("Security: Negative height rejected")
        else:
            self._height = height
            print(f"Height updated: {self.get_height()}cm [OK]")

    def set_age(self, age: int) -> None:
        """Securely set plant age."""
        if age < 0:
            print(
                f"Invalid operation attempted: age "
                f"{age} day{'s' if age != -1 else ''} [REJECTED]"
                )
            print("Security: Negative age rejected")
        else:
            self._age = age
            print(f"Age updated:    {self.get_age()}cm [OK]")

    def get_name(self) -> str:
        """Return plant name."""
        return (self._name)

    def get_height(self) -> int:
        """Return plant height."""
        return (self._height)

    def get_age(self) -> int:
        """Return plant age."""
        return (self._age)

    def get_info(self) -> str:
        """Return information (name, height, lifetime) about the plant."""
        return (f"Current plant: {self.get_name()} "
                f"({self.get_height()}cm, {self.get_age()} days)")


if __name__ == "__main__":
    plant = SecurePlant("Begonia", 30, 60)

    print()
    plant.set_height(-10)

    print(f"\n{plant.get_info()}")
