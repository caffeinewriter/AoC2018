import os, string
from pathlib import Path

def collapse_polymer(compound):
    i = 0
    while i < len(compound) - 1:
        if compound[i] != compound[i + 1] and \
            compound[i].lower() == compound[i+1].lower():
                compound = compound[:i] + compound[i + 2:]
                if i > 0:
                    i -= 1
        else:
            i += 1
    return len(compound)

def part_1():
    with open(Path(os.path.dirname(
            os.path.realpath(__file__))) / 'day5.txt') as f:
        compound = f.read().strip()
        return collapse_polymer(compound)


def part_2():
    with open(Path(os.path.dirname(
            os.path.realpath(__file__))) / 'day5.txt') as f:
        compound = f.read().strip()
        smallest = len(compound)
        for c in string.ascii_lowercase:
            smallest = min(smallest,
                    collapse_polymer(compound.replace(c, '').replace(c.upper(), '')))
        return smallest


def print_solutions_for_day():
    print("Advent of Code 2018 Day 5:")
    print("Part 1 - " + str(part_1()))
    print("Part 2 - " + str(part_2()))


if __name__ == '__main__':
    print_solutions_for_day()
