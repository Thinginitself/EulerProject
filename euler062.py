#Euler Project 62
#Thinginitself

tenTime = [10 ** x for x in xrange(13)]

def myhash(n):
	res = 0
	while n>0:
		k = n%10
		res += tenTime[k]
		n /= 10
	return res

mydic = {}
z = 1000000000
for i in xrange(345,100000):
	x = i*i*i
	k = myhash(x)
	if mydic.has_key(k):
		mydic[k][1] += 1
		if mydic[k][1]==5 and mydic[k][0]<z:
			z = mydic[k][0]
			print z,z*z*z
	else:
		mydic[k] = [i,1]