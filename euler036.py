#Euler Project 36
#Thinginitself

def isPalindrome(x,k):
	l = []
	while x > 0:
		l.append(x % k)
		x /= k
	length = len(l)
	for i in xrange(length):
		if l[i] != l[length-1-i]:
			return False
	return True


mysum = 0
for i in xrange(1000000):
	if isPalindrome(i,10) and isPalindrome(i,2):
		mysum += i

print mysum
