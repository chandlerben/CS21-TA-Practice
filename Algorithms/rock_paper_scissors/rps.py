#!/usr/bin/python

import sys


def rock_paper_scissors(n):
    output = []
    plays = ["rock", "paper", "scissors"]

    def find_outcomes(result=[]):
        if len(result) == n:
            output.append(result)
            return
        for play in plays:
            find_outcomes(result + [play])
    find_outcomes([])
    return output


print(rock_paper_scissors(5))
print(len(rock_paper_scissors(5)))

if __name__ == "__main__":
    if len(sys.argv) > 1:
        num_plays = int(sys.argv[1])
        print(rock_paper_scissors(num_plays))
    else:
        print('Usage: rps.py [num_plays]')
