#Euler Project 37
#Thinginitself

def primeSet(n):
	mylist = set()
	pl = [1] * (n+1)
	pl[0] = pl[1] = 0
	num = 2
	while num < n:
		mylist.add(num)
		x = num * num
		while x < n:
			pl[x] = 0
			x += num
		num += 1
		while not pl[num] and num<n : 
			num += 1
	return mylist

primes = primeSet(1000000)

def ok(x):
	if x < 10:
		return False
	now = x
	while now > 0:
		if not (now in primes):
			return False
		now //= 10
	div = 10
	while x > div:
		if not ((x % div) in primes):
			return False
		div *= 10
	return True

res = 0
count = 0
for i in primes:
	if ok(i):
		print i
		res += i

print res
