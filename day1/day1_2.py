freqs = {'0': 1}
freq = 0

def freq_repeater(freqlist):
	cur = 0
	l = len(freqlist)
	while True:
		yield freqlist[cur % l]
		cur += 1

with open('day1_1.txt', 'r') as f:
	for change in freq_repeater(f.read().splitlines()):
		if change[0] == '+':
			mul = 1
		else:
			mul = -1
		freq += int(change[1:]) * mul
		strfreq = str(freq)
		if strfreq in freqs:
			print(freq)
			exit()
		freqs[strfreq] = 1