import statistics
import sys

def is_intstring(s):
    try:
        int(s)
        return True
    except ValueError:
        return False

for arg in sys.argv[1:]:
    if not is_intstring(arg):
        sys.exit("All arguments must be integers. Exit.")

array = sys.argv[1:]
sorted_array = sorted(array, key=int)
array_4_processing = map(int, sorted_array)

def find_minimum():
	print "The Minimum is " + str(array_4_processing[0])

def find_maximum():
	print "The Maximum is " + str(array_4_processing[-1])

def find_range():
	print "The Range is " + str((array_4_processing[-1]) - (array_4_processing[0]))

print "The Mean is " + str(statistics.mean(array_4_processing))
print "The Mode is " + str(statistics.mode(array_4_processing))
print "The Median is " + str(statistics.median(array_4_processing))
find_minimum()
find_maximum()
find_range()