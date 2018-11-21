garray = ["dough", "fight", "light", "world", "anime", "super"]

import random

word = random.randint(1,6)

if word == 1:
	cat = garray[0]
	print "The first letter of the word is 'd'. Start guessing!"
if word == 2:
	cat = garray[1]
	print "The first letter of the word is 'f'. Start guessing!"
if word == 3:
	cat = garray[2]
	print "The first letter of the word is 'l'. Start guessing!"
if word == 4:
	cat = garray[3]
	print "The first letter of the word is 'w'. Start guessing!"
if word == 5:
	cat = garray[4]
	print "The first letter of the word is 'a'. Start guessing!"
if word == 6:
	cat = garray[5]
	print "The first letter of the word is 's'. Start guessing!"


i = 1
while i < 11:
	
	i = i + 1
	if i == 11:
		break


print "You lose, better luck next time!"