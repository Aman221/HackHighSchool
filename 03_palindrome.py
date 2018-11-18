print "Welcome to Palindrome Palace!"
print "By royal decree, her highness Queen Hannah has declared that only palindromes may be allowed within the sacred walls of Palindrome Palace!"
print "I am the royal guard, Noon!"
print "What is thy name? For that will decide whether or not thou may enter these sacred walls!"
palindrometest = raw_input('-')
if palindrometest == palindrometest[::-1]:
	print "Welcome to Palindrome Palace, palindrome! Thou art welcome now and forevermore!"
else:
	print "Apologies, non-palindrome! Thou art not welcome in these walls! No exceptions! Perhaps thou should try the Realm of Rhymes next door."