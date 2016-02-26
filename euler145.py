#Euler Project 145
#Thinginitself

res = 0

def reversible(n):
	global res
	if n %10 == 0:
		return False
	l = list()
	while n > 0:
		l.append(n % 10)
		n /= 10
	length = len(l)
	if l[0]<l[length-1]:
		return False
	new = [0] * (length+1)
	for i in xrange(length):
		new[i] += l[i] + l[length-1-i]
		if new[i]%2 == 0:
			return False
		new[i+1] += new[i]/10
	res += 1
	return True


for i in xrange(10 ** 6):
	reversible(i)
print res