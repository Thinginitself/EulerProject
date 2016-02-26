#Euler Project 79
#Thinginitself

with open("euler079_keylog.txt",'r') as f:
	s = f.read()

arr = list(set(s.split('\n')))

behind = list()
for i in xrange(10):
	behind.append(set())

for i in arr:
	a0 = int(i[0])
	a1 = int(i[1])
	a2 = int(i[2])
	behind[a0].add(a2)
	behind[a1].add(a2)
	behind[a0].add(a1)

for i in xrange(10):
	print i,':',tuple(behind[i])
