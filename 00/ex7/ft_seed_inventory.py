def ft_seed_inventory(seed_type: str, quantity: int, unit: str):
    print(f"{seed_type.capitalize()} seeds: ", end="")
    match unit:
        case "packets":
            print(f"{quantity} packets available")
        case "grams":
            print(f"{quantity} grams total")
        case "area":
            print(f"covers {quantity} square meters")
        case _:
            print("Unknown unit type")
