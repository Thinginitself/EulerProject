#Euler Project 29
#Thinginitself

res = 0
f = set()
for a in xrange (2, 101):
	for b in xrange(2, 101):
		x = pow(a, b)
		if not (x in f):
			res += 1
			f.add(x)

print res