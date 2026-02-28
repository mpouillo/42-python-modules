#!/usr/bin/env python3

import sys


def parse_args(args: list) -> dict:
    inv = {}
    try:
        for arg in args:
            item, qty = arg.split(":")
            if item.strip() == "":
                raise ValueError
            inv.update({item: int(qty)})
    except ValueError:
        sys.exit("Error while parsing arguments. Format: 'item:quantity'.")
    return inv


def ft_inventory_system() -> None:
    if len(sys.argv) == 1:
        sys.exit("No items provided. Usage: python3 "
                 f"{sys.argv[0]} <item1:quantity> <item2:quantity> ...")

    inv = parse_args(sys.argv[1:])

    print("=== Inventory System Analysis ===")

    total_qty = sum(inv.values())
    total_items = len(inv.keys())

    print("Total items in inventory:", total_qty)
    print("Unique item types:", total_items)

    print("\n=== Current Inventory ===")

    for item, qty in {k: v for (k, v) in sorted(inv.items(),
                                                key=lambda item: item[1],
                                                reverse=True)}.items():
        print(f"{item}: {qty} units ({round(qty / total_qty * 100, 1)}%)")

    print("\n=== Inventory Statistics ===")

    max_item = max(inv, key=inv.get)
    max_qty = inv.get(max_item)
    print(f"Most abundant: {max_item} "
          f"({max_qty} unit{'s' if max_qty > 1 else ''})")

    min_item = min(inv, key=inv.get)
    min_qty = inv.get(min_item)
    print(f"Least abundant: {min_item} "
          f"({min_qty} unit{'s' if min_qty > 1 else ''})")

    print("\n=== Item Categories ===")
    print("Moderate:", {k: v for (k, v) in inv.items() if v >= 5})
    print("Scarce:", {k: v for (k, v) in inv.items() if v < 5})

    print("\n=== Management Suggestions ===")
    print("Restock needed:", ", ".join([k for (k, v) in inv.items() if v < 2]))

    print("\n=== Dictionary Properies Demo ===")
    print("Dictionary keys:", ", ".join(inv.keys()))
    print("Dictionary values:", ", ".join(str(v) for v in inv.values()))
    print("Sample lookup - 'sword' in inventory:",
          True if inv.get("sword") is not None else False)


if __name__ == "__main__":
    try:
        ft_inventory_system()
    except SystemExit as e:
        print(e)
