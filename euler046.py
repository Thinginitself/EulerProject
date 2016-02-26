#Euler Project 46
#Thinginitself

SIZE = 10000

def primeList(n):
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

primes = primeList(SIZE)
primeSet = set(primes)

f = [0] * SIZE

for i in primes:
	for j in xrange(100):
		x = i + 2*j*j
		if x > SIZE:
			break
		f[x] = 1
for i in xrange(1,SIZE):
	if f[2*i+1] == 0 and not i  in primes:
		print 2*i+1
		break




