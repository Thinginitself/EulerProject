#Euler Project 47
#Thinginitself

from mylib.primes import primeList

primes = primeList(1000000)

def primeFactorNumber(n):
	res = 0
	for i in primes:
		if i > n:
			break
		if n%i == 0:
			res += 1
		while n%i == 0 and n>=i:
			n = n/i
	return res

def consecutive(n, m):
	con = 0
	for i in xrange(3,10000000):
		if primeFactorNumber(i) == m:
			con += 1
		else:
			con = 0
		if con == n:
			return i
	return -1

print consecutive(4,4)