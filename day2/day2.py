import os
from pathlib import Path
from collections import Counter


def comp_strings(a, b):
    a = a.strip()
    b = b.strip()
    la = len(a)
    diff = -1
    if la != len(b):
        raise ValueError('Strings not of equal length')
    for i in range(la):
        if a[i] != b[i] and diff == -1:
            diff = i
        elif a[i] != b[i]:
            return -1
    return diff


def part_1():
    ex_two = 0
    ex_three = 0
    with open(Path(os.path.dirname(
            os.path.realpath(__file__))) / 'day2.txt') as f:
        for idn in f:
            has_two = False
            has_three = False
            letterset = set(idn)
            counter = Counter(idn)
            for l in letterset:
                if counter[l] == 2:
                    has_two = True
                if counter[l] == 3:
                    has_three = True
                if has_two and has_three:
                    break
            ex_two += int(has_two)
            ex_three += int(has_three)
    return ex_two * ex_three


def part_2():
    with open(Path(os.path.dirname(
            os.path.realpath(__file__))) / 'day2.txt') as f:
        ordered = sorted(f.read().splitlines())
        commons = [[x, y] for x, y in zip(
            ordered[:-1], ordered[1:]) if comp_strings(x, y) > -1][0]
        diff_char = comp_strings(commons[0], commons[1])
        return commons[0][:diff_char] + commons[0][diff_char+1:]


def print_solutions_for_day():
    print("Advent of Code 2018 Day 2:")
    print("Part 1 - " + str(part_1()))
    print("Part 2 - " + str(part_2()))


if __name__ == '__main__':
    print_solutions_for_day()
