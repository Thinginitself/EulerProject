#Euler Project 52
#Thinginitself

import itertools

def fullarraySet(s):
	myarray = itertools.permutations(s,len(s))
	resarray = set()
	def turntonum(a):
		res = 0
		for x in a:
			res *= 10
			res += ord(x) - ord('0')
		return res
	for i in myarray:
		resarray.add(turntonum(i))
	return resarray

for i in xrange(1,10000000):
	myset = fullarraySet(str(i))
	flag = 1
	for j in xrange(2,7):
		if not j*i in myset:
			flag = 0
			break
	if flag == 1:
		print i
		break
