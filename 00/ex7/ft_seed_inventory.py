def ft_seed_inventory(seed_type: str, quantity: int, unit: str) -> None:
    print(f"{seed_type.capitalize()} seeds: ", end="")
    if unit == "packets":
        print(f"{quantity} packets available")
    elif unit == "grams":
        print(f"{quantity} grams total")
    elif unit == "area":
        print(f"covers {quantity} square meters")
    else:
        print("Unknown unit type")
