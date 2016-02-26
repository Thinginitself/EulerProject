#Euler Project 4
#Thinginitself

def ispa(x):
	l = []
	pos = 0
	flag = True
	while x >= 1:
		l.append(x % 10)
		x = x / 10 
		pos = pos + 1
	for i in range(pos):
		if l[i] != l[pos-1-i]:
			flag = False
			break
	return flag


maxOne = 0
for i in xrange(100,1000):
	for j in xrange(100,1000):
		x = i * j
		if ispa(x) and x > maxOne:
			maxOne = x
print maxOne
			