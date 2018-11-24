while True:
	user_input = raw_input('Ready: ')
	dictionary = {}
	with open("capitols.txt") as fh:
		for line in fh:
			key, val = line.strip().split(',')
			dictionary[key.strip()] = val.strip()
			print dictionary.items()
			if user_input in dictionary.keys():
				print val
				break
			elif user_input in dictionary.values():
				print key
				break
			elif user_input ==  "Done":
				quit()
			else:
				print "nil"
				break