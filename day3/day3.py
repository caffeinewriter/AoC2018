from functools import partial
from itertools import chain


class Field:
    def __init__(self):
        self.space = [[0 for x in range(1000)] for y in range(1000)]

    def claim(self, x, y, width, height):
        for wy in range(height):
            for wx in range(width):
                self.space[y + wy][x + wx] += 1

    def overlaps(self):
        flat_space = list(chain.from_iterable(self.space))
        return len(list(filter(lambda x: x > 1, flat_space)))


def handle_claim(field, claim):
    claim = claim.split(' ')
    num = claim[0][1:]
    startpoint = claim[2][:-1].split(',')
    sizestr = claim[3].split('x')
    field.claim(int(startpoint[0]), int(
        startpoint[1]), int(sizestr[0]), int(sizestr[1]))


def split_claim(claim):
    claim = claim.split(' ')
    num = claim[0][1:]
    startpoint = claim[2][:-1].split(',')
    sizestr = claim[3].split('x')
    return [int(num), int(startpoint[0]), int(startpoint[1]), int(sizestr[0]), int(sizestr[1])]


def determine_overlaps(claim1, claim2):
    if (claim1[1] < claim2[1] + claim2[3] and
        claim1[1] + claim1[3] > claim2[1] and
        claim1[2] < claim2[2] + claim2[4] and
        claim1[2] + claim1[4] > claim2[2]):
        return True
    return False

    # xs1 = set(range(claim1[1], claim1[1] + claim1[3]))
    # xs2 = set(range(claim2[1], claim2[1] + claim2[3]))
    # ys1 = set(range(claim1[2], claim1[2] + claim1[4]))
    # ys2 = set(range(claim2[2], claim2[2] + claim2[4]))
    # if xs1 & xs2 and ys1 & ys2:
    #     return True
    # return False


def part1():
    field = Field()
    with open('day3.txt') as f:
        for claim in f:
            handle_claim(field, claim)
    return field.overlaps()


def part2():
    with open('day3.txt') as f:
        claims = list(map(lambda x: split_claim(x), f.read().splitlines()))
        for i in range(len(claims) - 1):
            elem = claims[i]
            overlaps = False
            for j in range(len(claims)):
                if i == j:
                    continue
                overlaps = determine_overlaps(claims[i], claims[j])
                if overlaps:
                    break
            if not overlaps:
                return claims[i][0]


def part2_alt():
    with open('day3.txt') as f:
        invalid = []
        claims = list(map(lambda x: split_claim(x), f.read().splitlines()))
        for i in range(len(claims) - 1):
            elem = claims[i]
            overlaps = False
            for j in range(len(claims)):
                if i == j:
                    continue
                if determine_overlaps(claims[i], claims[j]):
                    overlaps = True
                if overlaps:
                    invalid + [i, j]
            if not overlaps:
                return claims[i][0]


print("Advent of Code 2018 Day 3:")
print("Part 1 - " + str(part1()))
print("Part 2 - " + str(part2()))
