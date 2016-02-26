#Euler Project 43
#Thinginitself

from math import sqrt

import itertools

def fullarray(n):
	myarray = itertools.permutations(range(n),n)
	resarray = []
	def turntonum(a):
		res = 0
		for x in a:
			res *= 10
			res += x
		return res
	for i in myarray:
		resarray.append(turntonum(i))
	return resarray

def strangeDivisible(x):
	primeList = [17, 13, 11, 7, 5, 3, 2]
	for i in primeList:
		z = x % 1000
		x = x / 10
		if z%i != 0:
			return False
	return True

print sum(filter(strangeDivisible, fullarray(10)))