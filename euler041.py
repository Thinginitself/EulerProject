#Euler Project 41
#Thinginitself

from math import sqrt

import itertools

def fullarray(n):
	myarray = itertools.permutations(range(1,n+1),n)
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

def isprime(n):
	for i in xrange(2,int(sqrt(n))):
		if n % i == 0:
			return False
	return True

maxnum = 0
for i in xrange(1,10):
	myarray = fullarray(i)
	for j in myarray:
		if isprime(j) and j>maxnum:
			maxnum = j
print maxnum