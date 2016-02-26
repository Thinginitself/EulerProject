#Euler Project 116
#Thinginitself

def func(m,n):
	f = [0] * (n+3)
	f[0] = 1
	for i in xrange(1,n+1):
		f[i] = f[i-1] + f[i-m]
	return f[n]-1	

print func(2,50) + func(3,50) + func(4,50)