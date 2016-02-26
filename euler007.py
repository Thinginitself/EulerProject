#Euler Project 7
#Thinginitself

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

primes = primeList(10000000)

print primes[10000]