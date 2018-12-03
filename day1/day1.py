from functools import reduce

def freq_repeater(freqlist):
	cur = 0
	l = len(freqlist)
	while True:
		yield freqlist[cur % l]
		cur += 1

def part1():
	freq = 0

	with open('day1.txt', 'r') as f:
		return reduce(lambda x, y: int(x) + int(y), f)


def part2():
	freqs = {0}
	freq = 0
	with open('day1.txt', 'r') as f:
		for change in freq_repeater(f.read().splitlines()):
			freq += int(change)
			if freq in freqs:
				return freq
			freqs.add(freq)

if __name__ == '__main__':
	print("Advent of Code Day 1:")
	print("Part 1 - " + str(part1()))
	print("Part 2 - " + str(part2()))