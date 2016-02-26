#Euler Project 25
#Thinginitself

x = 1
y = 1
big = pow(10,999)
pp = 2
for i in xrange (100000):
	z = x + y
	pp += 1
	if z > big:
		print pp
		break
	x = y
	y = z 

