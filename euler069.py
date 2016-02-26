#Euler Project 69
#Thinginitself

import mylib.primes

myprime = mylib.primes.primeList(10 ** 4)

res = 1
i = 0
MAX_NUM = 10 ** 6

while res * myprime[i] <= MAX_NUM:
	res *= myprime[i]
	i += 1

print res