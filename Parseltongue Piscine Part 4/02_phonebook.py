import collections
lok = []
lov = []
f = open('names.txt', 'r')
dictionary = dict()
for line in f.readlines():
	key, val = line.strip().split(None, 1) 
	dictionary[key.strip()] = val.strip()
	w = list(key)
	x = "".join(w)
	lok.append(x)
	a = list(val)
	b = "".join(a)
	lov.append(b)
c = collections.Counter(lok)
d = [k for k, v in c.iteritems() if v > 1]
y = collections.Counter(lov)
z = [k for k, v in y.iteritems() if v > 1]

