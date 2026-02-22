def ft_seed_inventory(seed_type: str, quantity: int, unit: str) -> None:
    print(f"{seed_type.capitalize()} seeds: ", end="")
    if unit == "packets":
        print(f"{quantity} packet{'s' if quantity > 1 else ''} available")
    elif unit == "grams":
        print(f"{quantity} gram{'s' if quantity > 1 else ''} total")
    elif unit == "area":
        print(f"covers {quantity} square meter{'s' if quantity > 1 else ''}")
    else:
        print("Unknown unit type")
