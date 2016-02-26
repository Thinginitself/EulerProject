#Euler Project 243
#Thinginitself

import math
import mylib.primes as primes
#23 223092870 0.163588195356 0.163588196089

p = primes.primeList(10 ** 5)

small = 15499.0/94744

res = 0.163588195356
d = 223092870

for j in xrange(2,29):
	if res*(d*j)/(d*j-1)<small:
		print j,d*j
		break