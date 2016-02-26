#Euler Project 21
#Thinginitself

import math



def sumOfFactors(n):
	res = 1
	sq = int(math.sqrt(n))
	for i in xrange(2, sq+1):
		if n%i == 0:
			res += i + n / i
	if n == sq * sq:
		res -= sq
	return res

def sumOfAmicableNumbers(n):
	res = 0
	for i in xrange(2,n):
		x = sumOfFactors(i)
		y = sumOfFactors(x)
		if i == y and i != x:
			res += i
	return res


print sumOfAmicableNumbers(10000)