#Euler Project 35
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

f = [False] * 1000000
v = [0] * 1000000

def circle(x):
	l = len(str(x))
	circleList = [x]
	for i in xrange(l-1):
		temp1 = x / (10 ** (l-1))
		temp2 = x % (10 ** (l-1))
		x = temp2 * 10 + temp1
		circleList.append(x)
	return circleList

def colored(x):
	if '0' in set(str(x)):
		f[x] = True
		return
	mylist = circle(x)
	flag = True
 	for i in mylist:
 		f[i] = True
		if not (i in primes):
			flag = False
	if flag:
		for i in mylist:
			v[i] = 1

for i in xrange(1,1000000):
	if not f[i]:
		colored(i)

print sum(v)
