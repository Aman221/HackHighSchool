import sys
for x in sys.argv:
		print "Argv of " + str(sys.argv.index(x)) + " is " + x
sys.argv.sort(key = len, reverse = True)
for x in sys.argv:
	print x