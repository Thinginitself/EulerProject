#Euler Project 33
#Thinginitself

for i in xrange(1,10):
	for j in xrange(1,10):
		if i == j:
			continue
		for k in xrange(1,10):
			if (i*10+k)*j == (k*10+j)*i:
				print i,j,k
#need some calculation