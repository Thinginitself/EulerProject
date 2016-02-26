#Euler Project 48
#Thinginitself

LARGENUM = 10 ** 10

res = 0
for i in xrange(1,1001):
	res += (i ** i)
	

print res%LARGENUM