#Euler Project 12
#Thinginitself

import math

def triangle(n):
	return n * (n + 1) / 2

def factorNumber(n):
	num = 0
	sq = int(math.sqrt(n))
	for i in xrange(1, sq+1):
		if n%i == 0:
			num += 2
	if n == sq * sq:
		num -= 1
	return num

def firstTriangleNumberOverKdivisors(numberOfDivors):
	for i in xrange(1, 1000000000):
		x = factorNumber(triangle(i))
		if  x >= numberOfDivors:
			return triangle(i)
print firstTriangleNumberOverKdivisors(500)