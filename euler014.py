#Euler Project 14
#Thinginitself

MYMAX = 1000000
MAXINT = MYMAX * 3

length = [0] * MAXINT

length[1] = 1

def change(n):
	if n % 2 == 0:
		return n / 2
	else:
		return n * 3 + 1

def collatzLength(n):
	if n < MAXINT and length[n] > 0:
		return length[n]
	path = [n]
	myLength = 1
	while n != 1:
		n = change(n)
		path.append(n)
		myLength += 1
		if n < MAXINT and length[n] > 0:
			myLength += length[n] - 1
			break
	for i in xrange(len(path)):
		if path[i] < MAXINT:
			length[path[i]] = myLength - i

	return myLength

def maxCollatzLengthUnderK(k):
	maxLength = 0
	number = 0
	for i in xrange(1,k):
		x = collatzLength(i)
		if x > maxLength:
			maxLength = x
			number = i
	return number

print maxCollatzLengthUnderK(MYMAX)