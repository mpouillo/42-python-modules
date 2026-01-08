#!/usr/bin/env python3

if __name__ == "__main__":
    print("=== Player Inventory System ===\n")

    inv = {
        "Alice": {
            "sword": {
                "type": "weapon",
                "rarity": "rare",
                "quantity": 1,
                "price": 500
            },
            "potion": {
                "type": "consumable",
                "rarity": "common",
                "quantity": 5,
                "price": 50
            },
            "shield": {
                "type": "armor",
                "rarity": "uncommon",
                "quantity": 1,
                "price": 200
            }
        }
    }

    for player, item in inv.items():
        print(f"=== {player}'s Inventory ===")
        for name, details in item.items():
            type = details.get("type")
            rarity = details.get("rarity")
            quantity = details.get("quantity", 1)
            price = details.get("price", 0)
            print(
                f"{name} ({type}, {rarity}): "
                f"{quantity}x @ {price} gold each = {quantity * price} gold"
            )

    total_value, item_count = 0, 0
    for details in inv["Alice"].values():
        item_count += details.get('quantity')
        total_value += details.get('quantity') * details.get('price')

    print(f"\nInventory value: {total_value}")
    print(f"Item count: {item_count} items")

    categories = ", ".join(
        f'{item}({inv["Alice"][item].get("quantity")})'
        for item in inv["Alice"]
    )
    print(f"Categories: {categories}\n")

    inv.update({"Bob": {}})
    traded_item = "potion"

    print(f"=== Transaction: Alice gives Bob 2 {traded_item}s ===")

    if traded_item in inv["Alice"]:
        inv["Alice"][traded_item]["quantity"] -= 2
        if traded_item in inv["Bob"]:
            inv["Bob"][traded_item]["quantity"] += 2
        else:
            inv["Bob"].update({traded_item: inv["Alice"][traded_item].copy()})
        inv["Bob"][traded_item]["quantity"] = 2
        print("Transaction successful!")

    print("\n=== Updated Inventories ===")

    for player, items in inv.items():
        print(f"{player} {traded_item}s: {items[traded_item].get('quantity')}")

    print("\n=== Inventory Analytics ===")

    RARITIES = {
        "common": 1,
        "uncommon": 2,
        "rare": 3
    }

    player_data = {
        "values": {
            player: sum(details['price'] * details['quantity']
                        for details in items.values())
            for player, items in inv.items()
        },
        "items": {
            player: sum(d['quantity'] for d in items.values())
            for player, items in inv.items()
        },
        "rarest": {
            player: max(
                items,
                key=lambda item: RARITIES.get(inv[player][item]['rarity'], 0),
                default="Nothing"
            )
            for player, items in inv.items()
        }
    }

    print(
        "Most valuable player:",
        max(player_data['values'],
            key=player_data['values'].get)
    )
    print(
        "Most items:",
        max(player_data['items'],
            key=player_data['items'].get)
    )
    print(
        "Rarest items:",
        ', '.join(item for player, item in player_data.get('rarest').items())
    )
