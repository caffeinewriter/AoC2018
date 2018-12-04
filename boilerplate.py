import os
from pathlib import Path


def part_1():
    with open(Path(os.path.dirname(
            os.path.realpath(__file__))) / 'dayX.txt') as f:
        pass


def part_2():
    with open(Path(os.path.dirname(
            os.path.realpath(__file__))) / 'dayX.txt') as f:
        pass


def print_solutions_for_day():
    print("Advent of Code 2018 Day X:")
    print("Part 1 - " + str(part_1()))
    print("Part 2 - " + str(part_2()))


if __name__ == '__main__':
    print_solutions_for_day()
