#Euler Project 114
#Thinginitself

limit = 10 ** 6


def func(m,n):
	f = [0] * (n+2)
	f[0] = 1
	for i in xrange(1,n+1):
		f[i] = f[i-1]
		for j in xrange(m+1,i+2):
			if i-j==-1:
				f[i] += 1
			f[i] += f[i-j]
	return f[n]

for i in xrange(51,1000):
	if func(50,i) > limit:
		print i
		break
