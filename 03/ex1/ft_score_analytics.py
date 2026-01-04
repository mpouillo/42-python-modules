#!/usr/bin/env python3

import sys


def ft_score_analytics():
    print("=== Player Score Analytics ===")
    if len(sys.argv) == 1:
        print(f"No scores provided. "
              f"Usage: python3 {sys.argv[0]} <score1> <score2> ....")
    else:
        args = sys.argv[1:]
        try:
            for arg in args:
                int(arg)
        except ValueError as e:
            print(f"Error processing scores: {e}")
            return
        print(f"Scores processed: {args}")
        len_args = len(args)
        print(f"Total players: {len_args}")
        sum_args = sum(int(x) for x in args)
        print(f"Total score: {sum_args}")
        print("Average score: " + "{:.1f}".format(sum_args / len_args))
        high = max(int(x) for x in args)
        print(f"High score: {high}")
        low = min(int(x) for x in args)
        print(f"Low score: {low}")
        print(f"Score range: {high - low}")


if __name__ == "__main__":
    ft_score_analytics()
