#!/usr/bin/env python3

from ex2.EliteCard import EliteCard
from pprint import pprint

if __name__ == "__main__":
    print("=== DataDeck Ability System ===")

    print("\nEliteCard capabilities:")
    print("- Card: ['play', 'get_card_info', 'is_playable']")
    print("- Combatable: ['attack', 'defend', 'get_combat_stats']")
    print("- Magical: ['cast_spell', 'channel_mana', 'get_magic_stats']")

    card = EliteCard("Arcane Warrior", 6, "Epic", 5, 6, 3, 8, 4)
    enemy1 = EliteCard("Enemy1", 3, "Common", 2, 3, 3, 5, 2)
    enemy2 = EliteCard("Enemy2", 3, "Common", 2, 3, 3, 5, 2)

    print(f"\nPlaying {card.name} (Elite Card):")

    attack_result = card.attack(enemy1)
    defense_result = card.defend(2)

    print("\nCombat phase:")
    print("Attack result:")
    pprint(attack_result, sort_dicts=False)
    print("Defense result:")
    pprint(defense_result, sort_dicts=False)

    spell_cast = card.cast_spell("Fireball", [enemy1, enemy2])
    mana_channel = card.channel_mana(3)

    print("\nMagic phase:")
    print("Spell cast:")
    pprint(spell_cast, sort_dicts=False)
    print("Mana channel:")
    pprint(mana_channel, sort_dicts=False)
