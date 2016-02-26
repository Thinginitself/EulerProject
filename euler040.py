#Euler Project 40
#Thinginitself

from math import log

s = ""
i = 0
while len(s) < 1000000:
	i += 1
	s += str(i)

res = 1
m = 1
for i in xrange(6):
	m *= 10
	z = int(s[m-1])
	print z,m
	res *= z
print res