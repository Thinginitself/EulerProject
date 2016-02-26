#Euler Project 71
#Thinginitself

for i in xrange(10 ** 6):
	j = 10**6 - i
	if j*3%7==1:
		print (j*3-1)/7
		break