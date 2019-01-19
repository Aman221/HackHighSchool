from collections import defaultdict 

def state(): 
	dct = defaultdict(list)
	dct2 = defaultdict(list)

	with open('names.txt') as fp: 
		line = fp.readline()
		while line:
			line = line.strip('\n')
			arr = line.split('\t')

			for x in arr[:-1]:
				dct[arr[-1].strip('\t')].append(x) 

			for x in arr[:-1]: 
				values = arr[-1].strip(' ')
				dct2[x].append(values.strip('\t'))
			line = fp.readline()

	print '\n'
	print 'Shared First Names!'
	for x in dct2.iteritems():
		if len(x[1]) > 1:
			print (x[0] + "(" + str(len(x[1])) + "): ") + str(x[1])
	print '\n'			
	print 'Shared Last Names!'
	for x in dct.iteritems():
		if len(x[1]) > 1:
			print (x[0 ]+ "(" + str(len(x[1])) + "): ") + str(x[1])
state()

