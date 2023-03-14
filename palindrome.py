import random


def solve(string):
	alph = {}
	palindrome = ""
	reflection = ""

	for c in string:
		if c in alph:
			alph[c] += 1 
		else:
			alph[c] = 1

	odds = 0
	oddone = ""
	for k, v in alph.items():
		if v % 2 != 0:
			odds += 1
			oddone = k
		if odds > 1:
			return None


	while len(alph)-odds > 0:
		index = random.randint(0,len(alph)-1)
		c = list(alph)[index]
		if c != oddone:
			alph[c] -= 2
			if alph[c] == 0:
				del alph[c]
			palindrome = palindrome + c
			reflection = c + reflection

	if odds == 1:
		palindrome = palindrome + oddone + reflection
	else:
		palindrome = palindrome + reflection
	
	return palindrome


s = "aabbccddeeffgghh"
p = solve(s)
print(p)