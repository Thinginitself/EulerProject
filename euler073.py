#Euler Project 73
#Thinginitself

from fractions import gcd


res = 0
for i in xrange(5,12001):
	l = i / 3 + 1
	h = i / 2 + 1
	for j in xrange(l,h):
		if gcd(i,j) == 1:
			res += 1

print res