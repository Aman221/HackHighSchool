while True:
	user_input = raw_input('Ready: ')
	dictionary = {}
	with open("capitols.txt") as fh:
		for line in fh:
			key, val = line.split(',')
			dictionary[str(key)] = val
			if user_input in key or user_input in key.lower():
				print val
				break
			elif user_input in val or user_input in val.lower():
				print key
				break
			elif user_input ==  "Done":
				quit()
			else:
				print "nil"
				break