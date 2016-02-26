#Euler Project 63
#Thinginitself

count = 0
for i in xrange(1,10):
	for j in xrange(1,100):
		l = len(str(i ** j))
		if l==j:
			count += 1
		elif l<j:
			break

print count