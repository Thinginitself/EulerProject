#Euler Project 45
#Thinginitself

SIZE = 200000

triangle = [n*(n+1)/2 for n in xrange(SIZE)]
pentagon = [n*(3*n-1)/2 for n in xrange(SIZE)]
hexagon  = [n*(2*n-1) for n in xrange(SIZE)]

triangleSet = set(triangle)
pentagonSet = set(pentagon)

for x in hexagon:
	if x in triangleSet and x in pentagonSet:
		print x