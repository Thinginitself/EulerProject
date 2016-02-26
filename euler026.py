#Euler Project 26
#Thinginitself

def cycle(n):
	f = {}
	rem = 1
	pos = 0
	while not f.has_key(rem):
		f[rem] = pos
		pos += 1
		rem *= 10
		rem %= n
	return pos - f[rem]

res = 0
maxlen = 0
for i in xrange(1,1000):
	x = cycle(i)
	if x > maxlen:
		res = i
		maxlen = x

print res,maxlen