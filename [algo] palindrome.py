import random


def solve(string):
	#set dictionary for all the characters of the given string
	alph = {}
	#set string variables for the palindrome
	palindrome = ""
	reflection = ""

	#count the number of each alphabets in the string
	for c in string:
		if c in alph:
			alph[c] += 1 
		else:
			alph[c] = 1

	#identify the number of alphabets that appear odd number of times
	#if more than one, return None as the string cannot form a palindrome
	odds = 0
	oddone = ""
	#get the key(the alphabet) and value(appearing frequency) of the alphabet set
	for k, v in alph.items():
		#if the frequency of alphabet is an odd number, mark the alphabet as the "oddone"
		if v % 2 != 0:
			odds += 1
			oddone = k
		#if their are more than two alphabets that appears odd number of times, end the function and return None
		if odds > 1:
			return None

	#create a loop that will consume all the even-times appearing alphabets to form a palindrome
	while len(alph)-odds > 0:
		#get a random number within the length of the alphabet set
		index = random.randint(0,len(alph)-1)
		#choose the alphabet in the randomly generated index
		c = list(alph)[index]
		#proceed to form palindrome if the alphabet is not odd-times appearing alphabet
		if c != oddone:
			#create a palindrome by adding the chosen alphabet to the end of the left part and the beginning of the right part
			palindrome = palindrome + c
			reflection = c + reflection
			#decrease the frequency of the chosen alphabet as it is used up to form the palindrome
			alph[c] -= 2
			#if the alphabet is all used up, delete the alphabet from the available set
			if alph[c] == 0:
				del alph[c]
			
	
	#if there is alphabet that appears odd number of times, put it in the middle of the result as it is its only appropriate place
	if odds == 1:
		palindrome = palindrome + oddone + reflection
	else:
		palindrome = palindrome + reflection
	
	#return the resulting palindrome
	return palindrome


s = "aabbccddeeffgghh"
p = solve(s)
print(p)
