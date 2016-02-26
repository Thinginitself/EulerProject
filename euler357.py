#Euler Project 357
#Thinginitself

import mylib.primes as primes
import math


mymax = 10 ** 8
p = primes.primeSet(mymax)

def isok(n):
	l = int(math.sqrt(n))
	for j in xrange(1,l+1):
		if n % j == 0:
			if not ((j+(n/j)) in p):
				return False
	return True


res = 0
for i in xrange(mymax):
	if isok(i):
		res += i

print res
