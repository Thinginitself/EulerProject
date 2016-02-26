#Euler Project 49
#Thinginitself

#1.primes 2.permutations 3.increase sequences

from mylib import primes


def count(n):
	res = 0
	while n > 0:
		last = n % 10
		res += 10 ** last
		n /= 10
	return res

def permutations(a, b, c):
	ca = count(a)
	cb = count(b)
	cc = count(c)
	if ca == cb and ca == cc:
		return True
	else:
		return False


tmp = primes.primeList(10 ** 4)
myprimes = filter(lambda x: x>1000,tmp)

myset = set(myprimes)

l = len(myprimes)

for i in xrange(l):
	for j in xrange(i+1,l):
		new = myprimes[j] * 2 - myprimes[i]
		if new in myset and permutations(myprimes[i],myprimes[j],new):
			print myprimes[i], myprimes[j], new