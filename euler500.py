#Euler Project 500
#Thinginitself

import mylib.primes as primes
import math

mod = 500500507
times = 500500

p = primes.primeList(10 * (10 ** 6))

pp = []

for i in p:
	tmp = i
	while tmp < p[-1]:
		pp.append(tmp)
		tmp = tmp*tmp

pp.sort()

print pp[:100]
res = 1
for i in xrange(times):
	res *= pp[i]
	res %= mod

print res