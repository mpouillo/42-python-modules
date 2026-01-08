#!/usr/bin/env python3

data = {
    'players': {
        'alice': {
            'total_score': 2300,
            'achievements': [
                'first_kill', 'level_10', 'speed_runner', 'collector', 'mvp'
            ],
            'region': 'north'
        },
        'bob': {
            'total_score': 1800,
            'achievements': ['level_10', 'treasure_hunter', 'survivor'],
            'region': 'east'
        },
        'charlie': {
            'total_score': 2150,
            'achievements': [
                'first_kill', 'boss_slayer', 'speed_runner',
                'collector', 'explorer', 'master', 'legend'
            ],
            'region': 'central'
        },
        'diana': {
            'total_score': 2000,
            'achievements': [
                'first_kill', 'level_10', 'treasure_hunter', 'winner'
            ],
            'region': 'north'
        }
    },
    'achievements_list': [
        'first_kill', 'level_10', 'boss_slayer', 'treasure_hunter',
        'speed_runner', 'collector', 'survivor', 'winner',
        'explorer', 'master', 'legend', 'mvp'
    ]
}

if __name__ == "__main__":
    print("=== Game Analytics Dashboard ===\n")

    print("=== List Comprehension Examples ===")

    top_3_scorers = sorted(
        data['players'],
        key=lambda name: data['players'][name]['total_score'],
        reverse=True
    )[:3]

    high_scorers = [
        name for name, info in data['players'].items()
        if info['total_score'] > 2000
    ]

    scores_doubled = [
        info['total_score'] * 2 for info in data['players'].values()
    ]

    active_players = [name for name in data['players']]

    print("Top 3 scorers:", top_3_scorers)
    print("High scorers (>2000):", high_scorers)
    print("Scores doubled:", scores_doubled)
    print("Active players:", active_players)

    print("\n=== Dict Comprehension Examples ===")

    player_scores = {
        name: info['total_score'] for name, info in data['players'].items()
    }

    score_categories = {
        "high": sum(
            1 for name, info in data['players'].items()
            if int(info['total_score']) > 6000
        ),
        "medium": sum(
            1 for name, info in data['players'].items()
            if 6000 >= int(info['total_score']) >= 2000
        ),
        "low": sum(
            1 for name, info in data['players'].items()
            if int(info['total_score']) < 2000
        )
    }

    achiev_counts = {
        name: len(info['achievements'])
        for name, info in data['players'].items()
    }

    print("Player scores:", player_scores)
    print("Score categories:", score_categories)
    print("Achievement counts:", achiev_counts)

    print("\n=== Set Comprehension Examples ===")

    unique_players = set(sorted(name for name in data['players'].keys()))
    unique_achiev = set(sorted(data['achievements_list']))
    active_regions = set(
        sorted(info['region'] for info in data['players'].values())
    )

    print("Unique players:", unique_players)
    print("Unique achievements", unique_achiev)
    print("Active regions:", active_regions)

    print("\n=== Combined Analysis ===")

    total_players = sum(1 for _ in unique_players)
    total_unique_achiev = sum(1 for _ in unique_achiev)
    average_score = (
        sum(score for score in player_scores.values()) / len(active_players)
    )
    top_performer_name = max(
        player_scores, key=player_scores.get
    )
    top_performer_score = player_scores[top_performer_name]
    top_performer_achiev_count = achiev_counts[top_performer_name]

    print("Total players:", total_players)
    print("Total unique achievements:", total_unique_achiev)
    print("Average score:", average_score)
    print(f"Top performers: {top_performer_name} ({top_performer_score}), "
          f"{top_performer_achiev_count} achievements")
