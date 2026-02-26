#!/usr/bin/env python3

import sys


def ft_score_analytics() -> None:
    print("=== Player Score Analytics ===")

    # Return if no arguments passed
    if len(sys.argv) == 1:
        print(f"No scores provided. "
              f"Usage: python3 {sys.argv[0]} <score1> <score2> ...")
        return

    # Remove program name from args
    args = sys.argv[1:]

    # Convert scores to int
    try:
        scores = [int(arg) for arg in args]
    except ValueError as e:
        print("Error processing scores:", e)
        return

    # Process scores
    nb_scores = len(scores)
    sum_scores = sum(int(x) for x in scores)
    avg_score = "{:.1f}".format(sum_scores / nb_scores)
    high_score = max(int(x) for x in scores)
    low_score = min(int(x) for x in scores)
    score_range = high_score - low_score

    print("Scores processed:", scores)
    print("Total players:", nb_scores)
    print("Total score:", sum_scores)
    print("Average score: ", avg_score)
    print("High score:", high_score)
    print("Low score:", low_score)
    print("Score range:", score_range)


if __name__ == "__main__":
    ft_score_analytics()
