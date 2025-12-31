#! /usr/bin/env python3

class GardenManager:
    def create_garden_network(self):
        self._garden_list = []

    def add_garden(self, garden: Garden):
        self._garden_list.append(garden)

    def delete_garden(self, garden: Garden):
        self._garden_list.remove(garden)

    def get_garden_network(self):
        return self._garden_list


class GardenStats(GardenManager):
    def

class Garden:
    def __init__(self, owner: str):
        self.set_owner(owner)

    def owner(owner)


def ft_garden_analytics():



if __name__ = "__main__":
    ft_garden_analytics()
