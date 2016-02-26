#Euler Project 15
#Thinginitself

def C(n,k):
	res = 1
	for i in xrange(1, k+1):
		res *= n - i + 1
		res /= i
	return res

print C(40, 20)