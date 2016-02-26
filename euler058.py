#Euler Project 58
#Thinginitself

import mylib.primes

myprime = mylib.primes.primeList(10 ** 6)

num = dem = 0.0

res = 0
for i in xrange(10 ** 5):
	t1 = (2*i+1)*(2*i+1) + (2*i+1) + 1
	t2 = t1 + (2*i+2)
	t3 = t2 + (2*i+2)
	t4 = t3 + (2*i+2)
	if mylib.primes.isprime(t1):
		num += 1
	if mylib.primes.isprime(t2):
		num += 1
	if mylib.primes.isprime(t3):
		num += 1
	if mylib.primes.isprime(t4):
		num += 1
	dem += 4
	if num/dem <= 0.1:
		print 2*i+3
		break

