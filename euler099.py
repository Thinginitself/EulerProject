#Euler Project 99
#Thinginitself

import re,math

with open('euler099_base.txt','r') as f:
	s = f.read()
num =map(int, re.split('[,\n]',s))

maxnum = 0
line = 0
for i in xrange(1000):
	tmp = math.log(num[2*i])*num[2*i+1]
	if tmp > maxnum:
		maxnum = tmp
		line = i+1

print line