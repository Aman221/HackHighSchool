from numpy import loadtxt
key_value = loadtxt("capitols.txt", delimiter=",")
dictionary = {k:v for k,v in key_value}
print k
print v