# import collections
# lok = []
# lov = []
# f = open('names.txt', 'r')
# dictionary = dict()
# for line in f.readlines():
# 	key, val = line.strip().split(None, 1) 
# 	dictionary[key.strip()] = val.strip()
# 	w = list(key)
# 	x = "".join(w)
# 	lok.append(x)
# 	a = list(val)
# 	b = "".join(a)
# 	lov.append(b)
# c = collections.Counter(lok)
# d = [k for k, v in c.iteritems() if v > 1]
# y = collections.Counter(lov)
# z = [k for k, v in y.iteritems() if v > 1]
# for name in second_first_names:
#    if second_first_names.count(name) > 1:
#        repeated_first_names.append([name, first_names.count(name)])
#        while second_first_names.count(name) > 0:
#            repeated_first_names.append(second_last_names[second_first_names.index(name)])
#            second_last_names.pop(second_first_names.index(name))
#            second_first_names.pop(second_first_names.index(name))

# #Does the same thing for the last_names (Notice that second_last_names wasn't used because it has already been modified)
# for name in last_names:
#    if last_names.count(name) > 1:
#        repeated_last_names.append([name, last_names.count(name)])
#        while last_names.count(name) > 0:
#            repeated_last_names.append(first_names[last_names.index(name)])
#            first_names.pop(last_names.index(name))
#            last_names.pop(last_names.index(name))
# 	dict = Hash.new {|h, k| h[k] = []}
# 	Open file here read_lines.each {|line|}
# 		arr = line.split(' ')
# 		arr[0...-1].each {|name| dict[arr.last] << name}
# 	end
# end

# arr = [1]
# arr << 2	
# arr = [1, 2]
from collections import defaultdict 

def state(): 
	dct = defaultdict(list)
	with open('names.txt') as fp: 
		line = fp.readline()
		while line:
			line = line.strip('\n')
			arr = line.split('\t')
			for x in arr[:-1]:
				dct[arr[-1].strip('\t')].append(x) 
				#print (dct[arr[-1].strip('\t')])
			line = fp.readline()

	print (dct)
state()

