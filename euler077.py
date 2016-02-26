#Euler Project 77
#Thinginitself

import mylib.primes as primes

p = primes.primeList(10 ** 6)

f = [0] *  (10 ** 7)

f[0] = 1
for j in p:
	if j > 1000:
		break
	for i in xrange(2,1000):
		f[i] += f[i-j]
for i in xrange(1000):
	if f[i] > 5000:
		print i
		break