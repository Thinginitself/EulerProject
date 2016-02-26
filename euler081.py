#Euler Project 81
#Thinginitself

import re

with open('euler081_matrix.txt','r') as f:
	s = f.read()
num =  map(int, re.split('[,\n]',s))

mysum = [0] * 6400

mysum[0] = num[0]

for i in xrange(1,80):
	mysum[i] = mysum[i-1] + num[i]
	mysum[i*80] = mysum[(i-1)*80] + num[i*80]

for i in xrange(1,80):
	for j in xrange(1,80):
		mysum[i*80+j] = min(mysum[i*80+j-1], mysum[i*80+j-80]) + num[i*80+j]

print mysum[-1]