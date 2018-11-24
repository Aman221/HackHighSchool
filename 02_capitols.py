while True:
	import csv
	user_input = raw_input('Ready: ')
	fh = csv.reader(open("capitols.txt", "r"))
	dictionary = {}	
	for line in fh:
		key, val = line
		dictionary[key] = val
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