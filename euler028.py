#Euler Project 28
#Thinginitself


res = 1

for i in xrange(1, 501):
	res += 20 * i
	res += 4 * (2 * i - 1) * (2 * i - 1)

print res