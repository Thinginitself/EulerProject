#Euler Project 31
#Thinginitself

f = [1, 2, 5, 10, 20, 50, 100, 200]

g = [0] * 201
g[0] = 1
	
for j in f:
	for i in xrange(201):
		if i >= j:
			g[i] += g[i-j]

print g[200]