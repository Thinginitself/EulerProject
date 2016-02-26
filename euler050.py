#Euler Project 50
#Thinginitself

from mylib import primes

primes = primes.primeList(1000000)
primeset = set(primes)
primes = [i for i in primes if i < 100000]
l = len(primes)
print l
sumofprimes = [0]
for i in xrange(1,l+1):
	sumofprimes.append(sumofprimes[i-1] + primes[i-1])
mymax = myprime = 0
for i in xrange(l-1):
	for j in xrange(i+2,l+1):
		x = sumofprimes[j] - sumofprimes[i]
		if x in primeset and j-i>mymax:
			mymax = j-i
			myprime = x

print myprime
