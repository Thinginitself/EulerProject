#Euler Project 112
#Thinginitself

def isBoncy(n):
	num = map(int,list(str(n)))
	flag = 0
	for i in xrange(1,len(num)):
		if num[i]==num[i-1]:
			continue
		if num[i]<num[i-1] and flag == 1:
			return True
		if num[i]>num[i-1] and flag == -1:
			return True
		if num[i]>num[i-1]:
			flag = 1
		if num[i]<num[i-1]:
			flag = -1
	return False

boncy = 0
for i in xrange(100,10000000):
	if isBoncy(i):
		boncy += 1
	if (boncy+0.0)/i >= 0.99:
		print i
		break
