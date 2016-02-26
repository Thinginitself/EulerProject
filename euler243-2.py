import math
import mylib.primes as primes

p = primes.primeList(10 ** 5)

small = 15499.0/94744
ans = 1.0
res = 1
for i in p:
	ans *= i-1
	ans /= i
	res *= i
	tmp = ans*res/(res-1)
	print i,res,ans,tmp
	if ans<small:
		break