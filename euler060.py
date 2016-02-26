#Euler Project 60
#Thinginitself

from mylib import primes

myprime = primes.primeList(10 ** 8)
myprime.remove(2)
myset = set(myprime)
maxprime = max(myprime)
p = [x for x in myprime if x < 10 ** 5]


def isprime(n):
	if n in myset:
		return True
	elif n > maxprime:
		return primes.isprime(n)
	return False

def combine(a,b):
	z = 10
	while z<b:
		z *= 10
	return isprime(a*z+b) 

def ok(a,b):
	return combine(a,b) and combine(b,a)

def ok_with_list(a,l):
	for i in l:
		if not ok(a,i):
			return False
	return True

def dfs(l):
	if len(l)==5:
		print l
		return 
	for i in p:
		if len(l)==0 or (i > max(l) and ok_with_list(i,l)):
			l.append(i)
			dfs(l)
			l.remove(i)

dfs([])