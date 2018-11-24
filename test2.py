user_input = raw_input('Ready: ')
f = open('capitols.txt', 'r')
dictionary = dict()
for line in f:
	key, val = line.strip().split(',')
	dictionary[key.strip()] = val.strip()
	if user_input in dictionary.iterkeys():
		print dictionary[key]
		break