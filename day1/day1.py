import os
from pathlib import Path
from functools import reduce


def freq_repeater(freqlist):
    cur = 0
    l = len(freqlist)
    while True:
        yield freqlist[cur % l]
        cur += 1


def part_1():
    freq = 0

    with open(Path(os.path.dirname(
            os.path.realpath(__file__))) / 'day1.txt') as f:
        return reduce(lambda x, y: int(x) + int(y), f)


def part_2():
    freqs = {0}
    freq = 0
    with open(Path(os.path.dirname(
            os.path.realpath(__file__))) / 'day1.txt') as f:
        for change in freq_repeater(f.read().splitlines()):
            freq += int(change)
            if freq in freqs:
                return freq
            freqs.add(freq)


def print_solutions_for_day():
    print("Advent of Code 2018 Day 1:")
    print("Part 1 - " + str(part_1()))
    print("Part 2 - " + str(part_2()))


if __name__ == '__main__':
    print_solutions_for_day()
