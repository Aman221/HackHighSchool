garray = ["dough", "fight", "light", "world", "anime", "super"]

import random

word = random.randint(1,6)

if word == 1:
	cat = garray[0]
	ultimate_first = cat[:1]
	print "The first letter of the word is " + ultimate_first + " . Start guessing!"
if word == 2:
	cat = garray[1]
	ultimate_first = cat[:1]
	print "The first letter of the word is " + ultimate_first + " . Start guessing!"
if word == 3:
	cat = garray[2]
	ultimate_first = cat[:1]
	print "The first letter of the word is " + ultimate_first + " . Start guessing!"
if word == 4:
	cat = garray[3]
	ultimate_first = cat[:1]
	print "The first letter of the word is " + ultimate_first + " . Start guessing!"
if word == 5:
	cat = garray[4]
	ultimate_first = cat[:1]
	print "The first letter of the word is " + ultimate_first + " . Start guessing!"
if word == 6:
	cat = garray[5]
	ultimate_first = cat[:1]
	print "The first letter of the word is " + ultimate_first + " . Start guessing!"

i = 1
while i < 11:
	user_guess = raw_input('-')
	if user_guess == '':
		print "You wasted a guess =P"
		i = i + 1
	elif user_guess == cat:
		print "Good Job! You are one with the Source."
		break
	elif len(user_guess) != 5:
		print "0, 1, 2, 3, 4, that's how we count to 5!"
		i = i + 1
	elif ultimate_first != user_guess[:1] and len(user_guess) == (5):
		print "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
		i = i
	elif ultimate_first == user_guess[:1] and len(user_guess) == (5):
		if i == 9:
			print "you have " + str((10 - i)) + " guess left."
			i = i + 1
		else:
			print "you have " + str((10 - i)) + " guesses left."
			i = i + 1
	if i == 11:
		print "You lose, better luck next time!"
		break