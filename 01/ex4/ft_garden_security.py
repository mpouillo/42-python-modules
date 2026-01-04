#!/usr/bin/env python3

class SecurePlant:
    def __init__(self,
                 name: str = "None",
                 height: int = 0,
                 age: int = 0):
        self.set_name(name)
        self.set_height(height)
        self.set_age(age)

    def set_name(self, name: str):
        self._name = name
        print(f"Plant created:  {self._name}")

    def set_height(self, height: int):
        if height < 0:
            print(f"Invalid operation attempted: height {height}cm [REJECTED]")
            print("Security: Negative height rejected")
        else:
            self._height = height
            print(f"Height updated: {self.get_height()}cm [OK]")

    def set_age(self, age: int):
        if age < 0:
            print(
                f"Invalid operation attempted: age "
                f"{age} day{'s' if age != -1 else ''} [REJECTED]"
                )
            print("Security: Negative age rejected")
        else:
            self._age = age
            print(f"Age updated:    {self.get_age()}cm [OK]")

    def get_name(self):
        return (self._name)

    def get_height(self):
        return (self._height)

    def get_age(self):
        return (self._age)

    def get_info(self):
        print(f"Current plant: {self.get_name()} "
              f"({self.get_height()}cm, {self.get_age()} days)")


def ft_garden_security():
    plant = SecurePlant("Begonia", 30, 60)
    print("")
    plant.set_height(-10)
    print("")
    plant.get_info()


if __name__ == "__main__":
    ft_garden_security()
