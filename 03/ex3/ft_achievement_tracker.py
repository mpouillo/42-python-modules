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

    print("\n=== Achievement Analytics ===")

    # List of len(players) sets of achievements
    achievements = [p["achievements"] for p in players]

    unique_ach = set.union(*achievements)
    print("All unique achievements: "
          f"{unique_ach if len(unique_ach) > 0 else None}")
    print(f"Total unique achievements: {len(unique_ach)}")

    common = set.intersection(*achievements)
    print(f"\nCommon to all players: {common if len(common) > 0 else None}")

    shared_ach = set()
    for i in range(len(players)):
        for j in range(i + 1, len(players)):
            shared_ach.update(achievements[i] & achievements[j])

    rare = unique_ach - shared_ach
    print(f"Rare achievements (1 player): {rare if len(rare) > 0 else None}")

    print("\nAlice vs Bob common:",
          set.intersection(alice['achievements'], bob['achievements']))
    print("Alice unique:", alice['achievements'] - bob['achievements'])
    print("Bob unique:", bob['achievements'] - alice['achievements'])
