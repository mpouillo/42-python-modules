#!/usr/bin/env python3

if __name__ == "__main__":
    print("=== Achievement Tracker System ===\n")
    alice = {
        "name": "alice",
        "achievements": {
            'first_kill',
            'ĺevel_10',
            'treasure_hunter',
            'speed_demon'
            }
        }
    bob = {
        "name": "bob",
        "achievements": {
            'first_kill',
            'ĺevel_10',
            'boss_slayer',
            'collector'
            }
        }
    charlie = {
        "name": "charlie",
        "achievements": {
            'ĺevel_10',
            'treasure_hunter',
            'boss_slayer',
            'speed_demon',
            'perfectionist'
            }
        }

    players = [alice, bob, charlie]

    for player in players:
        print(
            f"Player {player.get('name')} achievements: "
            f"{player.get('achievements')}"
            )

    print("=== Achievement Analytics ===\n")

    achievements = [p["achievements"] for p in players]

    all = set.union(*achievements)
    print(f"All unique achievements: {all if len(all) > 0 else None}")
    print(f"Total unique achievements: {len(all)}")
    print()

    common = set.intersection(*achievements)
    print(f"Common to all players: {common if len(common) > 0 else None}")

    shared = set()
    for i in range(len(players)):
        for j in range(i + 1, len(players)):
            shared.update(achievements[i] & achievements[j])

    rare = all - shared
    print(f"Rare achievements (1 player): {rare if len(rare) > 0 else None}")
    print()

    print("Alice vs Bob common: "
          f"{set.intersection(alice['achievements'], bob['achievements'])}")
    print("Alice unique: "
          f"{alice['achievements'] - bob['achievements']}")
    print("Bob unique: "
          f"{bob['achievements'] - alice['achievements']}")
