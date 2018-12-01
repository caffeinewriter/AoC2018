freq = 0

with open('day1_1.txt', 'r') as f:
	for change in f:
		if change[0] == '+':
			mul = 1
		else:
			mul = -1
		freq += int(change[1:]) * mul

print(freq)