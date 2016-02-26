#Euler Project 114
#Thinginitself

f = [0] * 100

f[0] = 1


for i in xrange(1,59):
	f[i] = f[i-1]
	for j in xrange(11,i+2):
		if i-j==-1:
			f[i] += 1
		f[i] += f[i-j]

print f[7],f[56]