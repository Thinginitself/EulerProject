#Euler Project 38
#Thinginitself



def connect(x,y):
	i = 1
	while i < y:
		i *= 10
	return x * i + y

def ispandigital(x):
	v = [0] * 10
	while x > 0:
		v[x % 10] += 1
		x = x / 10
	if v[0] != 0:
		return False
	for i in xrange(1,10):
		if v[i] != 1:
			return False
	return True	


def ok(n):
	res = n
	for i in xrange(2,10):
		res = connect(res,i*n)
		if res > 10 ** 8:
			break
	if res > 10 ** 9 or (not ispandigital(res)):
		return -1
	else:
		return res

mymax = 0
for i in xrange(10000):
	x = ok(i)
	if x > mymax:
		mymax = x
print mymax

