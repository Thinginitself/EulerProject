#Euler Project 53
#Thinginitself

one_million = 10 ** 6
res = 0
for n in xrange(1,101):
	val = 1
	for r in xrange(1,n+1):
		val = val * (n+1-r) / r
		if val > one_million:
			res += 1

print res