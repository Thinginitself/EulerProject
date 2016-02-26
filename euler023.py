#Euler Project 23
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

abnumber = filter(lambda x: sumOfFactors(x) > x, xrange(1,28124))
f = [0] * 60000
for x in abnumber:
	for y in abnumber:
		f[x+y] = 1
res = 0;
for i in xrange(1,30000):
	if f[i] == 0:
		res += i 

print res