#!/usr/bin/python

import sys


def rock_paper_scissors(n):
    outcome = []
    plays = ['rock', 'paper', 'scissors']

    def create_outcomes(rounds_left, result=[]):
        if rounds_left == 0:
            outcome.append(result)
            return
        for play in plays:
            create_outcomes(rounds_left-1, result + [play])
    create_outcomes(n, [])
    return outcome


print(rock_paper_scissors(2))
print(len(rock_paper_scissors(20)))


if __name__ == "__main__":
    if len(sys.argv) > 1:
        num_plays = int(sys.argv[1])
        print(rock_paper_scissors(num_plays))
    else:
        print('Usage: rps.py [num_plays]')
