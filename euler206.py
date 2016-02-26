#Euler Project 206
#Thinginitself

#1_2_3_4_5_6_7_8_9_0
#1_2_3_4_5_6_7_8_900

import math

tentime = [(100 ** x) /10 for x in xrange(10)]


f = [[],[],[],[],[],[],[],[],[],[]]
f[0] = [3,7]

def match(n):
	if len(str(n))!=17:
		return False
	for i in xrange(8):
		n /= 100
		if n%10 != (8-i):
			return False
	return True

for i in xrange(1,5):
	for j in f[i-1]:
		for k in xrange(100):
			tmp = j+k*tentime[i]
			ans = tmp*tmp
			if (ans/(tentime[i]*10))%10==(9-i):
				f[i].append(tmp)

for i in f[4]:
	if match(i*i):
		print i,i*i