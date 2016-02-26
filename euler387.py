#Euler Project 387
#Thinginitself

import mylib.primes as primes


mymax = 13
q = []
for i in xrange(mymax+1):
	q.append({})
q[0] = {0:0}


for times in xrange(mymax):
	for (i,v) in q[times].items():
		for k in xrange(10):
			tmp = k + i*10
			if k+v!=0 and tmp%(k+v)==0:
				q[times+1][tmp] = k+v

res = 0
for l in xrange(1,mymax+1):
	for (i,k) in q[l].items():
		if primes.isprime(i/k):
			tmp = 10 * i
			for j in xrange(10):
				if primes.isprime(j+tmp):
					res += tmp +j

print res