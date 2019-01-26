import math
import sys
from collections import Counter

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

def find_median():
	middle = (len(array_4_processing) - 1) / 2
	print "The Median is " + str(array_4_processing[middle])

def find_mean():
	print "The Mean is " + (str((sum(array_4_processing))/(len(array_4_processing))))

def find_mode():
	data = Counter(array_4_processing)
	print "The Mode is " + str(data.most_common(1)[0][0])

find_minimum()
find_maximum()
find_range()
find_median()
find_mean()
find_mode()