#Euler Project 27
#Thinginitself

def primeSet(n):
	mylist = []
	pl = [1] * (n+1)
	pl[0] = pl[1] = 0
	num = 2
	while num < n:
		mylist.append(num)
		x = num * num
		while x < n:
			pl[x] = 0
			x += num
		num += 1
		while not pl[num] and num<n:
			num += 1
	return mylist

myprimes = primeSet(2000001)
primes = set(myprimes)
myprimes = [i for i in myprimes if i < 1000]

res = 0
ansA = ansB = 0
for a in xrange(-999, 1000):
	for b in myprimes:
		now = 0
		for n in xrange(1000):
			x = n*n + a*n + b
			if not x in primes:
				now = n
				break
		if now > res:
			res = now
			ansA = a
			ansB = b
print ansA*ansB