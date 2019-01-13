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
d = {k:str(v) for k, v in c.iteritems()}
pk = {v:[k for k in c if c[k] == v] for v in c.itervalues()}
del pk[1] 
print pk
y = collections.Counter(lov)
z = {k:str(v) for k, v in y.iteritems()}
pv = {v:[k for k in y if y[k] == v] for v in y.itervalues()}
del pv[1]
print pv