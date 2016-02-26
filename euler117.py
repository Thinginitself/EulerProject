#Euler Project 117
#Thinginitself

n = 50

f = [0] * (n+3)
f[0] = 1
for i in xrange(1,n+1):
	f[i] = f[i-1]
	if i > 1:
		f[i] += f[i-2]
	if i > 2:
		f[i] += f[i-3]
	if i > 3:
		f[i] += f[i-4]

print f[n]

