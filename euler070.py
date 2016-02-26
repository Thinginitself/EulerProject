#Euler Project 70
#Thinginitself


import math
import mylib.primes as primes

limit = 10 ** 7

p = primes.primeList(10 ** 4)


fac = [0] * limit
f = [0] * limit

def getEulerfuc(size):
	for i in xrange(2,size):
		if fac[i]!=0:
			tmp = i/fac[i]
			if tmp%fac[i]==0:
				f[i] = f[tmp]*fac[i]
			else:
				f[i] = f[tmp]*(fac[i]-1)
		else:
			f[i] = i-1
			for j in xrange(i*i,size,i):
				if fac[j]==0:
					fac[j] = i

def permutation(n,m):
	qn = [0] * 10
	qm = [0] * 10
	while n > 0:
		qn[n%10] += 1
		n /= 10
	while m > 0:
		qm[m%10] += 1
		m /= 10
	for i in xrange(10):
		if qn[i]!=qm[i]:
			return False
	return True



getEulerfuc(limit)
print "getEulerfuc Done"

mymax = 87109.0/79180.0
myn = 0
for i in xrange(2,limit):
	tmp = (i+0.0)/f[i]
	if tmp < mymax and permutation(i,f[i]):
		mymax = tmp
		myn = i

print myn,mymax


