#Euler Project 55
#Thinginitself

def isPalindrome(x,k=10):
	l = []
	while x > 0:
		l.append(x % k)
		x /= k
	length = len(l)
	for i in xrange(length):
		if l[i] != l[length-1-i]:
			return False
	return True

def change(x):
	l = []
	while x > 0:
		l.append(x%10)
		x /= 10
	length = len(l)
	res = 0
	num = 1
	for i in xrange(length):
		res += num * (l[i]+l[length-1-i])
		num *=10
	return res


def isLychrel(x):
	for i in xrange(50):
		x = change(x)
		if isPalindrome(x):
			return False
	return True

count = 0
for i in xrange(10000):
	if isLychrel(i):
		count += 1
print count


