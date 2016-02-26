#Euler Project 44
#Thinginitself

pentagon = [n*(3*n-1)/2 for n in xrange(1,10000)]

pentagonSet = set(pentagon)

mymin = 1000000000

for i in pentagon:
	for j in pentagon:
		if i-j in pentagonSet and i+j in pentagonSet:
			print i,j
			if i-j< mymin:
				mymin = i-j

print mymin