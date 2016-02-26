#Euler Project 56
#Thinginitself

mymax = 0
for i in xrange(100):
	for j in xrange(100):
		res = i ** j
		num_sum = sum(map(int,str(res)))
		if num_sum > mymax:
			mymax = num_sum

print mymax