#Euler Project 87
#Thinginitself

import mylib.primes as primes

p = primes.primeList(10 ** 4)
mymax = 50 * 10 ** 6
myset = set()

for i in p:
	fi = i*i*i*i
	if fi>mymax:
		break
	for j in p:
		fj = j*j*j
		if fi+fj>mymax:
			break
		for k in p:
			fk = k*k
			if fi+fj+fk>mymax:
				break
			myset.add(fi+fj+fk)
		


print len(myset)
