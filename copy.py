while True:
	user_input = raw_input('Ready: ')
	print user_input
	dictionary = {}
	with open("2.txt") as fh:
		for line in fh:
			key, val = line.split(',')
			#print key
			#print val
#			dictionary[str(key)] = val
			dictionary[str(val)] = key
	
	if user_input == key:
		break
	elif user_input == "Done":
		print val
		print key
	elif user_input == val:
		print key
	else:
		print "nil"