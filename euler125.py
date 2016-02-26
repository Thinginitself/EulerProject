#Euler Project 125
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

f = [0,1]
mymax = 10 ** 8


for i in xrange(2,10 ** 4+1):
	tmp = f[i-1]+i*i
	if tmp-f[i-2] > mymax:
		break
	f.append(tmp)

length = len(f)

mysum = 0
for i in xrange(length):
	for j in xrange(i+2,length):
		tmp = f[j] - f[i]
		if tmp < mymax:
			if isPalindrome(tmp):
				mysum += tmp

print mysum
