#Euler Project 381
#Thinginitself

#-3 = x * 8 (mod p)
#p * i + 8 * x = -3

import mylib.primes as primes

p = primes.primeList(10 ** 8)
res = 0

# ans = x^-1 mod m
def work(x,m):
	y = x
	x = m
	a = 0
	b = 1
	while y!= 0:
		a, b = b, a - x // y * b
		x, y = y, x % y
	if x == 1:
		return  a % m

for i in p[2:]:
	tmp = (i-3) * work(8%i,i) % i
	res += tmp

print res
