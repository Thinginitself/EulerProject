#Euler Project 72
#Thinginitself

import math


fac = [0] * 10 ** 7
f = [0] * 10 ** 7

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

getEulerfuc(10 ** 6 + 1)

print sum(f)
