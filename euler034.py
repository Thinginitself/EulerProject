#Euler Project 34
#Thinginitself

from math import factorial

pos = 10

f = []

for i in xrange(10):
	f.append(factorial(i))
c = [0] * 10
res = 0
print f
def ok(x):
	v = [0] * 10
	while x > 0:
		v[x % 10] += 1
		x = x / 10
	for i in xrange(10):
		if v[i] != c[i]:
			return False
	return True

def dfs(k, last, mysum):
	if k == 0:
		c[0] = last
		mysum += last
		if ok(mysum):
			print mysum
			global res
			res += mysum 
		return 

	for i in xrange(last+1):
		newsum = mysum + f[k] * i
		c[k] = i
		dfs(k-1, last-i, newsum)

for i in xrange(2,10):
	dfs(9,i,0)
print res